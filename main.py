# mini game for fun
# the essence is endless character pumping :)

# py_adventure start scrypt
import os
import config
import random
import screen
import functions as func
import print_test

new_meeting = func.new_meeting          # Meeting
displayed_menu = func.displayed_menu    # Displayed menu

# gameplay:
continuation_of_the_game = True         # continuation of the game

# game loop:

# Идея реализации в том, что в цикле меняется экран в зависимости от выбора Игрока. 
# Отображается экран соответствующий состоянию переменных отвечающих за 
# место игрока и текущее состояние игрока. Игроку на экране описываются 
# условия выбора, от выбора игрока меняется состояние переменных и новое
# отображение следующего по циклу экрана.

    # ВНИМАНИЕ!!! реализация данного цикла не соответствует заявленной выше идеи реализации!!!
    # Смотри файл py_adventure_todo
while continuation_of_the_game:
    meeting = new_meeting()
    # Отображение нового экрана консоли для Windows cmd
    screen.display_interface(config.location_number, meeting, displayed_menu(int(meeting[0])))
    

    # Atention!!! This module (enter the value of a user-selected menu) must be changed!
    menu = 0
    menu = input()
    if menu == '1': # Move on (Сделать функцию displayed_menu(menu) с параметром menu которая возвращает
                    # параметр для отображения экрана)
        config.location_number = config.location_number + 1
        os.system('cls')  # Очистка экрана консоли для Windows cmd
        
        print('Вы оказались в необычном месте.')
        print('Пройдено километров:', config.location_number)
        
        # Встреча
        print(new_meeting())        
        
    elif menu == '2': # search the location
        os.system('cls')  # Очистка экрана консоли для Windows cmd
        
        print('Оглядевшись вы увидели...')
        print('Ничего. Ничего интересного.')
        print()
        
    elif menu == '3': # Check inventory
        os.system('cls')  # Очистка экрана консоли для Windows cmd
        
        print('Пора проверить инвентарь!')
        print('Похоже сумка пуста... или её нет совсем. Где же она?')
        print()
        
    elif menu == '4': # Exit game
        os.system('cls')  # Очистка экрана консоли для Windows cmd
        
        continue_game = input("Закончить игру? (Y/N): ")
        if continue_game == 'N':
            continuation_of_the_game = True
        else:
            continuation_of_the_game = False
            print('Игра закончена!')
            # Игра закончена
    else:
        os.system('cls')  # Очистка экрана консоли для Windows cmd
        
        print('Похоже ничего не происходит...')
        print('Совсем ничего!')
        print()
    
print_test.print_test()