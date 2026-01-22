from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('merak/', views.merak, name='merak'),
    path('learning-journey/', views.learning_journey, name='learning_journey'),
]
