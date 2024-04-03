'''
  Liệt kê các số nguyên chia hết cho k trong đoạn [m,n] với m<=n nhập vào từ bàn phím .Nếu m>n hoặc k =0 thì in ra
  thông báo để người dùng nhập lại
'''

m = int(input('Enter m: '))
n = int(input('Enter n>m: '))
k = int(input('Enter k !=0: '))

if k == 0 or n < m:
    print('Please enter number k!=0 and m<=n')
else:
    i = m
    while i <= n:
        if i % k == 0:
            print(f'{i} ', end='')
        i += 1
    else:
        print(f'\nTask completed')


