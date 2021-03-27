---
title: '#6 selfedu django'
created: '2021-03-14T12:50:21.752Z'
modified: '2021-03-14T15:00:05.028Z'
---

# #6 selfedu django

### #6. Шаблоны (templates). Начало | Django уроки

https://www.youtube.com/watch?v=v3JM4yUFdNo

https://proproprogs.ru/django/django-shablony-templates-nachalo

https://djbook.ru/rel3.0/topics/templates.html


### Шаблоны (templates).

women/views.py 

~~~python
# встроенный в Django шаблонизатор
from django.shortcuts import render

def index(request):  # класс запроса HttpRequest
    
    return render(request, '<путь к шаблону>') # women/templates/women/

~~~

создаем папку templates и подпапку women в папку приложения women

создаем там файд index.html
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Главная страница</title>
</head>
<body>
 
</body>
</html>
```


в women/urls.py добовляем в urlpatterns

~~~python
path('about/', about, name='about')
~~~

в файле women/views.py добавляем функцию about 

~~~python
def about(request):
    return render(request, 'women/about.html')
~~~

добавляем шаблон about.html в templates/women

~~~html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>О сайте</title>
</head>
<body>
<h1>О сайте</h1>
</body>
</html>
~~~


### Передача шаблонам параметров

```python
menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    return render(request, 'women/index.html', {'menu': menu, 'title': 'Главная страница'})
 
def about(request):
    return render(request, 'women/index.html', {'menu': menu, 'title': 'О сайте'})

```

в шаблонах перебрать в цикле его элементы 

```html
<ul>
{% for m in menu %}
<li>{{m}}</li>
{% endfor %}
</ul>
```


### Создание базового шаблона (наследование шаблонов)

создаем шаблон базовой страницы base.html в templates/women

```html
<!DOCTYPE html>
<html>
<head>
         <title>{{title}}</title>
</head>
<body>
{% block mainmenu %}
<ul>
         {% for m in menu %}
<li>{{m}}</li>
         {% endfor %}
</ul>
{% endblock mainmenu %}
 
{% block content %}
{% endblock %}
</body>
</html>
```

### Отображение списка статей

в модуле women/views.py импорт моделей

```python
from .models import *
```

функции представления index чтение записей из таблицы Women передача шаблону

```python
def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})
```





