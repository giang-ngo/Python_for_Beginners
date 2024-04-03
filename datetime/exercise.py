from datetime import datetime, timedelta


# BT1: Trừ đi 49 ngày từ một ngày cho sẵn trong Python
# Ví dụ:
# x = datetime(2022, 12, 31)

# Ngày ban đầu
x = datetime(2022, 12, 31)

# Trừ đi 49 ngày
new_date = x - timedelta(days=49)

print("Ngày sau khi trừ đi 49 ngày là:", new_date)


# BT2: In ra ngày theo định dạng sau:
# Thứ ngày tháng năm
# (datetime obj có sẵn trong machine, muốn hiện thị dạng str ra ngoài thì dùng strftime)
# Ví dụ:
# x = datetime(2022, 2, 24)

# Ngày ban đầu
x = datetime(2022, 2, 24)

# Định dạng và in ra ngày theo yêu cầu
formatted_date = x.strftime("%A %d %B %Y")
print(formatted_date)

# BT3: Tìm thứ trong tuần của ngày sau
# Ví dụ:
# x = datetime(2022, 10, 30)

x = datetime(2022, 10, 30)


day_of_week = x.strftime("%A")

print("Thứ của ngày trong tuần:", day_of_week)


# BT4: Cộng thêm 10 ngày 12 giờ vào một ngày cho sẵn
# Ví dụ:
# x = datetime(2022, 10, 30)

# Ngày ban đầu
x = datetime(2022, 10, 30)

# Cộng thêm 10 ngày và 12 giờ
new_date = x + timedelta(days=10, hours=12)

print("Ngày sau khi cộng thêm 10 ngày 12 giờ là:", new_date)


# BT5: Biến đổi datetime theo định dạng sau
# Ví dụ:
# x = datetime(2022, 2, 24)


# Ngày ban đầu
x = datetime(2022, 2, 24)

# Biến đổi thành chuỗi theo định dạng yêu cầu
formatted_date = x.strftime("%Y-%m-%d %H:%M:%S")

print("Biến đổi datetime thành chuỗi theo định dạng:", formatted_date)

# BT6:Tính số ngày  chiến sự  Nga -  Uknaina nổ ra tính tới thời điểm đề  cập
# (future date > past date)
# Ví dụ:
# x = datetime(2022, 2, 24)
# y = datetime(2022, 8, 20)


# Ngày ban đầu
x = datetime(2022, 2, 24)
y = datetime(2022, 8, 20)

# Tính số ngày giữa hai ngày
days = abs((y - x).days)

print("Số ngày giữa hai ngày là:", days)
