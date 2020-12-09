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
            }
            output['students'].append(student_details)

        return output

    @property
    def student_detail(self):
        return {
        'first_name': self.body.first_name,
        'last_name': self.body.last_name,
        'age': self.body.age,
        }