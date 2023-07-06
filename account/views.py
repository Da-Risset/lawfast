from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm


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
    context = {
        'user': user,
    }
    return render(request, 'account/profile.html', context)