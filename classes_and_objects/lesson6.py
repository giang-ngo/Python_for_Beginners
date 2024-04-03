class Person:
    def __init__(self, fname, gender, dob):
        self.__full_name = fname
        self.__gender = gender
        self._dob = dob

    def eat(self, food):
        print(f'{self.__full_name} đang ăn {food}')

    def __str__(self):
        return f'[{self.__full_name}, {self.__gender}, {self._dob}]'


class Student(Person):
    def __init__(self, fname, gender, dob, sid, gpa):
        super().__init__(fname, gender, dob)
        self.__student_id = sid
        self.__gpa = gpa

    def do_exam(self, subject):
        print(f'{self._Person__full_name} đang làm bài kt môn {subject}')

    def update_gpa(self, gpa):
        self.__gpa = gpa

    def __str__(self):
        return f'{super().__str__()},{self.__student_id},{self.__gpa}'


huong = Student("Nguyen Thi Huong", 'Nu', '25/09/2007', 'SV001', 3.7)
huong.do_exam('Toan')
huong.update_gpa(3.9)
print(f'GPA: {huong._Student__gpa}')
thuy = Person("Nguyen Thi Thuy", 'Nu', '25/09/2003')
thuy.eat('seafood')
print(huong)
print(thuy)
print(thuy._dob)
