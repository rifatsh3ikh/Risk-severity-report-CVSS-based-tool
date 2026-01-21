from django.urls import path
from .views import cvss_form, export_pdf

urlpatterns = [
    path('', cvss_form, name='cvss_form'),
    path('pdf/', export_pdf, name='export_pdf'),
]
