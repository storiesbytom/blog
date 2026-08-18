---
title: "Landschaft"
permalink: /einblicke/landschaft/
layout: single
classes: wide

# Hero-Banner oben
header:
  teaser: /assets/images/landschaft/lanschaft-hero.jpg
  overlay_image: /assets/images/landschaft/landschaft-hero.jpg
  overlay_filter: 0.5
  caption: "Foto: Tom Stelzer"
  actions:
    - label: "Zur Galerie"
      url: "/einblicke/landschaft/#galerie"

excerpt: "Weite Horizontlinien, Stille und das Zusammenspiel der Elemente in unberührter Natur."
---

## Weite und Entschleunigung

Landschaftsfotografie bedeutet für mich vor allem Geduld. Das Wechselspiel aus Licht, Wetter und Jahreszeiten verwandelt vertraute Orte in einzigartige Momente. Es geht nicht darum, die Landschaft zu beherrschen, sondern sich ihrem Rhythmus anzupassen und die Stille einzufangen.

### Galerie

{: #galerie}

<div class="custom-gallery">
  {% assign landscape_files = site.static_files | where_exp: "file", "file.path contains '/assets/images/landschaft/'" %}
  {% for file in landscape_files %}
    {% if file.extname == '.jpg' or file.extname == '.jpeg' %}
      <a href="{{ file.path | relative_url }}" class="custom-gallery-item">
        <img src="{{ file.path | relative_url }}" alt="Landschaftsfotografie" loading="lazy">
      </a>
    {% endif %}
  {% endfor %}
</div>
{% include gallery layout="half" %}
