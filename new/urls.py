from django.urls import path
from . import views

app_name = 'new'
urlpatterns = [
    path('signup/',  views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('log/', views.log, name='log'),
    path('create/', views.create, name="create"),
    path('<int:id>/', views.show, name="show"),
    path('home/', views.home, name="home"),
    path('show/', views.show, name="show"),

]