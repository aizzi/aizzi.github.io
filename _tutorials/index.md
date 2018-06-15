---
---
# Tutorials

<!---
Sort the tutorials in reverse order by last_update variable, so that last updated will be on-top of the page
-->
{% assign tutorials_list = site.tutorials | sort:"last_update" | reverse %}

<!--
Iterate through the list of tutorials, and build the index
-->
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
