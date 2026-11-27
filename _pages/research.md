---
layout: page
permalink: /research/
title: Research
description:
nav: true
nav_order: 1
_styles: >
  .research-figure { margin: 1.5rem 0; }
  .research-figure img { display: block; width: 100%; height: auto; background: #fff; padding: 0.75rem; border-radius: 6px; }
  .research-figure figcaption { font-size: 0.85rem; color: var(--global-text-color-light); margin-top: 0.5rem; }
---

<!-- Each section: an optional figure, a short paragraph, then key papers.
     To add a figure, put it in assets/img/ and copy the <figure class="research-figure"> block below. -->

## Neural field-level BAO reconstruction with DESI

<figure class="research-figure">
<img src="/assets/img/lift_inference_scheme.png" alt="Diagram of LiFT inference: input fields are cropped to subgrids, passed through LiFT, and the predicted subgrids are assembled into the full reconstructed field.">
<figcaption>LiFT at inference: the input fields are cropped to subgrids, LiFT predicts each subgrid, and the predictions are tiled into the full reconstructed field. From <a href="https://arxiv.org/abs/2609.14862">Parker et al. 2026</a>.</figcaption>
</figure>

To constrain dark energy, DESI charts the Universe's expansion history with a standard ruler: baryon acoustic oscillations (BAO), sound waves from the early Universe that left a preferred separation between galaxies. Billions of years of non-linear gravitational evolution have blurred this ruler. Surveys sharpen it by partially reversing the gravitational displacements, but standard reconstruction treats gravity and galaxy bias as linear, and its error analysis is exact only for a Gaussian field, so it has to be calibrated with mock simulations and empirical corrections. My thesis develops the Linear Field Transformer (LiFT), a neural network that performs non-linear BAO reconstruction on real survey data without these assumptions and significantly increases the information recovered from the same galaxies.

Key papers: [Parker et al. 2026](https://arxiv.org/abs/2609.14862), [Parker, Bayer & Seljak 2025](https://arxiv.org/abs/2504.01092), [Bayer, Parker et al. 2026](https://arxiv.org/abs/2603.15732)

<div style="clear: both;"></div>

## Lightcone Research

*Description to come.*

Code: [ASTRA](https://github.com/LightconeResearch/astra-spec), [Lightcone-CLI](https://github.com/LightconeResearch/lightcone-cli)

<div style="clear: both;"></div>

## Foundation models for astronomy

*Description to come.*

Key papers: [Parker, Lanusse, Shen et al. 2025](https://arxiv.org/abs/2510.17960), [Multimodal Universe Collaboration 2024](https://arxiv.org/abs/2412.02527), [Parker et al. 2024](https://arxiv.org/abs/2310.03024)

<div style="clear: both;"></div>

## Simulation-based inference of galaxy clustering

*Description to come.*

Key papers: [Lemos, Parker et al. 2024](https://arxiv.org/abs/2310.15256), [Hahn, Lemos, Parker et al. 2024](https://arxiv.org/abs/2310.15246)

<div style="clear: both;"></div>
