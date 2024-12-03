"""
URL configuration for metanit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from hello import views

urlpatterns = [
    path("index", views.index),
]



# urlpatterns = [
#     path('', views.index),

    # path('get', views.get),
        # path('set', views.set),
    #3
    # path("index/<int:id>", views.index),
    # path("access/<int:age>", views.age),
    #2
    # path('', views.index),
    # path('about/', views.about),
    # path('contact/', views.contact),
    # path('details/', views.details)

#1
    # это для нелбязательных пареметров
    # path('user/', views.user),
    # path('user/<name>', views.user),
    # path('user/<str:name>/<int:age>', views.user),
    # path('about', views.about, kwargs={"name":"Vova", "age" : 122}),
# ]



# urlpatterns = [
#     #Когда запрос приходит к приложению, то система проверяет соответствие запроса маршрутам
#     # по мере их определения: вначале сравнивается первый маршрут, если он не подходит,
#     # то сравнивается второй и так далее. Поэтому более общие маршруты должны определяться в последнюю очередь,
#     # а более конкретные маршруты должны идти в начале. Например:
#
#     re_path(r'^about/contact', views.contact, name='about'),
#     re_path(r'^about', views.about, name='about') # прикол в http://127.0.0.1:8000/about/dfvgfbfg всё равное выведет эбоут
#     # path('about', views.about, name = 'about'), #1 версия
#     # path('contact', views.contact),
# ]
