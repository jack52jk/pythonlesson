from django.urls import path,re_path
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

   #用户管理的遍历界面 add
   path("add/",views.AddView.as_view(),name='add'),
   path("addsave/",views.AddSaveView.as_view(),name='addSaveView'),

      #用户管理 用户 得详细信息 view
   re_path("detailView/",views.UserView.getView,name='detailView'),
 
      #用户管理 用户 得修改信息 view
   re_path("editView/",views.UserView.editView,name='editView'),
   re_path("editSaveView/",views.UserView.editSaveView,name='editSaveView'),

   #用户管理 用户 得删除信息
   re_path("deletebyidView/",views.UserView.deleteById,name='deletebyidView'),


]

