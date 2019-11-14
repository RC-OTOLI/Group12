{% extends 'layout.html'  %}
{% block body %}
    <h1> Add Transaction</h1>
    <form action= "" method = "POST" novalidate>
        <p>
            {{form.description.label}} <br>
            {{form.description(size = 10)}}
        </p>
        <p>
            {{form.amount.label}}<br>
            {{form.amount}}
        </p>
    </form>

{% endblock %}
