n = int(input("Введите число для вычисления факториала: "))

if n < 0:
    print("Ошибка: Факториал отрицательного числа не существует.")
else:
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i

    print(f"Факториал числа {n} ({n}!) равен: {factorial}")