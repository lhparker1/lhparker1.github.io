---
layout: page
permalink: /outside/
title: Outside physics
description:
nav: true
nav_order: 6
_styles: >
  article h2 { margin-top: 2rem; }
  article h2:first-child { margin-top: 0.5rem; }
  .outside-photo { margin: 1rem 0 2rem; }
  .outside-photo img { display: block; width: 100%; height: auto; border-radius: 4px; box-shadow: 0 2px 6px rgba(0,0,0,0.15); }
  .outside-photo figcaption { margin-top: 0.5rem; font-size: 0.85rem; color: var(--global-text-color-light); }
  .outside-row { display: flex; gap: 1.25rem; align-items: flex-start; margin: 1rem 0 2rem; }
  .outside-row .outside-photo { flex: var(--ar) 1 0; min-width: 0; margin: 0; }
  @media (max-width: 700px) { .outside-row { display: block; } .outside-row .outside-photo { margin: 0 0 1.5rem; } }
---

{% comment %}
  To add a photo: put the file in assets/img/outside/ and copy a figure block.
  A figure on its own spans the full width. Figures inside a div with class
  "outside-row" share one row at equal height: set --ar on each to its width
  divided by its height (1.333 for a 4:3 landscape photo, 0.75 for a 3:4
  portrait one, 0.667 for 2:3). One landscape plus one portrait fills a row well.
{% endcomment %}

I like to spend time outdoors, in particular anywhere on a mountain. I have also been learning guitar, although it's a long process. I used to compete in Olympic-style weightlifting, including at the USA National Championships in 2024 and 2025.

## Mountaineering

<div class="outside-row">
  <figure class="outside-photo" style="--ar: 1.333">
    <img src="/assets/img/outside/entreves.jpg" alt="A climber standing on the narrow rock ridge of the Aiguilles d'Entrèves, with glaciers and the peaks of the Mont Blanc massif behind." loading="lazy">
    <figcaption>Traverse of the Aiguilles d'Entrèves (3,600 m), Mont Blanc massif.</figcaption>
  </figure>
  <figure class="outside-photo" style="--ar: 0.75">
    <img src="/assets/img/outside/kilimanjaro.jpg" alt="A climber in a blue down jacket beside the summit sign at Uhuru Peak on Kilimanjaro." loading="lazy">
    <figcaption>Uhuru Peak, Kilimanjaro (5,895 m).</figcaption>
  </figure>
</div>

<div class="outside-row">
  <figure class="outside-photo" style="--ar: 0.667">
    <img src="/assets/img/outside/cayambe.jpg" alt="Three roped climbers walking down a snow ridge, with a broad glaciated mountain on the horizon." loading="lazy">
    <figcaption>Descending from the summit of Cayambe (5,790 m), with Antisana in the background.</figcaption>
  </figure>
  <figure class="outside-photo" style="--ar: 1.333">
    <img src="/assets/img/outside/cotopaxi.jpg" alt="Two climbers on a snow summit above a sea of cloud, one raising an ice axe." loading="lazy">
    <figcaption>Summit of Cotopaxi (5,897 m).</figcaption>
  </figure>
</div>

<figure class="outside-photo">
  <img src="/assets/img/outside/cotopaxi_eruption.jpg" alt="A snow-capped volcano sending a long plume of ash across the horizon at sunrise, above shadowed highlands." loading="lazy">
  <figcaption>Cotopaxi erupts at sunrise, seen from the bergschrund on Cayambe.</figcaption>
</figure>

<div class="outside-row">
  <figure class="outside-photo" style="--ar: 1.302">
    <img src="/assets/img/outside/rainier.jpg" alt="A line of climbers with heavy packs walking up a snowfield below the glaciated upper slopes of Mount Rainier." loading="lazy">
    <figcaption>Moving up to Camp Muir, Mount Rainier (4,392 m).</figcaption>
  </figure>
  <figure class="outside-photo" style="--ar: 0.75">
    <img src="/assets/img/outside/shasta.jpg" alt="A climber with a large pack, helmet and coiled rope walking up a snow-covered valley toward Mount Shasta." loading="lazy">
    <figcaption>On the approach to the north ridge of Mount Shasta (4,322 m).</figcaption>
  </figure>
</div>
