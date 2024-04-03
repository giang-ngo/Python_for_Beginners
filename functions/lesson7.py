message = 'Hello'
print(message)

# for x in message:
#     print(f'{x} ', end='')
# print()
#
# for x in range(0, len(message)):
#     print(f'{message[x]} ', end='')
# print()
#
# for e in range(-1, -len(message) - 1, -1):
#     print(f'{message[e]} ', end='')
# print()
#
# for i in range(-len(message), 0, 1):
#     print(f'{message[i]} ', end='')
# print()

# print(message[0:3])
# print(message[:3])
# print(message[3:])
# print(message[3:len(message)])
# print(message[:])

# print(r'Hello PyCharm')
# print('Welcome to \"PyCharm\"')
# print('D:\\Hello\\Some Folder\\Blabla')

string = '   welcome to PyCharm    '
numbers = '-3238201'
print(string.upper())
print(string.lower())
print(string.capitalize())  # viết hoa chữ cái đầu dòng
print(string.title())  # viết hoa chữ cái đầu của từ
print(string.swapcase())  # tráo đổi kí tự hoa thành thường và ngược lại
print(string.zfill(40))  # thêm 0 cho đủ 40 kí tự
print(numbers.zfill(20))
print(string.strip())  # bỏ khoảng trước trước, sau chuỗi
