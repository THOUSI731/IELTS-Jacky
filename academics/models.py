from django.db import models

# Create your models here.

class QnA(models.Model):
    questions=models.CharField(max_length=255)
    answers=models.TextField()
    video=models.URLField()

class SubQnA(models.Model):
    qna=models.ForeignKey(QnA,on_delete=models.CASCADE,related_name="sub_qna")
    name=models.CharField(max_length=255)
    description=models.TextField()

class Exam(models.Model):
    short_description=models.TextField()
    long_description=models.TextField()
    video=models.URLField()
    slogan=models.CharField(max_length=255)
    qna = models.ForeignKey(QnA,on_delete=models.CASCADE,related_name="exam_qna")
    
    