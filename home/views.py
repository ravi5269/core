from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Student
from home.serializers import StudentSerializer


@api_view(['GET'])
def home(request):
    student_objs = Student.objects.all()
    serializer = StudentSerializer(student_objs, many =True)

    return Response({"message": 200, 'payload':serializer.data})

@api_view(['POST'])
def post_student(request):
    data = request.data
    seroalizer = StudentSerializer(data=request.data)

    if not seroalizer.is_valid():
        print(seroalizer.errors)
        return Response({'message':'something went worng','errors': seroalizer.errors})
    
    seroalizer.save()
    return Response({'messages':'success','payload':seroalizer.data})
