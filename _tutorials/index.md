---
---
# Tutorials test 26

<p>collection: {{ page.collection }}</p>
<p>type: {{ page.type }}</p>
{% for tutorial in site.tutorials %}
  <p>{{ tutorial.url }}</p>
{% endfor %}
