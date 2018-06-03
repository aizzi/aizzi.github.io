---
---
# Tutorials test 10

<p>{{ page.type }}</p>
{% for tutorial in site.tutorials %}
  <p>{{ tutorial.url }}</p>
{% endfor %}
