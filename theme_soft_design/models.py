from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Course(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200,null=True,blank=True)
    audience = models.CharField(max_length=100)
    video = models.FileField(blank=True,upload_to="videos",null=True,)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnails = models.ImageField(upload_to='thumbnails',null=True)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})