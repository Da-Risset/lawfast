from django.urls import path

from . import views


app_name = 'document'

urlpatterns = [
    path('documents/', views.TypeDocumentListView.as_view(), name="document-list"),
    path('lawyers-list/<int:id>/', views.DocumentListView.as_view(), name="lawyer-list"),
    path('lawyers/<int:pk>/', views.DocumentLawyerDetailView.as_view(), name="lawyer-detail"),
    path('lawyers/<int:pk>/book/', views.BookDocumentiew.as_view(), name="book-document"),
]