class Person:
    def __init__(self, last, first, mid, dob, gender):
        self.last = last
        self.first = first
        self.mid = mid
        self.dob = dob
        self.gender = gender

    def show_info(self):
        print(f'[Name: {self.last} {self.mid} {self.first}, '
              f'Date of birth: {self.dob}, Gender: {self.gender}]')


class Student(Person):
    def __init__(self, last, first, mid, dob, gender, major, sid, gpa):
        super(Student, self).__init__(last, first, mid, dob, gender)
        self.major = major
        self.sid = sid
        self.gpa = gpa

    def do_exam(self, subject):
        print(f'{self.first} làm bài kiểm tra môn {subject}')


class Employee(Person):
    def __init__(self, last, first, mid, dob, gender, salary, role, eid):
        super(Employee, self).__init__(last, first, mid, dob, gender)
        self.salary = salary
        self.role = role
        self.eid = eid

    def checkin(self, time):
        print(f'{self.first} vào làm lúc {time}')

    def calculate_salary(self, day):
        real_salary = self.salary * day / 22
        print(f'{self.first} có mức lương là {real_salary}')


linh = Student('Nguyen', 'Linh', 'Thuy', '21/5/2000', 'Nữ', 'CNTT', 'SV01', 3.6)
linh.do_exam('math')
linh.show_info()
nam = Employee('Nguyen', 'Nam', 'Van', '21/9/1999', 'Nam', 2000000, 'CEO', 'NV001')
nam.checkin('8:30')
nam.calculate_salary(30)
