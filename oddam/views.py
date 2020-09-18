from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import views as auth_views, get_user_model
from django.views.generic import CreateView, DetailView

from .models import Donation, Institution, Category
from accounts.models import User
from .forms import UserRegistrationForm, UserLoginForm, AjaxForm


# Create your views here.


class LandingPage(View):
    def count_bags(self):
        bag_count = 0
        for bag in Donation.objects.all():
            bag_count += bag.quantity
        return bag_count

    def get(self, request):
        items = [
            Institution.objects.filter(type="FUN"),
            Institution.objects.filter(type="ORG"),
            Institution.objects.filter(type="LOK")
        ]
        for item in items:
            if Institution.objects.filter(type=item.first()):
                item_list = Institution.objects.filter(type=item.first().type)
                paginator = Paginator(item_list, 3)
                page = request.GET.get('page')
                new_item = paginator.get_page(page)
                items[items.index(item)] = new_item

        context = ({
            "bag_count": self.count_bags,
            "institution_count": len(Donation.objects.values("institution").distinct()),
            "items": items
        })
        return render(request, "index.html", context=context)


class AddDonation(View):
    def get(self, request):
        context = {
            "category_list": Category.objects.all(),
            "institution_list": Institution.objects.all()
        }
        return render(request, "form.html", context=context)

    def post(self, request):
        print(request.POST)


class LoginView(auth_views.LoginView):
    form_class = UserLoginForm
    template_name = "login.html"

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            User = get_user_model()
            if User.objects.filter(email=form.cleaned_data['username']).exists():
                return self.form_invalid(form)
            return redirect("register")


class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, "register.html", context={"form": form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Stworzono użytkownika {username}")
            # return redirect("style_main_page")
            return redirect("login")
        return redirect("register")


class AjaxView(View):
    form_class = AjaxForm
    template_name = "ajax.html"

    def get(self, *args, **kwargs):
        form = self.form_class()
        donations = Donation.objects.all()
        return render(self.request, self.template_name, {"form": form, "donations": donations})

    def post(self, *args, **kwargs):
        if self.request.is_ajax():
            form = self.form_class(self.request.POST)
            import pdb; pdb.set_trace()
            if form.is_valid():
                print(form.data)
                form.save()
                return JsonResponse({}, status=200)
            return JsonResponse({}, status=400)
        return JsonResponse({}, status=400)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "profile_view.html"

    def get_object(self, **kwargs):
        # id_ = self.kwargs.get("pk")
        id_ = self.request.user.id
        return get_object_or_404(User, pk=id_)
