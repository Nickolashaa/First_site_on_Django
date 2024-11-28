from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import datetime
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    MALE = "M"
    FEMALE = "F"
    SEX_CHOICES = [
        (MALE, "Мужской"),
        (FEMALE, "Женский")
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField("Аватарка пользователя", default='default.png', upload_to='user_images')
    sex = models.CharField("Пол", max_length=1, choices=SEX_CHOICES, default=MALE)
    mark = models.BooleanField("Согласие на отправку уведомлений по почте", default=False)

    
    def __str__(self):
        return f"Профиль пользователя {self.user.username}"
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        
    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 256 or img.width > 256:
            resize = (256, 256)
            img.thumbnail(resize)
            img.save(self.image.path)
            
            
            
class News(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название статьи", max_length=200, default="None")
    text = models.TextField("Содержание статьи", null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField("Время публикации статьи", default=datetime.now())
    
    def __str__(self):
        return f"Статья пользователя {self.author.username}"
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        
    def get_absolute_url(self):
        return reverse('news_id', kwargs={"pk": self.pk})
    

class Letters(models.Model):
    theme = models.CharField("Тема письма", max_length=200, default="Без темы")
    mail = models.EmailField("Электронная почта")
    text = models.TextField("Текст письма")
    
    
    class Meta:
        verbose_name = "Письмо"
        verbose_name_plural = "Письма"

    def __str__(self):
        return f"Письмо от пользователя { self.mail }"