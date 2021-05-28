from django.contrib import admin
from django.urls import path, include
from tablero import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('/', views.inicio,name='tablero.inicio'), 
  path('accounts/', include('django.contrib.auth.urls')), 
]