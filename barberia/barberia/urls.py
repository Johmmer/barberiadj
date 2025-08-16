from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Home page
    path('citas/', include('citas.urls')),  # Include URLs from the citas app
    path('contacto/', views.contacto, name='contacto'),  # Contact page
]
