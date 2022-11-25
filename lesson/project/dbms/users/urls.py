from django.urls import path
from users import views


app_name='users'
urlpatterns = [
   # path('userlist/', views.UsersViews.listUserView,name='listUser'),
   
   #首页
   path("",views.IndexView.as_view(),name='indexView'),
   #登录页面 
   path("login/",views.LoginView.as_view(),name='LoginView'),
   #退出页面
   path("logout/",views.LogoutView.as_view(),name='logoutView'),
   
   #登录成功后的首页
   path("index/",views.Index.as_view(),name='index'),

   #用户管理的遍历界面 list
   path("list/",views.UserView.as_view(),name='list'),
]

