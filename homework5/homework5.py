
def get_number():
    for num in range(30):
        if num % 2 != 0:  # Проверяем, является ли число нечётным
            yield num  # Возвращаем нечётное число

# Создаем генератор
odd_numbers = get_number()

# Ищем первое, пятое и последнее значения
first = None
fifth = None
last = None

for i, num in enumerate(odd_numbers):
    if first is None:
        first = num
    if i == 4:  # Пятое значение (индекс 4)
        fifth = num
    last = num  # Обновляем последнее значение

print(f"Первое нечётное число: {first}")
print(f"Пятое нечётное число: {fifth}")
print(f"Последнее нечётное число: {last}")
