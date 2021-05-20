from django.db import models
from django.template.defaultfilters import truncatechars
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.utils import timezone


from PIL import Image

import os

# Create your models here.

# Contact Model
class Contact(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    subject = models.CharField(max_length=200, null=False)
    message = models.CharField(max_length=2000, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    @property
    def short_msg(self):
        return truncatechars(self.message, 20)



# Portfolio Update Model
class PortfolioUpdate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    about = models.TextField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=14, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True, blank=True)
    github = models.CharField(max_length=100, null=True, blank=True)
    uniM = models.CharField(max_length=100, null=True, blank=True)
    uniM_subject = models.CharField(max_length=100, null=True, blank=True)
    uniM_result = models.CharField(max_length=10, null=True, blank=True)
    uniM_passing = models.CharField(max_length=4, null=True, blank=True)
    uni = models.CharField(max_length=100, null=True, blank=True)
    uni_subject = models.CharField(max_length=100, null=True, blank=True)
    uni_result = models.CharField(max_length=10, null=True, blank=True)
    uni_passing = models.CharField(max_length=4, null=True, blank=True)
    clg = models.CharField(max_length=100, null=True, blank=True)
    clg_group = models.CharField(max_length=20, null=True, blank=True)
    clg_result = models.CharField(max_length=10, null=True, blank=True)
    clg_passing = models.CharField(max_length=4, null=True, blank=True)
    skills = models.CharField(max_length=2000, null=True, blank=True)
    company1 = models.CharField(max_length=100, null=True, blank=True)
    designation1 = models.CharField(max_length=100, null=True, blank=True)
    period1 = models.CharField(max_length=50, null=True, blank=True)
    company2 = models.CharField(max_length=100, null=True, blank=True)
    designation2 = models.CharField(max_length=100, null=True, blank=True)
    period2 = models.CharField(max_length=50, null=True, blank=True)
    theme = models.CharField(max_length=50, default='default')
    image = models.ImageField(default='default.jpg', upload_to='images/user', null=True, blank=True)
    popularity = models.IntegerField(blank=True, null=True, default=0)

    def save(self):
        super().save()  # saving image first
        img = Image.open(self.image.path) # Open image using self
        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.image.path)  # saving image at the same path
    

    def __str__(self):
        return  f'{self.user.username}'
    
    @property
    def short_about(self):
        return truncatechars(self.about, 20)




class Theme(models.Model):
    name = models.CharField(max_length=50)
    html = models.CharField(max_length=20, blank=True, null=True)
    designer = models.CharField(max_length=50, blank=True, null=True)
    designerurl = models.URLField(max_length=200, blank=True, null=True)
    popularity = models.IntegerField(blank=True, null=True, default=0)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    skicon = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


