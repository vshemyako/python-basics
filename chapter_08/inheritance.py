class Person:

    def __init__(self):
        self.className = 'Person'


class Student(Person):

    def __init__(self):
        super().__init__()
        self.className = 'Student'

    def print_message(self):
        print('An instance of a {} class'.format(self.className))


student = Student()
student.print_message()
