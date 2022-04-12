# py_adventure functions
import random

# Meeting
def new_meeting():
    meeting_took_place = bool(random.randint(0, 1))
    if meeting_took_place:
        return (meeting_took_place, 'Рядом с вами летает Тень призрака. Кого-то она вам напоминает.', 'Её стоит прогнать с дороги, только вот как?',)
    else:
        return (meeting_took_place, 'Рядом с вами никого нет. Где все?', 'Куда они подевались?')
        
# Displayed menu
def displayed_menu(displayed_screen):
    menu_options = [('Идти дальше - 1********', 'Оглядеться - 2*********', 'Проверить инвентарь - 3', 'Выход - 4**************'),
                    ('Атаковать - 1**********', 'Оглядеться - 2*********', 'Проверить инвентарь - 3', 'Выход - 4**************'),]
    return menu_options[displayed_screen]
