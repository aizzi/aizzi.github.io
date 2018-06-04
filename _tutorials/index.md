---
type: "tutorials"
layout: "default"
---
# Tutorials test 18

<p>collection: {{ page.collection }}</p>
<p>type: {{ page.type }}</p>
{% for tutorial in site.tutorials %}
  <p>{{ tutorial.url }}</p>
{% endfor %}
