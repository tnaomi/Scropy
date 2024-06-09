from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.index, name="home"),
    path('crops', views.get_crops, name="crops"),
    path('crops/crop/<int:id>', views.get_crop_by_id, name="single"),
    path('zone/<int:id>', views.get_zone_by_id, name='single_zone'),
    path('about', views.about, name="about"),
] 