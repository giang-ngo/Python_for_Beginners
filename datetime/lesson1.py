from datetime import datetime


# Vd 1:In ra ngày và giờ hiện tại trong Python
# Lấy ngày và giờ hiện tại
now = datetime.now()

# In ra ngày và giờ hiện tại
print("Ngày và giờ hiện tại là:", now)


# Vd 2:Biến đổi string thành datetime
# Ví dụ: x =  "Mar 05 2023 3:30PM"
x =  "Mar 05 2023 3:30PM"

# Chuyển đổi chuỗi thành datetime
datetime = datetime.strptime(x, "%b %d %Y %I:%M%p")

# In ra đối tượng datetime đã chuyển đổi
print("Đối tượng datetime đã chuyển đổi:", datetime)


