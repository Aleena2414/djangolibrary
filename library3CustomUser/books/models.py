from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=30)
    author = models.CharField(max_length=40)
    page = models.IntegerField()
    price=models.IntegerField()
    language = models.CharField(max_length=40)
    cover=models.ImageField(upload_to='images')
    pdf=models.FileField(upload_to='pdf')

    def __str__(self):
        return self.title