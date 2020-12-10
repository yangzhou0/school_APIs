from builtins import object

class StudentSerializer(object):
    def __init__(self, body):
        self.body = body

    @property
    def all_students(self):
        output = {'students': []}

        for student in self.body:
            student_details = {
                'first_name': student.first_name,
                'last_name': student.last_name,
                'age': student.age,
                'enrolled_courses':[]
            }
            for course in student.enrolled_courses.all(): #add all() here because without all(), its not query set;
                student_details['enrolled_courses'].append(course.course_name)
            output['students'].append(student_details)

        return output

    @property
    def student_detail(self):
        student_details = {
        'first_name': self.body.first_name,
        'last_name': self.body.last_name,
        'age': self.body.age,
        'enrolled_courses':[]
        }
        for course in self.body.enrolled_courses.all():
            student_details['enrolled_courses'].append(course.course_name)
        return student_details

class CourseSerializer(object):
    def __init__(self, body):
        self.body = body

    @property
    def all_courses(self):
        output = {'courses': []}

        for course in self.body:
            course_details = {
                'course_name': course.course_name,
                'enrolled_students': []
            }
            for student in course.enrolled_students.all():
                course_details['enrolled_students'].append(f"{student.last_name}, {student.first_name}")
            output['courses'].append(course_details)
        return output

    @property
    def course_detail(self):
        course_details = {
            'course_name': self.body.course_name,
            'enrolled_students': []
        }
        for student in self.body.enrolled_students.all():
            course_details['enrolled_students'].append(f"{student.last_name}, {student.first_name}")
        
        return course_details