# UltraGS

This project was created by [***Yuezhe Yang***](https://bean-young.github.io) for the paper "**UltraGS: Real-Time Physically-Decoupled Gaussian Splatting for Ultrasound Novel View Synthesis**" ([Paper Link](https://arxiv.org/abs/2511.07743)).

## ***Abstract***

Ultrasound imaging is a cornerstone of non-invasive clinical diagnostics, yet its limited field of view poses challenges for novel view synthesis. We present UltraGS, a real-time framework that adapts Gaussian Splatting to sensorless ultrasound imaging by integrating explicit radiance fields with lightweight, physics-inspired acoustic modeling. UltraGS employs depth-aware Gaussian primitives with learnable fields of view to improve geometric consistency under unconstrained probe motion, and introduces PD Rendering, a differentiable acoustic operator that combines low-order spherical harmonics with first-order wave effects for efficient intensity synthesis. We further present a clinical ultrasound dataset acquired under real-world scanning protocols. Extensive evaluations across three datasets demonstrate that UltraGS establishes a new performance-efficiency frontier, achieving state-of-the-art results in PSNR (up to 29.55) and SSIM (up to 0.89) while achieving real-time synthesis at 64.69 fps on a single GPU.


## ***Prepare Data***

To validate the effectiveness of our model, we conducted extensive experiments on three ultrasound datasets from different sources.

The details of the datasets used and their specific links will be provided here for easy access to the data.

### **Ultrasound in the Wild Dataset (Wild Dataset)**

*Ultrasound in the Wild Dataset (Wild Dataset)*: This dataset contains ten knee ultrasound samples acquired using a handheld Butterfly iQ+ probe at 30 FPS. The longitudinal suprapatellar sweeps include realistic motion artifacts and trajectory variations, making the dataset suitable for evaluating robustness under uncontrolled scanning conditions.

[Ultrasound in the Wild Dataset](https://huggingface.co/datasets/rishitdagli/us-in-the-wild): We used this dataset to evaluate the performance of UltraGS under handheld and unconstrained scanning scenarios.

### **Lumbar Spine Phantom Dataset (Phantom Dataset)**

*Lumbar Spine Phantom Dataset (Phantom Dataset)*: This dataset contains nine lumbar spine phantom scans acquired using a KUKA robotic manipulator. The tilted and perpendicular sweeps introduce spinous process occlusions, which are useful for testing geometric reconstruction under controlled but challenging conditions.

[Lumbar Spine Phantom Dataset](https://drive.google.com/drive/folders/1aDc3wA2gugUKS6IABsH_TNWQ5Ijk7tmi?usp=drive_link): We used this dataset to validate reconstruction quality under controlled ultrasound acquisition.

### **Clinical Ultrasound Examination Dataset (Clinical Dataset)**

*Clinical Ultrasound Examination Dataset (Clinical Dataset)*: This is our in-house clinical ultrasound dataset collected using the Canon i900 ultrasound system with institutional research ethics approval (Ethics Approval No.: SL2024-KY-29-01). It contains six challenging cases with unconstrained probe motion, anatomical occlusions, and realistic clinical scanning variability, including wrist joint and kidney scans.

[Clinical Ultrasound Examination Dataset](https://drive.google.com/drive/folders/19B9QHH03PwxXNSBaaPoGvEbw_Vzxul96?dmr=1&ec=wgc-drive-%5Bmodule%5D-goto): We used this dataset to validate the performance of UltraGS under real-world clinical ultrasound examination scenarios.


## ***Set Up***

### Pytorch 2.0 (CUDA 11.8)
Our experimental platform is configured with RTX 3090 GPU (CUDA 11.8), and the code runs in a PyTorch 2.0 environment.

For details on the environment, please refer to the future [`requirements.txt`](requirements.txt) file.

**Run the installation command:**
```bash
pip install -r requirements.txt
```

## ***Data Preprocessing***

Data preprocessing is divided into two stages:
1) We prepare ultrasound images and camera parameters for each sequence
2) We generate the corresponding training and testing lists.

To better adapt ultrasound data for Gaussian Splatting and ensure optimal reconstruction performance, we will provide the packaged preprocessing code after the data release. You only need to run the future [`Prepare_data.py`](Prepare_data.py), or use the following command to preprocess the files.

```bash
python Prepare_data.py
```


## ***Train***

Once you have completed the data preparation, you can use the future [`train.py`](train.py) file to train your own model.

>**N.B.** The training code is being organized and will be released step by step.
```bash
python train.py
```


## ***Validation***

After completing the training, you can run the future [`evaluate.py`](evaluate.py) file to evaluate the model.

UltraGS is evaluated with PSNR, SSIM, MSE, and inference speed. In our experiments, UltraGS achieves up to 29.55 PSNR, 0.89 SSIM, and 64.69 fps on a single GPU.

```bash
python evaluate.py
```


## ***Visualization***

To better demonstrate the reconstruction results, we will provide visualization tools for novel ultrasound view synthesis, qualitative comparison, and ablation visualization.

The visualization code and demo results will be updated with the project code.


## ***References***

1) [**3DGS**](https://github.com/graphdeco-inria/gaussian-splatting)
2) [**2DGS**](https://github.com/hbb1/2d-gaussian-splatting)


## ***Citation***

```bibtex
@article{yang2025ultrags,
  title={UltraGS: Gaussian Splatting for Ultrasound Novel View Synthesis},
  author={Yang, Yuezhe and Cai, Wenjie and Yang, Dexin and Dong, Yufang and Dong, Xingbo and Jin, Zhe},
  journal={arXiv preprint arXiv:2511.07743},
  year={2025}
}
```
