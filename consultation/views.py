from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Consultation, Lawyer, Review
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin



def home(request):
    return render(request, 'index.html')


class ConsultationListView(ListView, LoginRequiredMixin):
    model = Consultation
    template_name = 'consultation/consultation_list.html'
    context_object_name = 'consultations'
    ordering = ['-date_posted']
    paginate_by = 5
    
    def get_queryset(self):
        # lawyers = Lawyer.objects.filter(verified=True)
        consultation = Consultation.objects.all()
        return consultation 