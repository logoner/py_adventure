import random
# py_adventure config scrypt
# Стартовые навыки:
# базовые навыки игрока:
player_level = 1 # Уровень игрока
player_strength = 1 # Сила игрока
player_agility = 1 # Ловкость игрока
player_vitality = 1 # Живучесть игрока
player_intelligence = 1 # Интеллект игрока
player_luck = 1 # Удача игрока

# Скрытые навыки игрока (не доступны при старте):
player_wisdom = 0 # Мудрость игрока

# Статы
player_experience = 0 # Опыт
player_stealth = 0 # Скрытность игрока
location_danger = 0 # опасность локации
location_number = 0 # номер локации


# complex game parameters:
# basic danger (strength and power) of the enemy (danger of the place + random from 1 to 20):
base_enemy_danger = location_danger + (1 * random.randint(1, 20))

# The amount of experience required to move the player to the next level
experience_required = player_level * 100 + player_level * 5