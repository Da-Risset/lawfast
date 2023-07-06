from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm

from .views import (
    RegistrationView,
)


app_name = 'account'

urlpatterns = [
    path('register/', RegistrationView.as_view(), name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html', authentication_form=LoginForm), name="login"),
]