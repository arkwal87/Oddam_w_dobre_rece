from django.shortcuts import render, redirect
from django.views import View
from django.core.paginator import Paginator
from django.contrib import messages

from .models import Donation, Institution
from .forms import UserRegistrationForm

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
            item_list = Institution.objects.filter(type=item.first().type)
            paginator = Paginator(item_list, 2)
            page = request.GET.get('page')
            print(page)
            new_item = paginator.get_page(page)
            items[items.index(item)] = new_item
            print(new_item)

        context = ({
            "bag_count": self.count_bags,
            "institution_count": len(Donation.objects.values("institution").distinct()),
            "items": items
        })
        return render(request, "index.html", context=context)


class AddDonation(View):
    def get(self, request):
        return render(request, "form.html")


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")


# class RegisterView(View):
#     def get(self, request):
#         return render(request, "register.html")


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