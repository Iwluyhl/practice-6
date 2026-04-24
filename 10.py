# Проверить, есть ли во введённом числе одинаковые цифры подряд.

n = abs(int(input("Введите число для проверки на одинаковые цифры подряд: ")))
duplicate = False
last_digit = n // 10

while n > 0:
    digit = n % 10
    if digit == last_digit:
        duplicate = True
        break
    last_digit = digit
    n = n // 10
if duplicate:
    print("В числе есть одинаковые цифры подряд.")
else:
    print("В числе нет одинаковых цифр подряд.")
