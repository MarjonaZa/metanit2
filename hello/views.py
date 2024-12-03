from django.http import  HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

from django.shortcuts import render
def index(request):
    return render(request, "index.html")




# def set(request):
#     username = request.GET.get("username", "Undefined")
#     response = HttpResponse(f" hello {username}")
#     response.set_cookie("username", username)
#
#     response.set_cookie("username", username)
#     return response
#
# def get(request):
#     username = request.COOKIES['username']
#     return HttpResponse(f"helllo {username}")

#5
# def index(request):
#     bob = Person("Bob", 44)
#     return JsonResponse(bob, safe=False, encoder=PersonEncoder)
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class PersonEncoder(DjangoJSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Person):
#             return {"name": obj.name, "agr": obj.age}
#         return super().default(obj)



#4
# def index(request):
#     return JsonResponse({"name": "Tom", "age": 36})

# Create your views here.


# 3
# def indexcccx(request, id):
#     ludi = ["tom", "jeri", "liaza"]
#     if id in range(0, len(ludi)):
#         return HttpResponse(ludi[id])
#     else:
#         return HttpResponseNotFound("Not Found")
#
# def age(request, age):
#     if age not in range(1, 111):
#         return  HttpResponseBadRequest("некоорекстные данные")
#     if(age > 17):
#         return  HttpResponse("Доступ резрешён")
#     else:
#         return HttpResponseForbidden("Доступ заблокирован: недостаточно лет")




#2
# def index(request):
#     return  HttpResponse('dfgjfgn наш index')

# def about(request):
#     return HttpResponse('топтоап наш эбаут')

# def contact(request):
#     return HttpResponseRedirect("/about")
#
# def details(request):
#     return HttpResponsePermanentRedirect("/")


#1
# def user(request, name = "Undefined", age = 0):
#
#     #В данном случае, если для параметра name не передается значение,
#     # то он получает в качестве значения строку "Undefined". Для параметра age значение по умолчанию 0.
#     return HttpResponse(f"<h2>name:{name} age={age} </h2>")
#
# def about(request, name, age):
#     return HttpResponse(f"about user: name: {name}, age: {age}")
#
# def contact(request):
#     return HttpResponse("контакты")


#{ op


def index(request):
    host = request.META['HTTP_HOST'], # получаем адрес сайта
    user_agent = request.META['HTTP_USER_AGENT'] # получаем данные браузере
    path = request.path # получаем запрошенной путь

    # return HttpResponse(f"""
    #        <p>Host: {host}</p>
    #        <p>Path: {path}</p>
    #        <p>User-agent: {user_agent}</p>
    #    """)

    #return HttpResponse("главная")
#}opo




# request - объект  HttpRequest, котрый хранит инфу о запросе, в данном случае не нужен преметр поэтому он не юзается



# def user(request):
#     age = request.GET.get("age", 0)
#     name = request.GET.get("name", "Undefined")
#     return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")
# Для получения параметров из строки запроса применяется метод request.GET.get(), в которую передается название параметра.