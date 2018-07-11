from django.db import models

# Create your models here.


class Exam(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.name


class Quiz(models.Model):
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE,)
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to='upload', null=True, blank=True)

    def __unicode__(self):
        return self.name


class Choice(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,)
    name = models.CharField(max_length=200)
    corrected = models.BooleanField(default=False)


    def __unicode__(self):
        return self.name

