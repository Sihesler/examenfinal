from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^carrera_nueva$', views.carrera_nueva, name='carrera_nueva'),
]
