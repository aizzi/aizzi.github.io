---
---
# Tutorials test 29

{% for tutorial in site.tutorials %}
  <p><a href="{{ tutorial.url }}">{{ tutorial.title }}</a></p>
  <p>{{ tutorial.description }}</p>
  <p>{{ tutorial.last_update }}</p>
  <p></p>
{% endfor %}
