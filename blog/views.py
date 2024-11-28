from typing import Any
from django.shortcuts import render, redirect
from .forms import RegForm, AboutForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UpdateForm, UpdateImage
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import News
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail

# Create your views here.

class Home(ListView):
    model = News
    template_name = "blog/index.html"
    context_object_name = "news"
    ordering = ['time']
    paginate_by = 1
    
    def get_context_data(self, **kwargs):
        ctx = super(Home, self).get_context_data(**kwargs)
        ctx['title'] = "Главная страница"
        return ctx
    
    
class NewsDetail(DetailView):
    model = News
    template_name = 'blog/news_detail.html'
    
    def get_context_data(self, **kwargs):
        ctx = super(NewsDetail, self).get_context_data(**kwargs)
        ctx['title'] = News.objects.get(id=self.kwargs['pk']).name
        return ctx
    

def reg(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            pass1 = form.cleaned_data.get('password1')
            pass2 = form.cleaned_data.get('password2')
            if pass1 == pass2:
                messages.success(request, f"Добро пожаловать, {username}!")
                form.save()
                return redirect('home')
            else:
                messages.error(request, "Пароли не совпадают!")
    else:
        form = RegForm()
    return render(request, "blog/reg.html", {"form": form, "title": "Registration Page"})


@login_required
def profile(request):
    if request.method == "POST":
        update_form = UpdateForm(request.POST, instance=request.user)
        update_image = UpdateImage(request.POST, request.FILES, instance=request.user.profile)
        if update_form.is_valid() and update_image.is_valid():
            update_form.save()
            update_image.save()
            messages.success(request, f"Профиль {update_form.cleaned_data.get("username")} успешно сохранен")
            return redirect('profile')
    else:
        pass
    update_form = UpdateForm(instance=request.user)
    update_image = UpdateImage(instance=request.user.profile)
    data = {
        "update_form": update_form,
        "update_image": update_image,
        "title": "Profile Page"
    }
    return render(request, 'blog/profile.html', data)

class CreateNew(LoginRequiredMixin, CreateView):
    model = News
    fields = ['name', 'text']
    
    template_name = 'blog/create_new.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class UpdateNew(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    fields = ['name', 'text']
    
    template_name = 'blog/edit_new.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        new = self.get_object()
        if self.request.user == new.author:
            return True
        return False
    
    
class DeleteNew(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'
    template_name = 'blog/delete_new.html'
    
    def test_func(self):
        new = self.get_object()
        if self.request.user == new.author:
            return True
        return False


def about(request):
    if request.method == "POST":
        form = AboutForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get("theme")
            to = form.cleaned_data.get("mail")
            from_email = "gracevnikolaj220@gmail.com"
            plain_message = form.cleaned_data.get("text")
            form.save()
            messages.success(request, "Письмо отправлено!")
            send_mail(subject, plain_message, from_email, [to])
            return redirect('home')
    else:
        form = AboutForm()
        return render(request, 'blog/about.html', {
            "title": "О нас",
            "form": form
        })