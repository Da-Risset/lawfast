from django.urls import path
# import TemplateView
from django.views.generic import TemplateView

from . import views

app_name = 'consultation'


urlpatterns = [
    path('', views.home, name='home'),
    path('consultation/', views.ConsultationListView.as_view(), name='consultation-list'),
    path('consultation/<int:pk>/', views.ConsultationDetailView.as_view(), name='consultation-detail'),
    path('get_variation_price/', views.get_variation_price, name='get-variation-price'),
    path('consultation/<int:pk>/book/', views.BookConsultationView.as_view(), name='book-consultation'),
]