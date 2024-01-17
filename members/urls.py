from django.urls import path
from . import views

urlpatterns = [
    path('',views.test, name='test'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('test/', views.test, name='test'),
]