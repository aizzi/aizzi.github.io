---
type: tutorials
---
# Tutorials test 15

<p>type: {{ page.collection }}</p>
{% for tutorial in site.tutorials %}
  <p>{{ tutorial.url }}</p>
{% endfor %}
