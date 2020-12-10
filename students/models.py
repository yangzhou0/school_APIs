from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    
        
class Course(models.Model):
    course_name = models.CharField(max_length=250)
    enrolled_students = models.ManyToManyField(
        Student, related_name='enrolled_courses',blank=True)

# class Enrollment(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)