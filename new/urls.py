from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('list/', views.list, name='list'),
    path('create/', views.create, name="create"),
    path('<int:id>/', views.show, name="show"),

]