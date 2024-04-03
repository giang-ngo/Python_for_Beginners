# def print_student_info(first, last, mid='', age=20):
#     '''This function print student  information'''
#     print(f'Full name: {first} {last} {mid}')
#     print(f'Age: {age}')
#     print('-----------------------------------')
#
#
# print_student_info('Khoa', 'Tran', 'Van', 21)
# print_student_info('Linh', 'Nguyen', 'Thuy')
# print_student_info('Hoang', 'Le')


# def print_words(*word):
#     i = 0
#     size = len(word)
#     while i < size:
#         print(f'{i}th parameter value: {word[i]}')
#         i += 1
#
#
# print_words('Hello', 1, 'Hi', 'Python', 'Django')


# def print_student_info(first, last, mid='', age=20):
#     '''This function print student  information'''
#     print(f'Full name: {first} {last} {mid}')
#     print(f'Age: {age}')
#     print('-----------------------------------')
#
# print_student_info(age=18,first='Nam',mid='Thanh',last='Hoàng')


def print_info(**info):
    print(f'Name: {info["name"]}')
    print(f'Age: {info["age"]}')
    print(f'Salary: {info["salary"]}')


print_info(age=16, name='Giang', salary='200000000')
