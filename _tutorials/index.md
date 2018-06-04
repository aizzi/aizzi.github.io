---
title: "Tutorials"
---
# Tutorials test 14

<p>type: {{ page.collection }}</p>
{% for tutorial in site.tutorials %}
  <p>{{ tutorial.url }}</p>
{% endfor %}
