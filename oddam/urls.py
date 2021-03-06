from django.urls import path
from oddam import views as oddam_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", oddam_views.LandingPage.as_view(), name="landing_page"),
    path("przekaz/", oddam_views.AddDonation.as_view(), name="add_donation"),
    path("login/", oddam_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view() , name="logout"),
    path("register/", oddam_views.RegisterView.as_view(), name="register"),
    path("profil/", oddam_views.ProfileDetailView.as_view(), name="profile"),
    path("ajax/", oddam_views.AjaxView.as_view(), name="ajax")
    # path('rest/get_institutions/', oddam_views.get_institution_list),

]