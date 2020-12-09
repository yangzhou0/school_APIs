from django.urls import path
from . import views
app_name = 'students'
urlpatterns = [
    path('', views.all_students, name='all_students'),
    path('new_student', views.new_student, name='new_student'),
    path('<int:student_id>', views.student_detail, name='student_detail'),
    path('<int:student_id>/update', views.update_student, name='update_student'),
    path('<int:student_id>/delete', views.delete_student, name='delete_student'),
]