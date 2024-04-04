# *1. In ra giá trị của key ‘math’ từ dict sau đây
# Ví dụ:
# x = {
#     "class": {
#         "student": {
#             "name": "Tom",
#             "marks": {
#                 "history": 70,
#                 "math": 80
#             }
#         }
#     }
# }

x = {
    "class": {
        "student": {
            "name": "Tom",
            "marks": {
                "history": 70,
                "math": 80
            }
        }
    }
}

# Truy cập giá trị của key 'math'
math_score = x["class"]["student"]["marks"]["math"]
print(math_score)


# *2. Viết chương trình tạo ra 1 dict mới bằng việc lấy ra những keys.
# Ví dụ:
# x = {
#     "name": "John",
#     "age": 25,
#     "height": 180,
#     "city": "Hanoi"}

# muốn lấy ra keys “name”, và “height”

x = {
    "name": "John",
    "age": 25,
    "height": 180,
    "city": "Hanoi"
}

# Các keys cần lấy ra
selected_keys = ["name", "height"]

# Tạo từ điển mới chỉ chứa các keys đã chọn
new_dict = {key: value for key, value in x.items() if key in selected_keys}

print(new_dict)

# *3. Xóa keys từ 1 dict

# Ví dụ:
# x = {
#     "name": "John",
#     "age": 25,
#     "height": 180,
#     "city": "Hanoi"}

# muốn lấy ra keys “name”, và “height”

x = {
    "name": "John",
    "age": 25,
    "height": 180,
    "city": "Hanoi"
}

# Keys cần xóa
keys_to_delete = ["name", "height"]

# Tạo từ điển mới không chứa các keys đã xóa
new_dict = {key: value for key,
            value in x.items() if key not in keys_to_delete}

print(new_dict)


# *4. Viết chương trình kiểm tra xem giá trị 40 có trong dict không
# Ví dụ:
# x = {'a': 100, 'b': 20, 'c': 40}

x = {'a': 100, 'b': 20, 'c': 40}

# Kiểm tra xem giá trị 40 có trong từ điển không
if 40 in x.values():
    print("Số 40 có trong dict")
else:
    print("Số 40 không có trong dict")

# *5. Thay đổi giá trị “22” thành “32” trong dict sau
# Ví dụ
# x = {
#     'per1': {'name': 'A', 'age': 18},
#     'per2': {'name': 'B', 'age': 22},
#     'per3': {'name': 'C', 'age': 25}
# }

x = {
    'per1': {'name': 'A', 'age': 18},
    'per2': {'name': 'B', 'age': 22},
    'per3': {'name': 'C', 'age': 25}
}

# Thay đổi giá trị từ "22" thành "32"
x['per2']['age'] = 32

print(x)

# *6.
# Đếm số lần xuất hiện của đoạn str sau:
# Ví dụ:
# x = “Toi di tim toi de di tim hanh phuc”

x = "Toi di tim toi de di tim hanh phuc"

# Chuyển đổi chuỗi thành danh sách các từ
words = x.split()

# Khởi tạo một từ điển để lưu trữ số lần xuất hiện của từng từ
word_count = {}

# Đếm số lần xuất hiện của mỗi từ và lưu vào từ điển word_count
for word in words:
    word_count[word.lower()] = word_count.get(word.lower(), 0) + 1

print(word_count)

