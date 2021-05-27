from django.urls import path
from django.urls.resolvers import URLPattern
from tablero import views

urlpatterns=[
    path('/', views.inicio)
]