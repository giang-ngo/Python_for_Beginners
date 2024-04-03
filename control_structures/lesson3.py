# Tính tổng các giá trị k đến n

# k = int(input('Enter integer number k: '))
# n = int(input('Enter integer number n >=k: '))
#
# sum = 0
# for i in range(k, n + 1, 1):
#     sum += i
# print(f'Sum from  {k} to {n}: {sum}')

# Hiển thị các kí tự trong 1 chuỗi

# full_name = input('Enter your full name: ')
# print('Spell your name: ')
#
# for i in full_name:
#     if i.isalpha():
#         print(f'"{i}"')
# else:
#     print('All done')

# Vẽ chữ nhật rỗng bằng dấu *

width = int(input('Enter width: '))
height = int(input('Enter height: '))

for i in range(-1, width + 1):
    for j in range(-1, height + 1):
        if i == 1 or i == width or j == 1 or j == height:
            print(' * ', end='')
        else:
            print('   ', end='')
    print()
