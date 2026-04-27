#
# Copyright (C) 2023, Inria
# GRAPHDECO research group, https://team.inria.fr/graphdeco
# All rights reserved.
#
# This software is free for non-commercial, research and evaluation use
# under the terms of the LICENSE.md file.
#
# For inquiries contact george.drettakis@inria.fr
#

import os
from argparse import ArgumentParser
from os import makedirs

import torch
import torchvision
from tqdm import tqdm

from arguments import ModelParams, PipelineParams, get_combined_args
from gaussian_renderer import GaussianModel, render
from scene import Scene
from utils.general_utils import safe_state
from utils.render_utils import create_videos, generate_path


def render_cameras(output_dir, name, cameras, gaussians, pipeline, background, save_gt=True):
    render_dir = os.path.join(output_dir, name, "renders")
    gt_dir = os.path.join(output_dir, name, "gt")
    makedirs(render_dir, exist_ok=True)
    if save_gt:
        makedirs(gt_dir, exist_ok=True)

    for idx, view in enumerate(tqdm(cameras, desc=f"Rendering {name}")):
        rendering = render(view, gaussians, pipeline, background)["render"]
        image_name = getattr(view, "image_name", f"{idx:05d}")
        torchvision.utils.save_image(rendering, os.path.join(render_dir, f"{image_name}.png"))
        if save_gt:
            torchvision.utils.save_image(view.original_image, os.path.join(gt_dir, f"{image_name}.png"))

    return render_dir


if __name__ == "__main__":
    parser = ArgumentParser(description="UltraGS rendering parameters")
    model = ModelParams(parser)
    pipeline = PipelineParams(parser)
    parser.add_argument("--iteration", default=-1, type=int)
    parser.add_argument("--skip_train", action="store_true")
    parser.add_argument("--skip_test", action="store_true")
    parser.add_argument("--quiet", action="store_true")
    parser.add_argument("--render_path", action="store_true")
    parser.add_argument("--num_frames", default=240, type=int)
    args = get_combined_args(parser)

    print("Rendering " + args.model_path)
    safe_state(args.quiet)

    dataset, iteration, pipe = model.extract(args), args.iteration, pipeline.extract(args)
    gaussians = GaussianModel(dataset.sh_degree)
    scene = Scene(dataset, gaussians, load_iteration=iteration, shuffle=False)

    bg_color = [1, 1, 1] if dataset.white_background else [0, 0, 0]
    background = torch.tensor(bg_color, dtype=torch.float32, device="cuda")
    output_dir = args.model_path
    method_name = f"ours_{scene.loaded_iter}"

    if not args.skip_train:
        render_cameras(output_dir, os.path.join("train", method_name), scene.getTrainCameras(), gaussians, pipe, background)

    if not args.skip_test and len(scene.getTestCameras()) > 0:
        render_cameras(output_dir, os.path.join("test", method_name), scene.getTestCameras(), gaussians, pipe, background)

    if args.render_path:
        traj_cameras = generate_path(scene.getTrainCameras(), n_frames=args.num_frames)
        traj_dir = render_cameras(output_dir, os.path.join("trajectory", method_name), traj_cameras, gaussians, pipe, background, save_gt=False)
        create_videos(
            base_dir=traj_dir,
            input_dir=traj_dir,
            out_name="render_traj",
            num_frames=args.num_frames,
        )
