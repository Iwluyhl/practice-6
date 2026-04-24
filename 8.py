n = int(input("Введите целое число: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")