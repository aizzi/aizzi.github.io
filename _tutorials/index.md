---
title: "index"
description: ""
last_update: "June 15th, 2018"
---
# Tutorials test 37

{% for tutorial in site.tutorials %}
    <div><h2><a href="{{ tutorial.url }}">{{ tutorial.title }}</a></h2></div>
    <blockquote>
      <div>{{ tutorial.description }}</div>
      <div>
        <small>
          <i>Last updated: {{ tutorial.last_update }}</i>
        </small>
      </div>
    </blockquote>
{% endfor %}
