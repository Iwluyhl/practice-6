number = int(input("Введите целое число: "))

n = abs(number)

if n == 0:
    count = 1
    total_sum = 0
else:
    count = 0
    total_sum = 0

    while n > 0:
        digit = n % 10
        total_sum += digit
        count += 1
        n = n // 10

print(f"В числе {number}:")
print(f"Количество цифр: {count}")
print(f"Сумма цифр: {total_sum}")
print(123//10)
print(123%10)