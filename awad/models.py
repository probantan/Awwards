# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,null=True,)
    bio = models.CharField(max_length=256, default='Edit profile for your bio')
    profile_pic = models.ImageField(upload_to='pictures/',  default="default.jpeg", null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Category(models.Model):
    name=models.CharField(max_length=60,default="")

class Project(models.Model):
    project_name = models.CharField(max_length =20)
    image=models.ImageField(upload_to='projects/', blank=True)
    detailed_description=models.TextField()
    project_url = models.CharField(max_length =50)
    deployed_link=models.CharField(max_length=40)
    category=models.ForeignKey(Category,related_name='category',null=True, blank=True, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, null = True,related_name='project')
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    user= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)


