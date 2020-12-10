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
    return JsonResponse(data={'status': f'Successfully deleted {student.first_name}.'}, status=200)


def all_courses(request):
    courses = Course.objects.all()
    serialized_courses = CourseSerializer(courses).all_courses
    return JsonResponse(data=serialized_courses, status=200)

def course_detail(request,course_id):
    course = Course.objects.get(id=course_id)
    serialized_course = CourseSerializer(course).course_detail
    return JsonResponse(data=serialized_course, status=200)

@csrf_exempt
def update_course(request,course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        data = json.load(request)
        form = CourseForm(data, instance=course)
        if form.is_valid():
            course = form.save(commit=True)
            serialized_course = CourseSerializer(course).course_detail
            return JsonResponse(data=serialized_course, status=200)

@csrf_exempt
def delete_course(request,course_id):
    if request.method == "POST":
        course = Course.objects.get(id=course_id)
        course.delete()
    return JsonResponse(data={f"successfully added {course.course_name}"}, status=200)

@csrf_exempt
def enroll_course(request,course_id,student_id):
    if request.method == 'POST':
        course = Course.objects.get(id=course_id)
        print('course enrolled students before enrollment ',course.enrolled_students.all())
        student = Student.objects.get(id=student_id)
        course.enrolled_students.add(student)
        print('course enrolled students after enrollment ',Course.objects.get(pk=course.pk).enrolled_students.all())
        print('course enrolled for this students ',student.enrolled_courses.all())
        return JsonResponse(data={'status': f"Successfully enrolled {student.first_name} {student.last_name} to {course.course_name}"}, status=200)

    

@csrf_exempt
def drop_course(request,course_id,student_id):
    pass

@csrf_exempt
def new_course(request):
    if request.method == "POST":
        data = json.load(request)
        form = CourseForm(data)
        if form.is_valid():
            course = form.save(commit=True)
            serialized_course = CourseSerializer(course).course_detail
            return JsonResponse(data=serialized_course, status=200)

