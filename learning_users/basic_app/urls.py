from django.urls import path
from . import views
app_name = "basic_app"
urlpatterns = [
  path('', views.index, name='index'),

  #path('login/',views.login, name='login'),
  path('register/',views.register, name='register'),
  path('logout/',views.user_logout,name='user_logout'),
  path('special/',views.special,name='special'),
  path('login/',views.user_login,name='user_login')

#
]
