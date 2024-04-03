# Đọc vào string str
# Đọc vào số nguyên int
# Đọc vào số thực float

full_name = input('Nhập vào tên của bạn rồi nhấn phím Enter: ')
print('Xin chào ', full_name)
address = input('Bạn ở đâu vậy? ')
print(f'Bạn {full_name} đến từ {address}')
age = int(input('Bạn bao nhiêu tuổi? '))
print(f'Ồ bạn {full_name} {age} tuổi')
gpa = float(input(f'Điểm trung bình môn kì trước của bạn là bao nhiêu? '))
print(f'Bạn {full_name} với điểm trung bình {gpa}')