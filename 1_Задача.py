# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# ОТВЕТ: Первому  игроку  надо первым ходом забрать остаток от целочисленного деления
# имеющегося количества конфет на то, которое можно взять за 1 ход максимально + 1
# В дальнейшем первому игроку нужно повторять стратегию, хотя без калькулятора не всегда это удобно посчитать))))
# Пример :  2021 % ( 28 + 1 ) = 20 , первый игрок первым ходом должен взять 20 конфет.
# если вторым ходом второй игрок взял 10 конфет, то первый должен взять 28 + 1 - 10 = 19 и так далее..
# Это как реализовано в игре против компа, хотя я прау раз выиграл, видимо не совсем правильно работает(((((


from random import *
import os


welcome_text = ('В игре с конфетами участвуют два игрока.\n'
                'На столе лежит 2021 конфета.\n'
                'Берете их по очереди,\n'
                'причем, за один раз можно взять не больше 28 конфет.\n'
                'Выигрывает тот, кто последним ходом заберет все конфеты.\n')
print(welcome_text)

message = ['берите, Ваша очередь']


def player_vs_player():
    candies_total = 2021
    max_take = 28
    count = 0
    player_1 = input('\nКак Вас зовут?: ')
    player_2 = input('\nКак зовут Вашего соперника?: ')

    print(f'\nУважаемые {player_1} и {player_2} игра начинается !\n')
    print('\nДля начала опеределим, кто первый начнет игру.\n')

    x = randint(1, 2)
    if x == 1:
        lucky = player_1
        loser = player_2
    else:
        lucky = player_2
        loser = player_1
    print(f'Поздравляю {lucky} Вы ходите первым !')

    while candies_total > 0:
        if count == 0:
            step = int(input(f'\n{choice(message)} {lucky} = '))
            if step > candies_total or step > max_take:
                step = int(input(
                    f'\nМожно взять не более {max_take} конфет {lucky}, попробуте еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nосталось {candies_total}')
            count = 1
        else:
            print('Игра окончена')

        if count == 1:
            step = int(input(f'\n{choice(message)}, {loser} '))
            if step > candies_total or step > max_take:
                step = int(input(
                    f'\nМожно взять не более {max_take} конфет {loser}, попробуйте еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nосталось {candies_total}')
            count = 0
        else:
            print('Игра окончена')

    if count == 1:
        print(f'{loser} ПОБЕДИЛ')
    if count == 0:
        print(f'{lucky} ПОБЕДИЛ')


player_vs_player()


def player_vs_bot():
    candies_total = 2021
    max_take = 28
    player_1 = input('\nКак Вас зовут?: ')
    player_2 = 'Компьютер'
    players = [player_1, player_2]
    print(f'\nУважаемые {player_1} и {player_2} игра начинается !\n')
    print('\nДля начала опеределим, кто первый начнет игру.\n')


    lucky = randint(-1, 0)

    print(f'Поздравляю {players[lucky+1]} Вы ходите первым !')

    while candies_total > 0:
        lucky += 1

        if players[lucky % 2] == 'Компьютер':
            print(
                f'\nХодит {players[lucky%2]} \nНа кону {candies_total}. \n{choice(message)}: ')

            if candies_total < 29:
                step = candies_total
            else:
                delenie = candies_total//28
                step = candies_total - ((delenie*max_take)+1)
                if step == -1:
                    step = max_take -1
                if step == 0:
                    step = max_take
            while step > 28 or step < 1:
                step = randint(1,28)
            print(step)
        else:
            step = int(input(f'\nХодите,  {players[lucky%2]} \nНа кону {candies_total} {choice(message)}:  '))
            while step > max_take or step > candies_total:
                step = int(input(f'\nЗа один ход можно взять {max_take} конфет, попробуйте еще раз: '))
        candies_total = candies_total - step

    print(f'Осталось {candies_total} \nПобедил {players[lucky%2]}')

player_vs_bot()