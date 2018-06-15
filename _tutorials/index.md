---
---
# Tutorials test 44

{% for tutorial in site.tutorials %}
  {% if true %}
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
