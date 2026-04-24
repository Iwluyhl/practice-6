n = int(input("Введите число которое хотите перевернуть: "))
reserved_num = 0

while n > 0:
    digit = n % 10
    reserved_num = (reserved_num * 10) + digit
    n = n // 10
print("Результат", reserved_num)