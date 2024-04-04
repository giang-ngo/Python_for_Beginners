'''
try:
    # do something
except:
    print("Exception occurred")


# Để xử lý riêng với từng loại ngoại lệ, có thể chỉ định rõ loại của ngoại lệ trong khai báo except:

try:
    # do something
except ErrorType1:
    print('ErrorType1')
except ErrorType2:
    print('ErrorType2')
except:
    print("Other exception")

# Trong trường hợp muốn thực hiện một hành động sau khi kết thúc một công việc bất chấp ngoại lệ có xảy ra trong quá trình thực hiện công việc đó hay không, có thể dùng finally:

try:
    # do something
except:
    print('Exception occurred')
finally:
    print('After try/except finished')


# Trong trường hợp muốn thực hiện một hành động sau khi kết thúc một công việc bất chấp ngoại lệ có xảy ra trong quá trình thực hiện công việc đó hay không, có thể dùng cấu trúc:

try:
    # do something
except:
    print("Exception occurred")
else:
   print("Sau khi chạy dòng try thành công không bị lỗi")
finally:
    print('After try/except finished')

'''
# ví dụ 1
a = 5
b = 0
try:
    result = a / b
except ZeroDivisionError:
    result = "Cannot divide by 0"
print(result)

# ví dụ 2
a = "Hello"
try:
    x = a + 10
except TypeError:
    print("Không thể thực hiện phép cộng giữa chuỗi và số nguyên")
