def calculate_age():
    # Запрашиваем текущую дату
    current_date = input("Введите текущую дату в формате день/месяц/год: ")
    currentday, currentmonth, currentyear = map(int, current_date.split('/'))

    # Запрашиваем дату рождения
    birth_date = input("Введите дату рождения в формате день/месяц/год: ")
    day, month, year = map(int, birth_date.split('/'))

    # Проверяем корректность введённых дат
    if currentmonth < 1 or currentmonth > 12:
        print("Некорректный месяц текущей даты.")
        return
    if currentday < 1 or (currentmonth in [1, 3, 5, 7, 8, 10, 12] and currentday > 31) or (currentmonth in [4, 6, 9, 11] and current_day > 30):
        print("Некорректный день текущей даты.")
        return
    if currentmonth == 2:
        # Проверяем високосный год
        if (currentyear % 4 == 0 and currentyear % 100 != 0) or (currentyear % 400 == 0):
            if currentday > 29:
                print("Некорректный день для февраля в високосный год.")
                return
        else:
            if currentday > 28:
                print("Некорректный день для февраля.")
                return

    if month < 1 or month > 12:
        print("Некорректный месяц даты рождения.")
        return
    if day < 1 or (month in [1, 3, 5, 7, 8, 10, 12] and day > 31) or (month in [4, 6, 9, 11] and day > 30):
        print("Некорректный день даты рождения.")
        return
    if month == 2:
        # Проверяем високосный год для даты рождения
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day > 29:
                print("Некорректный день для февраля в високосный год.")
                return
        else:
            if day > 28:
                print("Некорректный день для февраля.")
                return
            
    # Вычисляем возраст
    age = currentyear - year
    if (currentmonth < month) or (currentmonth == month and currentday < day):
        age -= 1

    print(f"Ваш возраст: {age} лет.")

#vВызов функции
calculate_age()
