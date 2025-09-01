from django.db import models
from ckeditor.fields import RichTextField

class Subscribe(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
    

class EmailTemplate(models.Model):
    subject = models.CharField(max_length=255)
    message = RichTextField()
    receipients = models.ManyToManyField(Subscribe)


    def __str__(self):
        return self.subject