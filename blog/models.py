from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

category = [
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
]


""" Post model """
class Post(models.Model):
    categories = (("1",'zjc level Documents'),
    ("2",'Olevel Documents'),
    ("3",'Alevel Documents'),
    ("4",'zjc Videos'),
    ("5",'Olevel Videos'),
    ("6",'Alevel Videos'),
    ("7",'All documents'),
    ("8",'All Videos'))
    
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    body = models.TextField(null=True,blank=True)
    video = models.FileField(blank=True,upload_to="videos",null=True,)
    document = models.FileField(blank=True,upload_to="documernts",null=True,)
    date_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    thumbnails = models.ImageField(upload_to='thumbnails',null=True)
    details = models.TextField(max_length=10000,null=True,blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="blogpost", blank=True)
    saves = models.ManyToManyField(User, related_name="blogsave", blank=True)
    category = models.CharField(choices=categories,max_length=8,default="1")     
    

    def total_likes(self):
        return self.likes.count()

    def total_saves(self):
        return self.saves.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"pk":self.pk})


""" Comment model """
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments" , on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blogcomment", blank=True)
    reply = models.ForeignKey('self', null=True, related_name="replies", on_delete=models.CASCADE)

    def total_clikes(self):
        return self.likes.count()

    def __str__(self):
        return '%s - %s - %s' %(self.post.title, self.name, self.id)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"pk":self.pk})
