from django.db import models

# Create your models here.


class Thumbnail(models.Model):
    title_name = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=255, null=True)
    link_text = models.CharField(max_length=50, null=True)
    link = models.URLField(null=True)
    background_image = models.ImageField(upload_to="background/")

    def __str__(self) -> str:
        return self.title_name


# class Feature(models.Model):
#     title_name = models.CharField(max_length=100)
#     description = models.TextField(null=True)
#     image = models.ImageField(upload_to="home/", null=True)

#     def __str__(self) -> str:
#         return self.title_name


class Accordion(models.Model):
    title_name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    profile_picture = models.ImageField(upload_to="accordion/", null=True)
    
    def __str__(self) -> str:
        return self.title_name


class Testimonial(models.Model):
    text_name = models.CharField(max_length=500)
    writer = models.CharField(max_length=60, default="~ Unknown")
    profile_picture = models.ImageField(
        upload_to="testimonials/", default="testimonials/user-dummy_nn5Ltlb.png"
    )

    def __str__(self) -> str:
        return self.writer


class SocialMedia(models.Model):
    social_name = models.CharField(max_length=50)
    social_link = models.URLField()
    social_logo = models.ImageField(upload_to="social/")


class Teacher(models.Model):
    name = models.CharField(max_length=155)
    profile_picture=models.ImageField(upload_to="teachers/",null=True)
    position = models.CharField(max_length=100, null=True)
    short_description = models.CharField(max_length=255, null=True)
    
    
    def __str__(self) -> str:
        return self.name
    
class Post(models.Model):
    class UserChoices(models.TextChoices):
        ADMIN = "admin","Admin"
        USER="user","User"
    title_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="blogs/")
    user_type=models.CharField(max_length=30,choices=UserChoices.choices,default=UserChoices.ADMIN)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.title_name
    
    
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="blog_comments")
    full_name=models.CharField(max_length=100)
    email=models.EmailField()
    website=models.URLField(null=True,blank=True)
    message=models.TextField()
    
    def __str__(self):
        return self
    
    