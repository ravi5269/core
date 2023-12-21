from rest_framework import serializers
from home.models import Student, Category, Book


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "age", "father_name"]

    def validate(self, data):
        if data["age"] < 18:
            raise serializers.ValidationError({"message": "age can`t be less then 18"})

        if data["name"]:
            for n in data["name"]:
                if n.isdigit():
                    raise serializers.ValidationError(
                        {"message": "name can not be numeric"}
                    )

        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
