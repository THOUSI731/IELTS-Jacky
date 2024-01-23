from django.db import models

# Create your models here.

class Thumbnail(models.Model):
    title_name=models.CharField(max_length=100)
    sub_title=models.CharField(max_length=255,null=True)
    link=models.URLField(null=True)
    

class Feature(models.Model):
    title_name=models.CharField(max_length=100)
    description=models.TextField(null=True)
    image=models.ImageField(upload_to="home/",null=True)
    

class Accordion(models.Model):
    title_name=models.CharField(max_length=255)
    description=models.TextField(null=True)
    
class Testimonial(models.Model):
    text_name=models.CharField(max_length=255)
    writer=models.CharField(max_length=60,default="~ Unknown")
    
class SocialMedia(models.Model):
    social_name=models.CharField(max_length=50)
    social_link=models.URLField()
    social_logo=models.ImageField(upload_to="social/")