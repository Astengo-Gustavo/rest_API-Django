from django.http import HttpResponse
from grades.models import Student
from django.http import JsonResponse
from grades.serializer import StudentSerializer
from rest_framework import viewsets

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


