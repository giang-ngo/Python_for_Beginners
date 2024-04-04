# BT1:
# Viết chương trình cho phép người dùng nhập vào một số. Nếu người dùng nhập vào ko phải là một số thì in ra lỗi,
# và bắt người dùng nhập lại. Nếu người dùng nhập đúng số thì thoát chương trình

while True:
    try:
        number = float(input("Nhập vào một số: "))
        break  # Nếu người dùng nhập đúng số, thoát khỏi vòng lặp
    except ValueError:
        print("Lỗi: bạn đã nhập không phải là một số. Vui lòng nhập lại.")

print("Bạn đã nhập số:", number)


# BT2
# Cho người dùng nhập vào, số a, và số b. In ra thương của hai số đó. Xử lý lỗi: nếu lỗi ValueError,
# thì in ra “Nhập sai số, vui long nhập lại”,
# nếu lỗi ZeroDivisionError, thì in ra “Không chia được với số 0, vui lòng nhập lại”, và bắt người dùng nhập lại hai số.

while True:
    try:
        a = float(input("Nhập số a: "))
        b = float(input("Nhập số b: "))
        result = a / b
        print("Thương của hai số là:", result)
        break  # Thoát khỏi vòng lặp nếu không có lỗi
    except ValueError:
        print("Nhập sai số, vui lòng nhập lại.")
    except ZeroDivisionError:
        print("Không chia được với số 0, vui lòng nhập lại.")

