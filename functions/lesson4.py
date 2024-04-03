# Tạo biểu thức lambda nhân 10 vào số a bất kì

f = lambda a: a * 10
print(f(10))

# a = lambda: print('OK')
# a()
sum = lambda a, b: a + b
print(sum(3, 5))


def my_function(n):
    return lambda a: a * n


doubler = my_function(2)
tripler = my_function(3)
x = 11
print(f'Before: {x}, after double value: {doubler(x)}')
print(f'Before: {x}, after double value: {tripler(x)}')
