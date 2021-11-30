from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    #path('register/', views.register, name="users-register"),
    #path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="users-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/testing.html'), name="users-logout"),
    path('profile/', views.profile, name="users-profile"),

    # PASSWORD RESET
    # path("password-reset/", 
    #     auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"), 
    #     name="password-reset"),

    # path("password-reset/done/", 
    #     auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), 
    #     name="password_reset_done"),

    # path("password-reset-confirm/<uidb64>/<token>/", 
    #     auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), 
    #     name="password_reset_confirm"),
 
    # path("password-reset-complete/", 
    #     auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), 
    #     name="password_reset_complete"),
]