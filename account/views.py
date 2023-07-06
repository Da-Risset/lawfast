from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View


class RegistrationView(View):
    def get(self, request):
        pass