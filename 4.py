start_c = int(input("Введите начальную температуру в градусах Цельсия: "))
end_c = int(input("Введите конечную температуру в градусах Цельсия: "))
step = int(input("Введите шаг: "))
sum = 0

print("-" * 33)
print(f"| {'Цельсий (°C)':^12} | {'Фаренгейт (°F)':^10} |")
print("-" * 33)

for celsius in range(start_c, end_c + 1, step):

    fahrenheit = celsius * 1.8 + 32

    print(f"| {celsius:>12} | {fahrenheit:>14.1f} |")

# 4. Закрывающая линия
print("-" * 33)
