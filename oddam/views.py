from django.shortcuts import render
from django.views import View

# Create your views here.


class LandingPage(View):
    def get(self, request):
        return render(request, "index.html")

class AddDonation(View):
    def get(self, request):
        return render(request, "form.html")


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")


class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")