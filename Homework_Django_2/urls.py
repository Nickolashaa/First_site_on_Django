from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls")),
    path('pass-reset', auth_Views.PasswordResetView.as_view(
        template_name="blog/pass-reset.html"), name="pass-reset"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_Views.PasswordResetConfirmView.as_view(
        template_name="blog/password_reset_confirm.html"), name="password_reset_confirm"),
    path('password_reset_done', auth_Views.PasswordResetDoneView.as_view(
        template_name="blog/pass-reset-done.html"), name="password_reset_done"),
    path('pass-reset-complete', auth_Views.PasswordResetCompleteView.as_view(
        template_name="pass-reset-complete.html"), name="pass-reset-complete"),
]
