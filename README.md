# UltraGS

This project was created by [***Yuezhe Yang***](https://bean-young.github.io) for the paper
"**UltraGS: Real-Time Physically-Decoupled Gaussian Splatting for Ultrasound Novel View Synthesis**"
([arXiv](https://arxiv.org/abs/2511.07743)).

> The paper has been accepted by ICME 2026. Code, dataset access instructions, and trained checkpoints will be released after the remaining privacy and compliance checks are completed.

## ***Abstract***

Ultrasound novel view synthesis is challenging because clinical scans are often acquired with a limited field of view, irregular probe motion, and tissue-dependent acoustic effects that are not modeled well by standard RGB rendering assumptions. UltraGS adapts Gaussian Splatting to sensorless ultrasound imaging by combining explicit Gaussian radiance fields with lightweight physics-inspired acoustic rendering.

The framework introduces depth-aware Gaussian primitives with learnable fields of view to improve geometric consistency during freehand probe motion. It also uses PD Rendering, a differentiable acoustic operator that combines low-order spherical harmonics with first-order wave effects for efficient tissue intensity synthesis. Experiments on three datasets show that UltraGS achieves strong reconstruction quality and real-time synthesis performance, reaching up to 29.55 PSNR, 0.89 SSIM, and 64.69 FPS on a single GPU.

## ***News***

- **2026.04**: UltraGS was accepted by ICME 2026.
- **2026.01**: The revised arXiv version was released.
- **2025.11**: The first arXiv version was released.

## ***Prepare Data***

UltraGS is evaluated on three ultrasound datasets, including a clinical ultrasound examination dataset collected under real scanning protocols. Because the clinical data may contain sensitive medical information, the public release will include only data that has completed privacy review and institutional approval.

The released data package will follow this structure:

```text
data/
  clinical/
    case_xxx/
      images/
      poses/
      masks/
      meta.json
  phantom/
  wild/
```

Each case is expected to contain ultrasound frames, calibrated or estimated probe poses, optional foreground masks, and metadata needed for reproducible training and evaluation.

## ***Set Up***

The training and rendering code will be released after final packaging. The expected environment is:

- Python 3.9+
- PyTorch with CUDA support
- NVIDIA GPU for training and real-time rendering
- Standard scientific Python packages for image processing and evaluation

After the code release, dependencies will be installed with:

```bash
pip install -r requirements.txt
```

## ***Code Structure***

The repository will be organized as follows:

```text
UltraGS/
  configs/              # Dataset and experiment configuration files
  data/                 # Local dataset root, ignored by git
  datasets/             # Dataset loaders and pose utilities
  gaussian_renderer/    # UltraGS rendering modules
  scene/                # Scene representation and Gaussian parameters
  scripts/              # Data preparation, training, and evaluation scripts
  utils/                # Metrics, image processing, and visualization tools
  train.py              # Training entry point
  render.py             # Novel view rendering entry point
  evaluate.py           # Quantitative evaluation entry point
```

## ***Train***

After the dataset and code are released, a typical training command will be:

```bash
python train.py --config configs/clinical.yaml
```

Detailed configuration files will be provided for each benchmark dataset.

## ***Validation***

Quantitative evaluation will report standard novel view synthesis metrics, including PSNR, SSIM, and MSE. The evaluation entry point will be:

```bash
python evaluate.py --config configs/clinical.yaml --checkpoint path/to/checkpoint.pth
```

## ***Visualization***

The released visualization tools will support:

- Rendering novel ultrasound views from trained UltraGS scenes
- Exporting side-by-side comparisons of ground truth and synthesized frames
- Visualizing depth-aware Gaussian primitives and learned field-of-view parameters

## ***Release Plan***

We are preparing a reproducible release in the following order:

1. Environment file and installation instructions
2. Data preprocessing and anonymization scripts
3. Core UltraGS training and rendering code
4. Evaluation scripts and benchmark configurations
5. Trained checkpoints and demo assets

## ***References***

1. [3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)
2. [arXiv:2511.07743](https://arxiv.org/abs/2511.07743)

## ***Citation***

If you find this project useful, please cite our paper. The proceedings BibTeX will be updated after the ICME 2026 record is available.

```bibtex
@article{yang2025ultrags,
  title={UltraGS: Real-Time Physically-Decoupled Gaussian Splatting for Ultrasound Novel View Synthesis},
  author={Yang, Yuezhe and Ruan, Qingqing and Cai, Wenjie and Dong, Yudang and Yang, Dexin and Dong, Xingbo and Jin, Zhe and Dai, Yong},
  journal={arXiv preprint arXiv:2511.07743},
  year={2025}
}
```

## ***Contact***

For questions about the paper, code release, or dataset access, please contact the authors through the project maintainer's homepage: [bean-young.github.io](https://bean-young.github.io).
