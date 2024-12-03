import random

def get_computer_choice():
    """Функция для выбора компьютером камня, ножниц или бумаги."""
    choices = ['камень', 'ножницы', 'бумага']
    return random.choice(choices)

def get_user_choice():
    """Функция для получения выбора пользователя."""
    user_input = input("Введите 'камень', 'ножницы' или 'бумага': ").lower()
    while user_input not in ['камень', 'ножницы', 'бумага']:
        print("Неверный ввод. Попробуйте снова.")
        user_input = input("Введите 'камень', 'ножницы' или 'бумага': ").lower()
    return user_input

def determine_winner(user_choice, computer_choice):
    """Функция для определения победителя."""
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
        (user_choice == 'ножницы' and computer_choice == 'бумага') or \
        (user_choice == 'бумага' and computer_choice == 'камень'):
        return "Вы выиграли!"
    else:
        return "Компьютер выиграл!"

def play_game():
    """Основная функция игры."""
    print("Добро пожаловать в игру 'Камень-Ножницы-Бумага'!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"Вы выбрали: {user_choice}")
        print(f"Компьютер выбрал: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
        if play_again != 'да':
            break

if __name__ == "__main__":
    play_game()
