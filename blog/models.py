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
    categories = (("1",'family and religous studies'),
    ("2",'physics'),
    ("3",'chemistry'),
    ("4",'mathematics'),
    ("5",'technology'),
    ("6",'english'),
    ("7",'shona'),
    ("8",'history'),
    ("9","business studies"),
    ('10','biology'),
    ('11','accounts'),
    ('12','combined science'),
    ('13','economics'),
    ('14','geography'))
    
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=100,blank=True, null=True)
    audience = models.TextField(null=True,blank=True)
    writer = models.TextField(max_length=50,null=True,blank=True)
    publisher = models.TextField(max_length=50,null=True,blank=True)
    document = models.FileField(blank=True,upload_to="documernts",null=True,)
    date_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    thumbnails = models.ImageField(upload_to='thumbnails',null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=2000,blank=True,null=True)
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
