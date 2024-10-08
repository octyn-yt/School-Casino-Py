import random
import os
import time

## School Python Casino Project Made by Octyn-YT for 'Coding Challenge' Prep

def main_menu(please):
    print('Your balance is: ', please)
    cleanUp()
    gameChoice = input('What game would you like to play? "BlackJack" or "Lucky Slots?"')
    if gameChoice == 'BlackJack':
        blackjack(please)
    if gameChoice == 'Lucky Slots':
        slots(please)

def slots(please):
    cleanUp()
    bet = int(input('How much would you like to bet?'))
    please -= bet
    print('Get three in a row to win!')
    row1 = ['🍀','🎉','🍒','🎁','💰','🔔']
    row2 = ['🍀','🎉','🍒','🎁','💰','🔔']
    row3 = ['🍀','🎉','🍒','🎁','💰','🔔']

    option1 = random.choice(row1)
    option2 = random.choice(row2)
    option3 = random.choice(row3)

    print(option1, option2, option3)

    payout = bet * 6
    jackpot = bet *1200000

    if option1 != '🍀'and option1 == option2 == option3:
        print('You win a payout!', payout)
        please + payout
        print('Your balance is: ', please)
        main_menu(please)
    elif option1 == option2 == option3 and option1 == '🍀':
        print('YOU WIN THE MEGA JACKPOT!')
        please + jackpot
        print('Your balance is: ', please)
        main_menu(please)
    else:
        print('Nothing! :c')
        main_menu(please)


def blackjack(please):
    status1 = ''
    newCard = 0
    newdCard = 0
    print('''
    BlackJack
    ''')
    print('Only 2 max hits!!! Use them wisely')
    bet = int(input('How much would you like to bet? '))
    if bet > please or bet <= 0:
        print('Failed to bet. (You are too broke)')
        main_menu(please)
    else:
        ''
        please -= bet

    print('Choices are "hit", "stand" or "double" ')
    cards = [1,2,3,4,5,6,7,8,9,12,13,14,10,11]

    desire = 21

    newCardl = ''
    newdCardl = ''

    dCard1 = random.choice(cards)
    dCard2 = random.choice(cards)

    card1 = random.choice(cards)
    card2 = random.choice(cards)

    card1l = card1
    card2l = card2
    dCard2l = dCard2
    dCard1l = dCard1

    if card1 == 12:
        card1l = 'J'
        card1 = 10
    elif card1 == 13:
        card1l = 'Q'
        card1 = 10
    elif card1 == 14:
        card1l = 'K'
        card1 = 10
    elif card1 == 11:
        card1l = 'A'

    if dCard1 == 12:
        dCard1l = 'J'
        dCard1 = 10
    elif dCard1 == 13:
        dCard1l = 'Q'
        dCard1 = 10
    elif dCard1 == 14:
        dCard1l = 'K'
        dCard1 = 10
    elif dCard1 == 11:
        dCard1l = 'A'

    if card2 == 12:
        card2l = 'J'
        card2 = 10
    elif card2 == 13:
        card2l = 'Q'
        card2 = 10
    elif card2 == 14:
        card2l = 'K'
        card2 = 10
    elif card2 == 11:
        card2l = 'A'

    if dCard2 == 12:
        dCard2l = 'J'
        dCard2 = 10
    elif dCard2 == 13:
        dCard2l = 'Q'
        dCard2 = 10
    elif dCard2 == 14:
        dCard2l = 'K'
        dCard2 = 10
    elif dCard2 == 11:
        dCard2l = 'A'


    total1 = card1 + card2
    total2 = dCard2 + dCard1

    if total1 > desire:
        print('You are bust! (fail)')
        please = please / 6
        main_menu(please)
    else:
        print('You have: ',card1l, card2l)
        choice = input('Choose your choice: ')

        if choice == 'double':
            def checkDouble():
                if bet*2 > please:
                    print('Sorry you dont have enough! Quitting game...')
                    main_menu(please)
                else:
                    print('You have enough funds! Continuing!!!')
            checkDouble()
            newCard = random.choice(cards)
            newdCard = random.choice(cards)

            newCardl = newCard
            newdCardl = newdCard

            if newCard == 12:
                newCardl = 'J'
                newCard = 10
            elif newCard == 13:
                newCardl = 'Q'
                newCard = 10
            elif newCard == 14:
                newCardl = 'K'
                newCard = 10
            elif newCard == 11:
                newCardl = 'A'

            if newdCard == 12:
                newdCardl = 'J'
                newdCard = 10
            elif newdCard == 13:
                newdCardl = 'Q'
                newdCard = 10
            elif newdCard == 14:
                newdCardl = 'K'
                newdCard = 10
            elif newdCard == 11:
                newdCardl = 'A'

            if newCard > 0 or newdCard > 0:
                total1 = card1 + card2 + newCard
                total2 = dCard1 + dCard2 + newdCard
                print('You have: ', card1l, card2l, newCardl)
                if (desire - total1) < (desire - total2) and status1 != 'fail':
                    print('You are closest! (win)')
                    status1 = 'win'
                    please = please + bet * 6
                    main_menu(please)
                else:
                    print('You have lost :c')
                    please = please + bet / 6
                    main_menu(please)
            else:
                total1 = card1 + card2
                total2 = dCard1 + dCard2
                print('You have: ', card1l, card2l)
                if (desire - total1) < (desire - total2) and status1 != 'fail':
                    print('You are closest! (win)')
                    status1 = 'win'
                    please = please + bet * 6
                    main_menu(please)
                else:
                    print('You have lost :c')
                    please = please + bet / 6
            if total1 > desire:
                print('You are bust! (fail)')
                status1 = 'fail'
                please = please + bet / 6
                main_menu(please)

        elif choice == 'hit':
            newCard = random.choice(cards)
            newdCard = random.choice(cards)

            newCardl = newCard
            newdCardl = newdCard

            if newCard == 12:
                newCardl = 'J'
                newCard = 10
            elif newCard == 13:
                newCardl = 'Q'
                newCard = 10
            elif newCard == 14:
                newCardl = 'K'
                newCard = 10
            elif newCard == 11:
                newCardl = 'A'

            if newdCard == 12:
                newdCardl = 'J'
                newdCard = 10
            elif newdCard == 13:
                newdCardl = 'Q'
                newdCard = 10
            elif newdCard == 14:
                newdCardl = 'K'
                newdCard = 10
            elif newdCard == 11:
                newdCardl = 'A'

            if newCard > 0 or newdCard > 0:
                total1 = card1 + card2 + newCard
                total2 = dCard1 + dCard2 + newdCard
                print('You have: ', card1l, card2l, newCardl)
            else:
                total1 = card1 + card2
                total2 = dCard1 + dCard2
                print('You have: ', card1l, card2l)
            if total1 > desire:
                print('You are bust! (fail)')
                status1 = 'fail'
                please = please + bet / 6
                main_menu(please)
            elif total1 <= desire:
                print('You have: ', card1l, card2l, newCardl)
                choice = input('Choose your choice (hit or stand): ')
                if choice == 'hit':
                    if total1 > desire:
                        print('You are bust! (fail)')
                        status1 = 'fail'
                        please = please + bet / 6
                        main_menu(please)
                    elif total1 <= desire and (desire - total1) < (desire - total2):
                        print('Max hits')
                        print('You are closest! (win)')
                        status1 = 'win'
                        please = please + bet * 6
                        main_menu(please)
                    elif total1 <= desire and (desire - total1) > (desire - total2):
                        print('Max hits')
                        print('You aren\'t closest! (lose)')
                        please = please + bet / 6
                        main_menu(please)


        if choice == 'stand' and newCard <= 0:
            print('You have: ', card1l, card2l)
            print('Dealer has: ', dCard1l, dCard2l)
        else:
            print('You have: ', card1l, card2l, newdCardl)
            print('Dealer has: ', dCard1l, dCard2l, newdCardl)

        while choice == 'stand':
            if  total1 > desire and total2 > desire:
                print('You are both over 21 (fail)')
                status1 = 'fail'
                please = please + bet / 6
                main_menu(please)
            elif total1 > desire and total2 <= desire:
                print('You are over 21 (fail')
                status1 = 'fail'
                please = please + bet / 6
                main_menu(please)
            elif total2 > desire and total1 <= desire:
                print('Dealer is bust! (win)')
                status1 = 'win'
                please = please + bet * 6
                main_menu(please)
            elif (desire - total1) < (desire - total2) and status1 != 'fail':
                print('You are closest! (win)')
                status1 = 'win'
                please = please + bet * 6
                main_menu(please)
            else:
                print('fail')
                status1 = 'fail'
                please = please + bet / 6
                main_menu(please)

def cleanUp():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def menu_yep():
    cleanUp()
    print('####[Welcome to the PyCasino]####')
    please = int(input('Please give me all your life savings: £'))
    main_menu(please)

menu_yep()