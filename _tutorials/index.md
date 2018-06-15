---
---
# Tutorials test 65

<p>
  {% assign tutorials_list = site.tutorials | sort:"last_update" | reverse %}
</p>

{% for tutorial in tutorials_list %}
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
