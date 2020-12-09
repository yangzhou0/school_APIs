# added some comments
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import StudentForm,CourseForm
from .models import Student,Course
from .serializers import StudentSerializer, CourseSerializer
import json

def all_students(request):
    students = Student.objects.all()
    serialized_students = StudentSerializer(students).all_students
    return JsonResponse(data=serialized_students, status=200)


def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    serialized_student = StudentSerializer(student).student_detail
    return JsonResponse(data=serialized_student, status=200)

@csrf_exempt
def new_student(request):
    if request.method == "POST":
        data = json.load(request)
        form = StudentForm(data)
        if form.is_valid():
            student = form.save(commit=True)
            serialized_student = StudentSerializer(student).student_detail
            return JsonResponse(data=serialized_student, status=200)

@csrf_exempt
def update_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        data = json.load(request)
        form = StudentForm(data, instance=student)
        if form.is_valid():
            student = form.save(commit=True)
            serialized_student = StudentSerializer(student).student_detail
            return JsonResponse(data=serialized_student, status=200)


@csrf_exempt
def delete_student(request, student_id):
    if request.method == "POST":
        student = Student.objects.get(id=student_id)
        student.delete()
    return JsonResponse(data={'status': 'Successfully deleted student.'}, status=200)


    def all_courses(request):
        courses = Course.objects.all()
        serialized_courses = courseserializer(courses).all_courses
        return JsonResponse(data=serialized_courses, status=200)

    def course_detail(request,course_id):
        pass

    def update_course(request,course_id):
        pass
    def delete_course(request,course_id):
        pass

    def enroll_course(request,course_id,student_id):
        pass

    def drop_course(request,course_id,student_id):
        pass

