---
---
# Tutorials test 30

{% for tutorial in site.tutorials %}
  <div><a href="{{ tutorial.url }}">{{ tutorial.title }}</a></div>
  <div>>{{ tutorial.description }}</div>
  <div>Last updated: {{ tutorial.last_update }}</div>
  <p></p>
{% endfor %}
