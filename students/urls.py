from django.urls import path
from . import views
app_name = 'students'
urlpatterns = [
    path('students', views.all_students, name='all_students'),
    path('students/new_student', views.new_student, name='new_student'),
    path('students/<int:student_id>', views.student_detail, name='student_detail'),
    path('students/<int:student_id>/update', views.update_student, name='update_student'),
    path('students/<int:student_id>/delete', views.delete_student, name='delete_student'),
    path('courses', views.all_courses, name='all_courses'),
    path('courses/new_course', views.new_course, name='new_course'),
    path('courses/<int:course_id>', views.course_detail, name='course_detail'),
    path('courses/<int:course_id>/update', views.update_course, name='update_course'),
    path('courses/<int:course_id>/delete', views.delete_course, name='delete_course'),
    path('courses/<int:course_id>/students/<int:student_id>/enroll', views.enroll_course, name='enroll_course'),
    path('courses/<int:course_id>/students/<int:student_id>/drop', views.drop_course, name='drop_course'),
]