from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Min
from django.http import JsonResponse
from django import forms
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Consultation, Lawyer, Review, Variation
from .forms import VariationForm

from order.models import Cart

def home(request):
    return render(request, 'index.html')


class ConsultationListView(ListView, LoginRequiredMixin):
    model = Consultation
    template_name = 'consultation/consultation_list.html'
    context_object_name = 'consultations'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ConsultationListView, self).get_context_data(**kwargs)
        context['lawyers'] = Lawyer.objects.filter(verified=True)
        return context

    def get_queryset(self):
        queryset = super(ConsultationListView, self).get_queryset()
        queryset = queryset.prefetch_related('variations')
        queryset = queryset.select_related('lawyer')
        queryset = queryset.annotate(lowest_price=Min('variations__price'))
        return queryset


class ConsultationDetailView(DetailView):
    model = Consultation
    template_name = 'consultation/consultation_detail.html'
    context_object_name = 'consultation'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        consultation = context['consultation']

        # Mendapatkan semua variasi yang terkait dengan konsultasi
        variations = Variation.objects.filter(consultation=consultation)

        # Mengelompokkan variasi berdasarkan tipe
        type_choices = set(variation.type for variation in variations)

        # Menyusun opsi variasi berdasarkan tipe
        options = {}
        for choice in type_choices:
            durations = variations.filter(type=choice).values_list('duration', flat=True).distinct()
            options[choice] = list(durations)

        context['options'] = options
        return context


@csrf_exempt
def get_variation_price(request):
    if request.method == 'POST':
        variation_type = request.POST.get('type')
        variation_duration = request.POST.get('duration')

        variations = Variation.objects.filter(type=variation_type, duration=variation_duration)
        if variations.exists():
            variation = variations.first()
            return JsonResponse({'price': variation.price})


class BookConsultationView(View):
    def post(self, request, pk):
        consultation = Consultation.objects.get(id=pk)
        variation_type = request.POST.get('type')
        variation_duration = request.POST.get('duration')
        print(variation_type, variation_duration)

        try:
            # get or create cart
            cart, created = Cart.objects.get_or_create(
                user=request.user,
                consultation=consultation,
                variation_type=variation_type,
                variation_duration=variation_duration,
            )

            if created:
                cart.save()
            else:
                messages.info(request, 'Item already exists in your cart')

            return redirect('order:cart')
        except:
            print('error')
            return redirect('consultation:consultation-detail', pk=pk)