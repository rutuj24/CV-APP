from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('builder/', include('resumesite.urls')),
    path('', views.index, name="index"),
    path('screen/', views.screen, name="screen"),
    path('screen/screen_r', views.screen_result, name="screen_r"),
]
