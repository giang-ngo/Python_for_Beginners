# 1.Đảo ngược tuple sau
# Ví dụ:
# x = (1, 2, 3, 7, 5)

x = (1, 2, 3, 7, 5)
reversed_tuple = tuple(reversed(x))
print(reversed_tuple)

# *2. Truy cập giá trị 20 từ tuple sau
# Ví dụ:
# x = (“ô tô kê”, [1, 20, 33], (5, 67, 88))

x = ("ô tô kê", [1, 20, 33], (5, 67, 88))
value = x[1][1]
print(value)


# *3. Tính số lần xuất hiện của số 5 trong tuple sau
# Ví dụ:
# x = (1, 3, 5, 6, 5, 55)

x = (1, 3, 5, 6, 5, 55)
count_5 = x.count(5)
print(count_5)

