
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pdfform/', views.pdf_upload, name='pdf_upload'),
    path('pdf/', views.spdf, name='spdf'),
    path('pdf/<int:id>/',views.delete_document,name='delete_document'),
]