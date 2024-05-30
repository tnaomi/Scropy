from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('crops', views.get_crops),
] 