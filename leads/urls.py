from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('export-leads/', views.export_leads_csv, name='export_leads_csv'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('export-leads/', views.export_leads_csv, name='export_leads_csv'), # এই লিঙ্কে গেলে CSV ডাউনলোড হবে
]