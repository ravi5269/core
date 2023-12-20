from rest_framework import serializers
from home.models import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id','name','age','father_name']
        


