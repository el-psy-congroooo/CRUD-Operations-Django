from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.home, name='home'),
    path('create/', views.create, name='create'),
    path('create/<int:id>', views.create, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('signup/', views.signup, name='signup'),
]
