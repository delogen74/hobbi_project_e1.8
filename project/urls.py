from django.contrib import admin
from django.urls import path, include
from abouts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('abouts/', include('abouts.urls')),
]
