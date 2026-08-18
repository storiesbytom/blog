---
title: "Notizen"
permalink: /notizen/
layout: single
classes: wide
author_profile: true
---

{% assign postsByYear = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}

<!-- Jahres-Filter Pills -->
<ul class="taxonomy__index">
  {% for yearGroup in postsByYear %}
    <li>
      <a href="#year-{{ yearGroup.name }}">
        <strong>{{ yearGroup.name }}</strong> <span class="taxonomy__count">{{ yearGroup.items | size }}</span>
      </a>
    </li>
  {% endfor %}
</ul>

<!-- Beiträge nach Jahren -->

{% for yearGroup in postsByYear %}

  <section id="year-{{ yearGroup.name }}" class="taxonomy__section">
    <h2 class="archive__subtitle">{{ yearGroup.name }}</h2>

    <div class="archive-list">
      {% for post in yearGroup.items %}
        <article class="archive-item-custom">

          {% if post.header.teaser %}
            <div class="archive-item-teaser">
              <a href="{{ post.url | relative_url }}">
                <img src="{{ post.header.teaser | relative_url }}" alt="{{ post.title | escape }}" loading="lazy">
              </a>
            </div>
          {% endif %}

          <div class="archive-item-content">
            <h3 class="archive-item-title">
              <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
            </h3>

            <div class="archive-item-meta">
              <i class="far fa-clock" aria-hidden="true"></i> {{ post.date | date: "%d.%m.%Y" }}
            </div>

            {% if post.excerpt %}
              <p class="archive-item-excerpt">
                {{ post.excerpt | strip_html | truncate: 150 }}
              </p>
            {% endif %}
          </div>

        </article>
      {% endfor %}
    </div>

  </section>
{% endfor %}
