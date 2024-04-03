# Chỉ định kiểu trả về của tham số, hàm
import math


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    bound = int(math.sqrt(n))
    for i in range(2, bound + 1):
        if n % i == 0:
            return False
    return True


def get_full_name() -> str | None:
    name = input('Họ và tên: ')
    if len(name) > 0:
        return name
    else:
        return None


full_name = get_full_name()
print(full_name)
