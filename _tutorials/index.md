---
---
# Tutorials test 54

<p>
  {{ site.tutorials.docs }}
</p>

{% for tutorial in site.tutorials %}
{% if tutorial.title != 'Index' %}
  <div>
    <h2>
      <a href="{{ tutorial.url }}">{{ tutorial.title }}</a>
    </h2>
  </div>
  <blockquote>
    <div>
      {{ tutorial.description }}
    </div>
    <div>
      <small>
        <i>Last updated: {{ tutorial.last_update }}</i>
      </small>
    </div>
  </blockquote>
{% endif %}
{% endfor %}
