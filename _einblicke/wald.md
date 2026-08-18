---
title: "Wald"
permalink: /einblicke/wald/
layout: single
classes: wide

# Hero-Banner oben
header:
  teaser: /assets/images/wald/wald-hero.jpg
  overlay_image: /assets/images/wald/wald-hero.jpg
  overlay_filter: 0.5
  caption: "Foto: Tom Stelzer"
  actions:
    - label: "Zur Galerie"
      url: "/einblicke/wald/#galerie"

excerpt: "Lichtspiele zwischen Baumkronen, Stille und das besondere Mikroklima im dicht bewachsenen Forst."
---

## Licht und Schatten im Geäst

Die Waldfotografie fasziniert mich durch ihre ständige Veränderung. Zwischen dichtem Geäst bricht das Sonnenlicht oft spürbar in feinen Strahlen durch den Dunst – Momente der Stille, die auf analogem Film eine ganz eigene Tiefe entfalten.

### Galerie

{: #galerie}

<div class="custom-gallery">
  {% assign wald_files = site.static_files | where_exp: "file", "file.path contains '/assets/images/wald/'" %}
  {% for file in wald_files %}
    {% if file.extname == '.jpg' or file.extname == '.jpeg' or file.extname == '.JPG' %}
      {% unless file.path contains 'hero' %}
        <a href="{{ file.path | relative_url }}" class="custom-gallery-item">
          <img src="{{ file.path | relative_url }}" alt="Waldfotografie" loading="lazy">
        </a>
      {% endunless %}
    {% endif %}
  {% endfor %}
</div>
