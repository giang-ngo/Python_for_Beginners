# def factorial(n):
#     '''Hàm tính n giai thừa đệ qui'''
#     if n == 1 or n == 0:
#         return 1
#     return n * factorial(n - 1)
#
#
# def factorial_loop(n):
#     result = 1
#     for x in range(1, n + 1):
#         result *= x
#     return result
#
#
# value=5
# print(f'{value}! = {factorial(value)}')
# print(f'{value}! = {factorial_loop(value)}')


# n = int(input('Enter an integer number > 0: '))
#
#
# def sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum(n - 1)
#
#
# print(sum(n))


def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


k = int(input('Enter an integer number >=0: '))
print(fibo(k))
