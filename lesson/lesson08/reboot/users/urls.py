from django.urls import path
#from users.views import View
from users import views

app_name='users'

urlpatterns = [
   path("",views.IndexView.as_view(),name='indexView'),
   # path("",views.loginView,name='loginView'),
   path("login/",views.LoginView.as_view(),name='loginView'),
   path("logout/",views.LogoutView.as_view(),name='logoutView'),
  
]