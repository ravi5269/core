


from django.urls import path
from home.views import home,post_student
from django.contrib import admin

urlpatterns = [
   
    path('get_student/',home),
    path('post_student/',post_student)
    
]
