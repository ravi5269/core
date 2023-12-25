from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Student, Book, Category
from home.serializers import (
    StudentSerializer,
    User,
    BookSerializer,
    CategorySerializer,
    UserSerializer,
)

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

# from rest_framework.authentication import SessionAuthentication,BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            # print(serializer.errors)
            return Response(
                {"message": "something went worng", "errors": serializer.errors}
            )

        serializer.save()
        user = User.objects.get(username=serializer.data["username"])
        refresh = RefreshToken.for_user(user)
        # print(token_obj.key)
        return Response(
            {"messages": "success",
            "payload": serializer.data,
            "refresh": str(refresh),
            "access":str(refresh.access_token),"message":"your data is saved"}
        )


class StudentAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs, many=True)

        return Response({"message": 200, "payload": serializer.data})

    def post(self, request):
        data = request.data
        seroalizer = StudentSerializer(data=request.data)

        if not seroalizer.is_valid():
            print(seroalizer.errors)
            return Response(
                {"message": "something went worng", "errors": seroalizer.errors}
            )

        seroalizer.save()
        return Response({"messages": "success", "payload": seroalizer.data})

    def put(self, request, pk):
        try:
            student_obj = Student.objects.get(pk=pk)
            seroalizer = StudentSerializer(student_obj, data=request.data)

            if not seroalizer.is_valid():
                print(seroalizer.errors)
                return Response(
                    {"message": "something went worng", "errors": seroalizer.errors}
                )

            seroalizer.save()
            return Response({"messages": "success", "payload": seroalizer.data})
        except Exception as e:
            print(e)
            return Response({"message": "invallid ID"})

    def patch(self, request, pk):
        try:
            student_obj = Student.objects.get(pk=pk)
            seroalizer = StudentSerializer(student_obj, data=request.data, partial=True)

            if not seroalizer.is_valid():
                print(seroalizer.errors)
                return Response(
                    {"message": "something went worng", "errors": seroalizer.errors}
                )

            seroalizer.save()
            return Response({"messages": "success", "payload": seroalizer.data})
        except Exception as e:
            print(e)
            return Response({"message": "invallid ID"})

    def delete(self, request, pk):
        try:
            student_obj = Student.objects.get(pk=pk)
            student_obj.delete()
            return Response({"message": "deleted success"})
        except Exception as e:
            print(e)
            return Response({"message": "invallid ID"})


@api_view(["GET"])
def home(request):
    student_objs = Student.objects.all()
    serializer = StudentSerializer(student_objs, many=True)

    return Response({"message": 200, "payload": serializer.data})


@api_view(["POST"])
def post_student(request):
    data = request.data
    seroalizer = StudentSerializer(data=request.data)

    if not seroalizer.is_valid():
        print(seroalizer.errors)
        return Response(
            {"message": "something went worng", "errors": seroalizer.errors}
        )

    seroalizer.save()
    return Response({"messages": "success", "payload": seroalizer.data})


@api_view(["PUT"])
def upadte_student(request, pk):
    try:
        student_obj = Student.objects.get(pk=pk)
        seroalizer = StudentSerializer(student_obj, data=request.data)

        if not seroalizer.is_valid():
            print(seroalizer.errors)
            return Response(
                {"message": "something went worng", "errors": seroalizer.errors}
            )

        seroalizer.save()
        return Response({"messages": "success", "payload": seroalizer.data})
    except Exception as e:
        print(e)
        return Response({"message": "invallid ID"})


@api_view(["PATCH"])
def partial_upadte_student(request, pk):
    try:
        student_obj = Student.objects.get(pk=pk)
        seroalizer = StudentSerializer(student_obj, data=request.data, partial=True)

        if not seroalizer.is_valid():
            print(seroalizer.errors)
            return Response(
                {"message": "something went worng", "errors": seroalizer.errors}
            )

        seroalizer.save()
        return Response({"messages": "success", "payload": seroalizer.data})
    except Exception as e:
        print(e)
        return Response({"message": "invallid ID"})


@api_view(["DELETE"])
def delete_student(request, pk):
    try:
        student_obj = Student.objects.get(pk=pk)
        student_obj.delete()
        return Response({"message": "deleted success"})
    except Exception as e:
        print(e)
        return Response({"message": "invallid ID"})
