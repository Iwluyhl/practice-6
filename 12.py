print("Загадай число от 0 до 1000, а я его отгадаю!")
print("Отвечай так: '>' (число которое я загадал больше), '<' (число которое я загадал меньше) или '=' (угадано)")

low = 0
high = 1000
attempts = 0
guessed = False

while not guessed:

    mid = (low + high) // 2
    attempts += 1

    print(f"Попытка №{attempts}: Это число {mid}?")
    answer = input("Ваш ответ: ")

    if answer == '>':

        low = mid + 1
    elif answer == '<':
        high = mid - 1
    elif answer == '=':
        print(f"Ура! Я угадал за {attempts} попыток.")
        guessed = True
    else:
        print("Пожалуйста, используй только символы '>', '<' или '='.")

    if low > high:
        print("Кажется, вы где-то ошиблись в ответах. Такого числа не существует!")
        break