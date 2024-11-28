from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Letters


class RegForm(UserCreationForm):
    username = forms.CharField(label="Введите ваше имя", required=True, widget=forms.TextInput(attrs={
			"class": "form_field",
            "placeholder": "Ivan_2005"
		}))
    
    email = forms.CharField(label="Введите вашу электронную почту", required=True, widget=forms.TextInput(attrs={
			"class": "form_field",
            "placeholder": "Ivan_2005@yandex.ru"
		}))
    
    password1 = forms.CharField(
        label="Придумайте сложный пароль",
        required=True,
        widget=forms.PasswordInput(attrs={
			"class": "form_field"
		}))
    
    password2 = forms.CharField(
        label="Подтвердите пароль",
        required=True,
        widget=forms.PasswordInput(attrs={
			"class": "form_field"
		}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
class UpdateForm(forms.ModelForm):
    username = forms.CharField(label="Изменить логин", required=True, widget=forms.TextInput(attrs={
			"class": "form_field"
		}))
    
    email = forms.CharField(label="Изменить электронную почту", required=True, widget=forms.TextInput(attrs={
			"class": "form_field"
		}))
    
    class Meta:
        model = User
        fields = ['username', 'email']
        
        
class UpdateImage(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'sex', 'mark']
    
    image = forms.ImageField(label="Загрузить фото", required=False, widget=forms.FileInput)
    
    MALE = "M"
    FEMALE = "F"
    SEX_CHOICES = [
        (MALE, "Мужской"),
        (FEMALE, "Женский")
    ]
    
    sex = forms.ChoiceField(choices=SEX_CHOICES, label="Выберите пол", required=False)
    
    mark = forms.BooleanField(label="Соглашение на отправку уведомлений на почту", required=False)
    
    
class AboutForm(forms.Form):
    theme = forms.CharField(label="Тема письма", required=True, widget=forms.TextInput(attrs={
			"class": "form_field",
            "placeholder": "Введите тему письма"
		}))
    mail = forms.CharField(label="Ваша электронная почта", required=True, widget=forms.TextInput(attrs={
			"class": "form_field",
            "placeholder": "Введите вашу электронную почту"
		}))
    text = forms.CharField(label="Текст письма", required=True, widget=forms.TextInput(attrs={
			"class": "form_field",
            "placeholder": "Напишите всё, что хотите"
		}))
    
    class Meta:
        model = Letters
        fields = ['theme', 'mail', 'text']
        
    def save(self):
        if self.is_valid():
            cleaned_data = self.cleaned_data
            letter = Letters(
                theme=cleaned_data['theme'],
                mail=cleaned_data['mail'],
                text=cleaned_data['text']
            )
            letter.save()
            return letter