from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# import reverse_lazy for Class Based Views
from django.urls import reverse_lazy

from .forms import RegistrationForm, AddressForm
from .models import Address


class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully')
            form.save()
            return redirect('login')
        return render(request, 'account/register.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    address = user.addresses.first()
    context = {
        'user': user,
        'address': address,
        'orders': user.orders.all(),
    }
    return render(request, 'account/profile.html', context)


class AddressCreateView(CreateView):
    model = Address
    form_class = AddressForm
    template_name = 'account/add_address.html'
    success_url = reverse_lazy('account:profile')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)