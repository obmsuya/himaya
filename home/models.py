from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):

    post = models.CharField(max_length=200)
    bookname = models.CharField (max_length=220, default='', blank=True)
    booklink = models.CharField (max_length=220, default='', blank=True)
    bookimage = models.ImageField(default='default.jpg', upload_to='media')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
  

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Category'
        
    name = models.CharField(max_length=32)
    
    def __str__(self):
        return self.name

class Paymentdetail(models.Model):
    name = models.CharField (max_length=120, default='')
    
    def __str__(self):
        return self.name
    


class Item(models.Model):
    class Meta:
        verbose_name_plural = 'Item'
    
    name = models.CharField(max_length= 50)
    subtitle = models.CharField (max_length=120, default='', blank=True)
    description = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='media')
    
    image_author = models.ImageField(default='default.jpg', upload_to='media')
    

    image_index = models.ImageField(default='default.jpg', upload_to='media')
    
    videofile= models.FileField(default='default.mp4', upload_to='media', null=True, verbose_name="")

    author = models.CharField(max_length=200, default= "")
    author_description = models.TextField(default= "")
    price = models.IntegerField(default=0)
    tigopesa = models.IntegerField(default=0, blank=True)
    mpesa = models.IntegerField(default=0, blank=True)
    airtel = models.IntegerField(default=0, blank=True)
    halotel = models.IntegerField(default=0, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    paymentdetail = models.ForeignKey(Paymentdetail, null=True, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name + ": " + str(self.videofile)
    def get_absolute_url(self):
        return "/item/%i/" % self.pk
  





class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.current_user
    
    
    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

        
    
    def __str__(self):
        return str(self.current_user)

        
    # @classmethod
    # def lose_friend(cls, current_user, new_friend):
    #     friend, created = cls.objects.get_or_create(
    #         current_user=current_user
    #     )
    #     friend.users.remove(new_friend)
    

     
#This model is for class registration 
class Post4(models.Model):
    class Meta:
        verbose_name_plural = 'Students Request'
    
    fullname = models.CharField (max_length=100, default='')
    username = models.CharField (max_length=100, default='')
    country = models.CharField (max_length=100, default='')
    region = models.CharField (max_length=100, default='')
    Proffession = models.CharField (max_length=100, default='')
    book = models.CharField (max_length=250, default='')
    subtitle = models.CharField (max_length=100, default='')
    phone = models.IntegerField(default=0)
    Jina = models.CharField (max_length=100, default='')
    Simu = models.IntegerField(default=0)
    Tukusaidiaje = models.TextField(default='')
    
    
    
    def __str__(self):
        return self.fullname
    







