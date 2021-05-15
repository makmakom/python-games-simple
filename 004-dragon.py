import random
import time


def display_intro():
    print('''Вы находитесь в землях, заселенных драконами. 
Перед собой вы видите две пещеры. В одной из них — дружелюбный дракон,
который готов поделиться с вами своими сокровищами. Во второй —
жадный и голодный дракон, который мигом вас съест.''', end='\n\n')


def cave_choose():
    cave = 0
    while cave != 1 and cave != 2:
        print('В какую пещеру вы войдете? (нажмите клавишу 1 или 2)')
        cave = int(input())

    return cave


def cave_check(chosen_cave):
    print('Вы приближаетесь к пещере...')
    time.sleep(2)
    print('Ее темнота заставляет вас дрожать от страха...')
    time.sleep(2)
    print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...', end='\n\n')
    time.sleep(2)

    if chosen_cave == random.randint(1, 2):
        print('...делится с вами своими сокровищами!')
    else:
        print('...моментально вас съедает!')


playMore = 'да'
while playMore == 'да' or playMore == 'д':
    display_intro()
    cave_check(cave_choose())

    print('Попытаете удачу еще раз? (да или нет)')
    playMore = input()
