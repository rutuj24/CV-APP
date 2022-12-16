from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    path('resume/', views.home, name="home"),
    path('',views.info,name="info"),
    path('pdf', views.pdf_resume, name = 'create_pdf'),
    path('analyze', views.analyzer, name = 'analyze'),
    path('result', views.analysis, name = 'res')
]