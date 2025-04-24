from django.contrib import admin
from .models import Product, Book, Document, Article
# Register your models here.

admin.site.register(Product)
admin.site.register(Book)
admin.site.register(Document)
admin.site.register(Article)