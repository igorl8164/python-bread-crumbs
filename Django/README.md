## Django

### MVC - Model Controller View

model.py  # модель создавать, получать, обновлять, удолять данные в таблицах баз данных
	class ClassName_1(models.Model):
		pass
		
	class ClassName_2(models.Model):
		pass
		
templates # представление шаблоны формирует внешний вид страници 
\app\tamplates\app
		index.html
		layout.html
		about.html
		
<h2> {{ title }} </h2>  # Переменные шаблона
		
{% <тег> %}  # теги шаблона

тег цикла
'''
{% for <переменная элемент списка> in <список> %}
<блок тела цикла>
[{% empty %}
<блок empty>]
{% endfor %}
<блок empty> 
'''

теги условных выражений
'''
{% if <условие 1> %}
<блок 1>
[{% elif <условие 2> %}
<блок 2>]
[<другие теги elif>]
[{% else %}
<блок else>]
{% endif %}
'''

views.py # контроллер логика отображения веб-страниц
HttpRequest — запрос
HttpResponse — ответ

		def meth01(request : HttpRequest) -> HttpResponse:
			return response
			
		def meth02(request : HttpRequest) -> HttpResponse:
			return response
			
передачи данных от контроллера к представлению
return render(
        request,
        'app/page1.html',
        {                                           
            'title': title,      # передача переменной title в шаблон веб-страницы
        })
		
urls.py  # роутер вызов метода контроллера URL адреса шаблона
	url(r'^contact$', app.views.meth02, name='meth02')
	url(r'^(?P<pk>\d+)/$', app.views.meth02, name='choice')
	
	
urls.py -> views.py -> [model.py] -> templates

manage.py  утилита различные действия над проектом

settings.py  настройки проекта
urls.py  ведения о привязке приложений к интернет-адресам
wsgi.py  публикации веб-сайта

### app
--__init__.py-- пакет приложений
--models.py-- код моделий приложений
--views.py-- код контроллеров приложений
--forms.py-- код форм проиложений
admin.py параметры административного приложения
test.py базовая структура модульных тестов
migrations скрипты обновления баз данных
templates файлы представления html
static статические файлы приложения


settings.py # настройка приожения

DATABASES словарь сведеней о БД Python

LANGUAGE_CODE язык сайта

TIME_ZONE временная зона

INSTALLED_APPS кортеж строк имена активные приложения

### Встроенные приложения

django.contrib.admin администротивный раздел
django.contrib.auth разгроничение досиупа
django.contrib.contenttypes автоматическая обработка моделий
django.contrib.sessions обработка сессий
django.contrib.messages подсистема сообщений
django.contrib.staticfiles обработка статических файлов
