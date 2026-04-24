

n = abs(int(input("Введите число для проверки на неубывающий порядок: ")))
flag = False
last_digit = n // 10

while n > 0:
    digit = n % 10
    if digit > last_digit:
        flag = True
        break
    last_digit = digit
    n = n // 10
if flag:
    print("В числе убывающий порядок.")
else:
    print("В числе не убывающий порядок.")
