---
layout: page
permalink: /research/
title: Research
description:
nav: true
nav_order: 1
_styles: >
  article h2 { margin-top: 3rem; }
  article h2:first-child { margin-top: 0.5rem; }
  .research-figure { float: right; width: 400px; max-width: 48%; margin: 0.35rem 0 1rem 1.75rem; }
  .research-figure img { display: block; width: 100%; height: auto; background: #fff; padding: 0.6rem; border-radius: 4px; box-shadow: 0 2px 6px rgba(0,0,0,0.15); }
  @media (max-width: 700px) { .research-figure { float: none; width: 100%; max-width: 100%; margin: 1rem 0; } }
---

<!-- Each section: an optional figure, a short paragraph, then key papers.
     To add a figure, put it in assets/img/ and copy the <figure class="research-figure"> block below;
     it floats to the right of the text, as on Oliver's page. -->

## Neural field-level BAO reconstruction with DESI

<figure class="research-figure">
<img src="/assets/img/lift_inference_scheme.png" alt="Diagram of LiFT inference: input fields are cropped to subgrids, passed through LiFT, and the predicted subgrids are assembled into the full reconstructed field.">
</figure>

To constrain dark energy, DESI charts the Universe's expansion history with a standard ruler: baryon acoustic oscillations (BAO), sound waves from the early Universe that left a preferred separation between galaxies. Billions of years of non-linear gravitational evolution have blurred this ruler. Surveys sharpen it by partially reversing the gravitational displacements, but standard reconstruction treats gravity and galaxy bias as linear, and its error analysis is exact only for a Gaussian field, so it has to be calibrated with mock simulations and empirical corrections. My thesis develops the Linear Field Transformer (LiFT), a neural network that performs non-linear BAO reconstruction on real survey data without these assumptions and significantly increases the information recovered from the same galaxies.

Key papers: [Parker et al. 2026](https://arxiv.org/abs/2609.14862), [Parker, Bayer & Seljak 2025](https://arxiv.org/abs/2504.01092), [Bayer, Parker et al. 2026](https://arxiv.org/abs/2603.15732)

<div style="clear: both;"></div>

## Lightcone Research

*Description to come.*

Code: [ASTRA](https://github.com/LightconeResearch/astra-spec), [Lightcone-CLI](https://github.com/LightconeResearch/lightcone-cli)

<div style="clear: both;"></div>

## Foundation models for astronomy

<figure class="research-figure">
<img src="/assets/img/aion_overview.png" alt="Overview of the AION model: images, spectra, segmentation maps and physical parameters are tokenized, passed through a transformer encoder and decoder, and the resulting embeddings are used for downstream tasks such as regression, segmentation and retrieval.">
</figure>

Modern surveys observe the same objects in many ways: images, spectra, photometry, time series. Most analysis is still built one instrument and one task at a time. With collaborators, I have developed methods that combine observations from different surveys in a single model, and pretrained models of up to 7 billion parameters whose learned representations can be reused across tasks with little or no labeled data. Alongside this, we built open data infrastructure, now more than 100 TB, that makes the data from these surveys machine-learning ready.

Key papers: [Parker, Lanusse, Shen et al. 2025](https://arxiv.org/abs/2510.17960), [Multimodal Universe Collaboration 2024](https://arxiv.org/abs/2412.02527), [Parker et al. 2024](https://arxiv.org/abs/2310.03024), [Koblischke, Parker et al. 2026](https://arxiv.org/abs/2512.11982)

<div style="clear: both;"></div>

## Simulation-based inference of galaxy clustering

<figure class="research-figure">
<img src="/assets/img/simbig_cnn_posterior.png" alt="Corner plot of posterior constraints on five cosmological parameters from BOSS galaxies, comparing a field-level convolutional neural network analysis with power spectrum analyses; an inset enlarges the matter density and clustering amplitude panel, where the neural network contours are tighter.">
</figure>

Standard analyses compress a galaxy survey into its two-point statistics, which miss the information on small scales and in the non-Gaussian structure of the map. Simulation-based inference instead trains neural networks on simulated galaxy catalogs that include the survey's geometry and observational effects. With collaborators, I applied this to BOSS galaxies at the field level, and the resulting constraint on σ8 is 2.65 times tighter than a standard power spectrum analysis.

Key papers: [Lemos, Parker et al. 2024](https://arxiv.org/abs/2310.15256), [Hahn, Lemos, Parker et al. 2024](https://arxiv.org/abs/2310.15246)

<div style="clear: both;"></div>
