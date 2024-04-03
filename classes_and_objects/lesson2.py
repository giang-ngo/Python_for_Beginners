class Student:
    '''This class desciption student information and behavior'''

    def __init__(self, id, full_name, major, gpa):
        self.student_id = id
        self.set_full_name(full_name)
        self.major = major
        self.gpa = gpa
        self.full_name = self.last_name + ' ' + self.mid_name + self.first_name

    def set_full_name(self, full_name):
        words = full_name.split()
        self.last_name = words[0]
        self.first_name = words[len(words) - 1]
        self.mid_name = ''
        for x in range(1, len(words) - 1):
            self.mid_name += words[x] + ' '

    def show_info(self):
        print(f'[{self.student_id}, {self.full_name}, {self.major}, {self.gpa}]')


def create_student():
    print('==================================================')
    id = input('Enter id: ')
    full_name = input('Enter full name: ')
    major = input('Enter your major: ')
    gpa = float(input('Enter your gpa: '))
    return Student(id=id, full_name=full_name, major=major, gpa=gpa)


students = []
n = int(input('Enter number of student: '))
for x in range(n):
    student = create_student()
    students.append(student)

students.sort(key=lambda x: x.student_id, reverse=True)

for x in students:
    x.show_info()
