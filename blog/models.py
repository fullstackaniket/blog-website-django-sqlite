from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save
from django.utils.text import slugify
from django.urls import reverse

class Cate(models.Model):
    S_Choice=(
        ('hide','Hide'),
        ('show','Show')
    )
    c_name = models.CharField(max_length=40)
    c_img = models.ImageField(upload_to="CatImg")
    c_status =models.CharField(max_length=20,choices=S_Choice, default='hide')


    def __str__(self):
        return self.c_name
    

class BlogInfo(models.Model):
    B_Choice=(
        ('hide','Hide'),
        ('show','Show'),
    )
    b_cat = models.ForeignKey(Cate,on_delete=False)
    title = models.CharField(max_length=50)
    b_img = models.ImageField(upload_to='blogImage')
    slug = models.SlugField(max_length=70)
    author = models.ForeignKey(User,on_delete=False)
    b_status = models.CharField(max_length=20,choices=B_Choice,default='hide')
    b_create = models.DateTimeField( auto_now_add=True)
    b_update = models.DateTimeField( auto_now=True)
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name="likes",blank=True)
    


 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("singlestandard", args=[self.id,self.slug])
    def total_likes(self):
        return self.likes.count()

@receiver(pre_save,sender=BlogInfo)
def save_slug(sender,**kwargs):
    slug=slugify(kwargs['instance'].title)
    print(slug)
    kwargs['instance'].slug=slug



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio= models.TextField(max_length=500,blank=True,)
    location = models.CharField(max_length=35,blank=True)
    dob=models.DateTimeField(null=True, blank=True)
    pic=models.ImageField(upload_to="profile_img", default="awatar.jpg")
        

@receiver(post_save,sender=User)
def save_profile_user(sender, instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



class BascicSettings(models.Model):
    icon=models.ImageField(upload_to="icon", blank=True)
    facebook=models.URLField(max_length=300)
    twitter= models.URLField(max_length=300)
    instagram= models.URLField(max_length=300)
    pinterest=models.URLField(max_length=300)
    driblelink=models.URLField(max_length=300)
    email=models.EmailField(max_length=300)
    phone=models.CharField(max_length=10)
   
   

