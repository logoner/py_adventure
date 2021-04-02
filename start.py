# py_adventure start scrypt
import config
import screen
import random
import os

# мини игра для фана

# суть - бесконечная прокачка персонажа :)

# комплексные параметры игры:
# базовая опасность (сила и мощь) врага (опасность места + рандом от 1 до 20):
base_enemy_danger = config.location_danger + (1 * random.randint(1, 20))

# Количество опыта необходимое для перехода игрока на следующий уровень
# The amount of experience required to move the player to the next level
experience_required = config.player_level * 100 + config.player_level * 5

# Встреча
def new_meeting():
    meeting_took_place = bool(random.randint(0, 1))
    if meeting_took_place:
        return (meeting_took_place, 'Рядом с вами летает Тень призрака. Кого-то она вам напоминает.', 'Её стоит прогнать с дороги, только вот как?',)
    else:
        return (meeting_took_place, 'Рядом с вами никого нет. Где все?', 'Куда они подевались?')
        
# Отображаемое меню
def displayed_menu(displayed_screen):
    menu_options = [('Идти дальше - 1********', 'Оглядеться - 2*********', 'Проверить инвентарь - 3', 'Выход - 4**************'),
                    ('Атаковать - 1**********', 'Оглядеться - 2*********', 'Проверить инвентарь - 3', 'Выход - 4**************'),]
    return menu_options[displayed_screen]

# геймплей:
# продолжение игры
continuation_of_the_game = True

# game loop

# print('Вы оказались в необычном месте.')
# print('Пройдено километров:', config.location_number)

while continuation_of_the_game:
    meeting = new_meeting()
    screen.display_interface(config.location_number, meeting, displayed_menu(int(meeting[0])))
    menu = 0
    menu = input()
    if menu == '1': # Move on
        config.location_number = config.location_number + 1
        os.system('cls')  # For Windows
        print('Вы оказались в необычном месте.')
        print('Пройдено километров:', config.location_number)
        
        # Встреча
        print(new_meeting())        
        
    elif menu == '2': # search the location
        os.system('cls')  # For Windows
        print('Оглядевшись вы увидели...')
        print('Ничего. Ничего интересного.')
        print()
        
    elif menu == '3': # Check inventory
        os.system('cls')  # For Windows
        print('Пора проверить инвентарь!')
        print('Похоже сумка пуста... или её нет совсем. Где же она?')
        print()
        
    elif menu == '4': # Exit game
        os.system('cls')  # For Windows
        continue_game = input("Закончить игру? (Y/N): ")
        if continue_game == 'N':
            continuation_of_the_game = True
        else:
            continuation_of_the_game = False
            print('Игра закончена!')
            # Игра закончена
    else:
        os.system('cls')  # For Windows
        print('Похоже ничего не происходит...')
        print('Совсем ничего!')
        print()
    

print('test:')
# Текущие показатели

print('Пройдено километров:', config.location_number)
print('Текущее максимальное здоровье игрока:', 10 * config.player_vitality)
print('Текущий уровень игрока:', config.player_level) # Уровень игрока
print('Текущая сила игрока:', config.player_strength) # Сила игрока
print('Текущая ловкость игрока:', config.player_agility) # Ловкость игрока
print('Текущая живучесть игрока:', config.player_vitality) # Живучесть игрока
print('Текущий интеллект игрока:', config.player_intelligence) # Интеллект игрока
print('Текущая удача игрока:', config.player_luck) # Удача игрока

# Скрытые навыки игрока (не доступны при старте):
print('Текущая мудрость игрока (скрыто):', config.player_wisdom) # Мудрость игрока

# Статы
print('Текущий опыт игрока:', config.player_experience) # Опыт
print('Текущая скрытность игрока:', config.player_stealth) # Скрытность игрока
print('Текущая опасность локации:', config.location_danger) # опасность локации

print('Необходимо опыта игрока:', experience_required) # Количество опыта необходимое для перехода игрока на следующий уровень
print('Текущая опасность врагов:', base_enemy_danger) # базовая опасность (сила и мощь) врага
print()

