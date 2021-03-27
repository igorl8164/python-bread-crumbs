### #8. Формирование URL-адресов в шаблонах

[Django для python (уроки)](https://www.youtube.com/watch?v=FyTL1bnUx5I&list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F)

[youtube](https://www.youtube.com/watch?v=IrUG07namQ8&list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F&index=9)

[proproprogs.ru](https://proproprogs.ru/django/formirovanie-url-adresov-v-shablonah)

[github](https://github.com/selfedu-rus/django-lessons)

[Русскоязычная документация по Django 3](https://djbook.ru/rel3.0/)

[шаблонизатору Jinja](https://www.youtube.com/watch?v=cFJqMXxVNsI&list=PLA0M1Bcd0w8wfmtElObQrBbZjY6XeA06U)

~~~

теги {% имя_тега %}
переменные {{ имя_переменной }}
фильтры {{value|имя_фильтра}}

~~~

тег ссылки на страницу
~~~
{% url '<URL-адрес или имя маргрута>' [параметры ссылки] %}
~~~

в шаблоне base.html строчку

~~~ html
<li class="logo"><a href="/"><div class="logo"></div></a></li>
~~~

меняем на

~~~ html
<li class="logo"><a href="{% url 'home' %}"><div class="logo"></div></a></li>
~~~

home - имя маршрута одной из функций в women/urls.py
~~~
path('', index, name='home'),
~~~

#### Формирование динамических URL-адресов

в файле women/urls.py добавим строчку в urlpatterns
~~~ python
path('post/<int:post_id>/', show_post, name='post'),
# http://127.0.0.1:8000/post/<идентификатор_поста>/
~~~

функцию представления show_post

~~~ python
def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")
~~~

в шаблоне index.html
~~~ html
<p class="link-read-post"><a href="{% url 'post' p.pk %}">Читать пост</a></p>
<!-- http://127.0.0.1:8000/post/5/
-->
~~~


#### Функция get_absolute_url()

MTV (Models, Templates, Views)  
get_absolute_url()

~~~ python
from django.urls import reverse
def get_absolute_url(self):
    return reverse('post', kwargs={'post_id': self.pk})
# path('post/<int:post_id>/', show_post, name='post')
#  функция reverse, которая строит текущий URL-адрес записи на основе имени маршрута post и словаря параметров kwargs

~~~

шаблоне index.html
~~~ html
<p class="link-read-post"><a href="{{ p.get_absolute_url }}">Читать пост</a></p>
~~~
