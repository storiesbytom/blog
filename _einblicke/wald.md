---
title: "Wald"
layout: single
classes: wide

# 1. Hero-Header mit Button zum Anker-Link
header:
  overlay_image: /assets/images/wald-hero.jpg
  overlay_filter: 0.5
  actions:
    - label: "Zur Galerie springen"
      url: "#galerie"

# 2. Bilder-Definition für die Galerie
gallery:
  - image_path: /assets/images/wald-1.jpg
    url: /assets/images/wald-1.jpg
    alt: "Morgennebel"
    title: "Morgennebel im Wald"
  - image_path: /assets/images/wald-2.jpg
    alt: "Sonnenlicht"
    title: "Lichtspiel im Blätterdach"
  - image_path: /assets/images/wald-3.jpg
    alt: "Moospfad"
    title: "Ruhiger Pfad im Moos"
---

## Schönheit der Stille

Der Wald bietet unzählige Perspektiven und eine Ruhe, die man kaum woanders findet.

<!-- 3. Hier setzen wir die ID für den Sprungmarken-Link -->

{: #galerie}

### Galerie

<!-- 4. Hier wird die oben definierte Galerie gerendert -->

{% include gallery layout="half" %}
