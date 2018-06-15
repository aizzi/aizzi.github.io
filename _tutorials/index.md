---
---
# Tutorials test 32

{% for tutorial in site.tutorials %}
  <div><h2><a href="{{ tutorial.url }}">{{ tutorial.title }}</a></h2></div>
  <blockquote>
    <div>{{ tutorial.description }}</div>
    <div>Last updated: {{ tutorial.last_update }}</div>
  </blockquote>
{% endfor %}
