from django.contrib import admin

# Register your models here.
from home.models import Student, Book, Category

admin.site.register([Student, Book, Category])
