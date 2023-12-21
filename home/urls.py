


from django.urls import path
from home.views import home,post_student,upadte_student,partial_upadte_student,delete_student
from django.contrib import admin

urlpatterns = [
   
    path('get_student/',home),
    path('post_student/',post_student),
    path('update_student/',upadte_student),
    path('update_student/<int:pk>',upadte_student),
    path('partial_update_student/<int:pk>',partial_upadte_student),
    path('delete_student/<int:pk>',delete_student)
    

    
]
