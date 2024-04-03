class Student:
    '''Lớp mô tả thông tin và hành động sinh viên'''

    def __init__(self, id, name, major):
        self.student_id = id
        self.name = name
        self.major = major

    def do_exam(self, subject):
        print(f'{self.name} is doing {subject} exam.')

    def word(self):
        print(f'{self.name} is woking')

    def do_homework(self,subject):
        print(f'{self.name} is doing {subject} homework')

huong=Student('SV001','Huong','CNTT')
huong.do_exam('math')
huong.do_homework('physics')
huong.word()
print(f'{huong.name}\'s {huong.student_id}')