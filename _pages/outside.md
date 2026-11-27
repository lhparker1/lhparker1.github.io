---
layout: page
permalink: /outside/
title: Outside physics
description:
nav: true
nav_order: 6
_styles: >
  article h2 { margin-top: 3rem; }
  article h2:first-child { margin-top: 0.5rem; }
  .outside-photo { margin: 1rem 0 2rem; }
  .outside-photo img { display: block; width: 100%; height: auto; border-radius: 4px; box-shadow: 0 2px 6px rgba(0,0,0,0.15); }
  .outside-photo figcaption { margin-top: 0.5rem; font-size: 0.85rem; color: var(--global-text-color-light); }
  .outside-row { display: flex; gap: 1.25rem; align-items: flex-start; margin: 1rem 0 2rem; }
  .outside-row .outside-photo { flex: var(--ar) 1 0; min-width: 0; margin: 0; }
  @media (max-width: 700px) { .outside-row { display: block; } .outside-row .outside-photo { margin: 0 0 1.5rem; } }
---

<!--
  To add a photo: put the file in assets/img/outside/ and copy a <figure> block.
  A figure on its own spans the full width. Figures inside <div class="outside-row">
  share one row at equal height: set --ar on each to its width divided by its height
  (1.333 for a 4:3 landscape photo, 0.75 for a 3:4 portrait one).
-->

## Mountaineering

<div class="outside-row">
  <figure class="outside-photo" style="--ar: 1.333">
    <img src="/assets/img/outside/entreves.jpg" alt="A climber standing on the narrow rock ridge of the Aiguilles d'Entrèves, with glaciers and the peaks of the Mont Blanc massif behind." loading="lazy">
    <figcaption>Traverse of the Aiguilles d'Entrèves, Mont Blanc massif.</figcaption>
  </figure>
  <figure class="outside-photo" style="--ar: 0.75">
    <img src="/assets/img/outside/kilimanjaro.jpg" alt="A climber in a blue down jacket beside the summit sign at Uhuru Peak on Kilimanjaro." loading="lazy">
    <figcaption>Uhuru Peak, Kilimanjaro (5,895 m).</figcaption>
  </figure>
</div>
