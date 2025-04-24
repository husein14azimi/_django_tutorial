from django.db import models

# Create your models here.



class Product(models.Model):
    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Book(models.Model):

    title = models.CharField(max_length=200)

    author = models.CharField(max_length=100, blank=True, null=True)

    published_date = models.DateField(blank=True, null=True)


    def __str__(self):

        return self.title
    
    
class Document(models.Model):
    title=models.CharField(max_length=255)
    number_of_pages = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title