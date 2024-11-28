from django.urls import path
from . import views as blog_Views
from django.contrib.auth import views as auth_Views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', blog_Views.Home.as_view(), name="home"),
    path('reg', blog_Views.reg, name="reg"),
    path('auth', auth_Views.LoginView.as_view(
        template_name="blog/auth.html"), name="auth"),
    path('exit', auth_Views.LogoutView.as_view(
        template_name="blog/exit.html"), name="exit"),
    path('news/<int:pk>', blog_Views.NewsDetail.as_view(), name='news_id'),
    path('profile', blog_Views.profile, name="profile"),
    path('add', blog_Views.CreateNew.as_view(), name="add"),
    path('news/<int:pk>/update', blog_Views.UpdateNew.as_view(), name="update"),
    path('news/<int:pk>/delete', blog_Views.DeleteNew.as_view(), name="delete"),
    path('about', blog_Views.about, name="about"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
