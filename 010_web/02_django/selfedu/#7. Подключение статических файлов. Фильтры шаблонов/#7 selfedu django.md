### #7. Подключение статических файлов. Фильтры шаблонов

[Django для python (уроки)](https://www.youtube.com/watch?v=FyTL1bnUx5I&list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F)


[youtube](https://www.youtube.com/watch?v=IrUG07namQ8&list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F&index=8)

[proproprogs.ru](https://proproprogs.ru/django/podklyuchenie-staticheskih-faylov-filtry-shablonov)

[github](https://github.com/selfedu-rus/django-lessons)

[Bootstrap](https://getbootstrap.com​)
[Фильтры шаблонов](https://djbook.ru/rel3.0/ref/templates/builtins.html#ref-templates-builtins-filters)


- STATIC_URL – префикс URL-адреса для статических файлов;
- STATIC_ROOT – путь к общей статической папке, используемой реальным веб-сервером;
- STATICFILES_DIRS – список дополнительных (нестандартных) путей к статическим файлам, используемых для сбора и для режима отладки.

coolsite/settings.py

~~~ python
STATIC_URL = '/static/'  # URL статических файлов
STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # путь к папке статических хайлов всего проекта
STATICFILES_DIRS = []  # нестандартные пути статических файлов
~~~

в приложении women создаем новую деректорию для статических файлов static в ней подкаталог приложения (от конфликта имен) с вложенными папками css js images

в файле шаблона html
добавляем тэг загрузки статических файлов
~~~ html
{% load static %}
~~~
подключаем файл оформления

~~~ html
<!-- подключаем файл оформления путь к файлу стилей относительно папки static -->
<link type="text/css" href="{% static 'women/css/styles.css' %}" rel="stylesheet" />
~~~
