# UltraGS Release Checklist

This checklist keeps the public release aligned with the repository structure described in the README.

## Repository

- [ ] Add `requirements.txt` with pinned major dependencies.
- [ ] Add reproducible configuration files under `configs/`.
- [ ] Add dataset loaders under `datasets/`.
- [ ] Add UltraGS scene and rendering implementation.
- [ ] Add training, rendering, and evaluation entry points.
- [ ] Add demo assets that do not contain sensitive clinical information.

## Data

- [ ] Complete privacy review for clinical data.
- [ ] Publish anonymized dataset metadata.
- [ ] Document data download or access request procedure.
- [ ] Provide preprocessing scripts and expected folder structure.
- [ ] Include checksums for released files.

## Experiments

- [ ] Provide benchmark configs for clinical, phantom, and wild datasets.
- [ ] Add commands for reproducing PSNR, SSIM, MSE, and FPS results.
- [ ] Release trained checkpoints after compliance approval.
- [ ] Add visualization examples for rendered ultrasound views.

## Documentation

- [ ] Update README commands after code release.
- [ ] Add detailed dataset documentation.
- [ ] Add model checkpoint documentation.
- [ ] Add citation information for the final published version.
