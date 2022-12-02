from django.urls import path,re_path
from . import views
 

app_name= 'hello'
urlpatterns=[
    # #普通匹配
 
     path('list/',views.listView,name="listView"),
     path('test/',views.test,name="test"),
     path('login/',views.loginView,name="login"),
     re_path('hello/',views.index,name="index"),
     path('index/',views.indexView,name='indexView')
    # #位置参数匹配
    # re_path('hello/([0-9]{4})/([0-9]{2})/',views.index,name='index'),
    #关键字匹配
    #re_path('hello/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/',views.index,name='index')
 ]