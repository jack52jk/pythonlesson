"""ops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include,re_path


from api.views import helloView,sumView,CommandView,LoginShowView,LoginView,LoginAuthView
from assets.views import CollectHostInfo,AssetViews,CmdbView,CmdbDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # #login
    path('api/login_auth/',LoginAuthView),
    path('api/login/',LoginShowView),
    path('api/auth/',LoginView),
    
   # path('api/', include('api.urls')),
    path('api/hello/',helloView),
    #api/sum/?args1=1&args2=2
    path('api/sum/',sumView),
    #api/command/?args=df
    path('api/command/',CommandView),
    re_path('api/v1/cmdb$',CmdbView.as_view(),name="cmdb_list"),
    re_path(r'^api/v1/cmdb/delete/(?P<pk>[0-9]+)/$',CmdbDeleteView),
    path('api/v1/cmdb/collect',CollectHostInfo.as_view()),
     
     #args的参数传递  位置参数即元组
    #re_path(r'assets/2019/',AssetViews),
    #re_path(r'^assets/([0-9]{4})/',AssetViews),
    #re_path(r'^assets/([0-9]{4})/([0-9]{2})/([0-9]+)/',AssetViews),

    #kwargs的参数传递  关键字参数即字典类型
    re_path(r'^assets/(?P<year>[0-9]{4})/$', AssetViews)
    

]
