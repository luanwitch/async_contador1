from django.contrib import admin
from django.urls import path
from contador_async_final import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("contador/", views.contador, name="contador"),
    path("", views.home, name="home"), 
]
