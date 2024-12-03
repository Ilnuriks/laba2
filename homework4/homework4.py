import random

def find_multiples():
    # Генерация списка из 10 случайных чисел в диапазоне от 0 до 200
    numbers = [random.randint(0, 200) for _ in range(10)]
    print("Сгенерированные числа:", numbers)

    # Запрос цифры X у пользователя
    while True:
        try:
            x = int(input("Введите цифру X (от 1 до 9): "))
            if 1 <= x <= 9:
                break
            else:
                print("Пожалуйста, введите цифру от 1 до 9.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

    multiples = list(filter(lambda num: num % x == 0, numbers)) # Использование лямбда-функции для фильтрации чисел, кратных X

    # Вывод найденных чисел
    if multiples:
        print(f"Числа, кратные {x}: {multiples}")
    else:
        print(f"Нет чисел, кратных {x}.")

find_multiples() # Вызов функции