---
title: "Tutorials"
---
# Tutorials test 13

<p>type: {{ page.type }}</p>
{% for tutorial in site.tutorials %}
  <p>{{ tutorial.url }}</p>
{% endfor %}
