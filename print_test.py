# py_adventure start scrypt
import os
import config
import random
import screen
import functions as func

# mini game for fun
# the essence is endless character pumping :)

# Meeting
new_meeting = func.new_meeting
#def new_meeting():
    
# Displayed menu
displayed_menu = func.displayed_menu

# gameplay:
# continuation of the game
continuation_of_the_game = True

def print_test():
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

    print('Необходимо опыта игрока:', config.experience_required) # Количество опыта необходимое для перехода игрока на следующий уровень
    print('Текущая опасность врагов:', config.base_enemy_danger) # базовая опасность (сила и мощь) врага
    print()
    os.system('pause')
    os.system('cls')  # For Windows