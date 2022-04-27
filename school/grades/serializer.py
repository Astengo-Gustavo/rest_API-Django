from rest_framework import serializers
from grades.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['age','first_name','last_name']

