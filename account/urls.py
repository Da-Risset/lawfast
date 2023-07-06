from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm

from . import views


app_name = 'account'

urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html', authentication_form=LoginForm), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='account:login'), name="logout"),
    path('profile/', views.profile, name="profile"),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'), name="password-reset"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'), name="password_reset_confirm"),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name="password_reset_complete"),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='account/password_change.html'), name="password-change"),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), name="password_change_done"),
]