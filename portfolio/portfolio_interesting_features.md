# Portfolio Interesting Features

## `Edit` Button is Only Available to the `owner` of the `Project`

`portfolio\templates\portfolio\project_detail.html`:
```html
{% block content %}
    {{ project.title }}
    {% if user == project.owner %}
        - <a href={% url 'portfolio:project-update' project.id %}>Edit</a>
    {% endif %}
    <hr>
    {{ project.description }}
{% endblock content %}
```

## Alternate Image for `Project` with No `image`

`portfolio\templates\portfolio\project_list.html`:
```html
<img
    class="card-img-top"
    {% if project.image %}
        src="{{ project.image.url }}"
    {% else %}
        src="{% static 'portfolio/images/placeholder.png' %}"
    {% endif %}
>
```