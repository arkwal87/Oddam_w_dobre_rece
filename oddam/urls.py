from django.urls import path
from oddam import views as oddam_views

urlpatterns = [
    path("", oddam_views.LandingPage.as_view(), name="landing_page"),
    path("przekaz/", oddam_views.AddDonation.as_view(), name="add_donation"),
    path("login/", oddam_views.LoginView.as_view(), name="login"),
    path("register/", oddam_views.RegisterView.as_view(), name="register")
]