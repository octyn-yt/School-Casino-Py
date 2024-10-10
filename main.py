import random
import os
import time

## School Python Casino Project Made by Octyn-YT for 'Coding Challenge' Prep

def main_menu(please):
    print('Your balance is: ', please)
    time.sleep(5)
    cleanUp()
    gameChoice = input('What game would you like to play? "BlackJack", "Roulette", "Horse Racing" or "Lucky Slots?"')
    if gameChoice == 'BlackJack':
        blackjack(please)
    elif gameChoice == 'Lucky Slots':
        slots(please)
    elif gameChoice == 'Roulette':
        roulette(please)
    elif gameChoice == 'Horse Racing':
        horserace(please)
    elif gameChoice == 'Failure':
        rRoulette(please)
    else:
        exit()

def horserace(please):
    cleanUp()
    bet = int(input('How much would you like to bet? '))
    if bet > please or bet <= 0:
        print('Failed to bet. (You are too broke)')
        main_menu(please)
    else:
        ''
        please -= bet

    payOption = [2,3,4,5,6,7]
    paySelect = random.choice(payOption)
    win = bet * paySelect

    print('''
    Horse 1
    Horse 2
    Horse 3
    Horse 4
    Horse 5
    ''')
    horses = [1, 2, 3, 4, 5]
    horseChosen = random.choice(horses)
    horseChoice = int(input('Pick a horse\'s number to bet on: '))
    print('Racing....')
    time.sleep(10)
    if horseChosen == horseChoice:
        please += win
        print('You won: ', win)
        main_menu(please)
    else:
        print('You lose.')
        main_menu(please)


def roulette(please):
    cleanUp()
    bet = int(input('How much would you like to bet? '))
    if bet > please or bet <= 0:
        print('Failed to bet. (You are too broke)')
        main_menu(please)
    else:
        ''
        please -= bet
    numberRoulette = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,40,31,32,33,34,35,36]
    IOChoose = input('Inside or Outside? ')
    if IOChoose == 'Inside':
        insideBet = input('Straight \n[Others removed due to issues.]')

    elif IOChoose == 'Outside':
        outsideBet = input('1-18,19-36,Red,Black,Even,Odd,Dozen,Column,Snake')
    print('Spinning Wheel....')
    time.sleep(4)
    print('Spinning Ball.....')
    time.sleep(10)
    win = bet * 2
    chosenRoulette = random.choice(numberRoulette)
    if IOChoose == 'Outside':
        if outsideBet == '1-18':
            if chosenRoulette >= 1 and chosenRoulette <= 18:
                please + win
                print('You have won: ',win)
                main_menu(please)
            else:
                print('You have lost :c')
                main_menu(please)
        elif outsideBet == '19-36':
                if chosenRoulette >= 19 and chosenRoulette <= 36:
                    please + win
                    print('You have won: ', win)
                    main_menu(please)
                else:
                    print('You have lost :c')
                    main_menu(please)
        elif outsideBet == 'Red':
            if chosenRoulette == 1 or chosenRoulette == 3 or chosenRoulette == 5 or chosenRoulette ==7 or chosenRoulette == 9 or chosenRoulette == 12 or chosenRoulette == 14 or chosenRoulette == 16 or chosenRoulette == 18 or chosenRoulette == 19 or chosenRoulette == 21 or chosenRoulette == 23 or chosenRoulette == 25 or chosenRoulette == 27 or chosenRoulette == 30 or chosenRoulette == 32 or chosenRoulette == 34 or chosenRoulette == 36:
                please + win
                print('You have won: ',win)
                main_menu(please)
            else:
                print('You have lost :c')
                main_menu(please)
        elif outsideBet == 'Black':
            if chosenRoulette != 1 or chosenRoulette != 3 or chosenRoulette != 5 or chosenRoulette !=7 or chosenRoulette != 9 or chosenRoulette != 12 or chosenRoulette != 14 or chosenRoulette != 16 or chosenRoulette != 18 or chosenRoulette != 19 or chosenRoulette != 21 or chosenRoulette != 23 or chosenRoulette != 25 or chosenRoulette != 27 or chosenRoulette != 30 or chosenRoulette != 32 or chosenRoulette != 34 or chosenRoulette != 36:
                please + win
                print('You have won: ',win)
                main_menu(please)
            else:
                print('You have lost :c')
                main_menu(please)
        elif outsideBet == 'Even':
            if chosenRoulette % 2 == 0:
                please + win
                print('You have won: ', win)
                main_menu(please)
            else:
                print('You have lost :c')
                main_menu(please)
        elif outsideBet == 'Odd':
            if chosenRoulette % 2 != 0:
                please + win
                print('You have won: ', win)
                main_menu(please)
            else:
                print('You have lost :c')
                main_menu(please)
        elif outsideBet == 'Dozen':
            DozenNum = input('1-12, 13-24 or 25-36')
            if DozenNum == '1-12':
                if chosenRoulette in range(1, 12):
                    please + win
                    print('You have won: ', win)
                    main_menu(please)
                else:
                    print('You have lost :c')
                    main_menu(please)
            elif DozenNum == '13-24':
                if chosenRoulette in range(13, 24):
                    please + win
                    print('You have won: ', win)
                    main_menu(please)
                else:
                    print('You have lost :c')
                    main_menu(please)
            elif DozenNum == '25-36':
                if chosenRoulette in range(25, 36):
                    please + win
                    print('You have won: ', win)
                    main_menu(please)
                else:
                    print('You have lost :c')
                    main_menu(please)
        elif outsideBet == 'Column':
            whichColumn = int(input('Column 1, 2 or 3?'))
            if whichColumn == 1:
                if chosenRoulette == 1 or chosenRoulette == 4 or chosenRoulette == 7 or chosenRoulette == 10 or chosenRoulette == 13 or chosenRoulette == 16 or chosenRoulette == 19 or chosenRoulette == 22 or chosenRoulette == 25 or chosenRoulette == 28 or chosenRoulette == 31 or chosenRoulette == 34:
                    please + win
                    print('You have won: ', win)
                    main_menu(please)
                else:
                    print('You have lost: ')
                    main_menu(please)
            elif whichColumn == 2:
                if chosenRoulette == 2 or chosenRoulette == 5 or chosenRoulette == 8 or chosenRoulette == 11 or chosenRoulette == 14 or chosenRoulette == 17 or chosenRoulette == 20 or chosenRoulette == 23 or chosenRoulette == 26 or chosenRoulette == 29 or chosenRoulette == 32 or chosenRoulette == 35:
                    please + win
                    print('You have won: ', win)
                    main_menu(please)
                else:
                    print('You have lost: ')
                    main_menu(please)
            elif whichColumn == 3:
                if chosenRoulette == 3 or chosenRoulette == 6 or chosenRoulette == 9 or chosenRoulette == 12 or chosenRoulette == 15 or chosenRoulette == 18 or chosenRoulette == 21 or chosenRoulette == 24 or chosenRoulette == 27 or chosenRoulette == 30 or chosenRoulette == 33 or chosenRoulette == 36:
                    please + win
                    print('You have won: ', win)
                    main_menu(please)
                else:
                    print('You have lost: ')
                    main_menu(please)
        elif outsideBet == 'Snake':
            if chosenRoulette == 1 or chosenRoulette == 5 or chosenRoulette == 9 or chosenRoulette == 12 or chosenRoulette == 14 or chosenRoulette == 16 or chosenRoulette == 19 or chosenRoulette == 23 or chosenRoulette == 27 or chosenRoulette == 30 or chosenRoulette == 32 or chosenRoulette == 34:
                please + win
                print('You have won: ', win)
                main_menu(please)
            else:
                print('You have lost')
                main_menu(please)
    elif IOChoose == 'Inside':
        if insideBet == 'Straight':
            yourChoice = int(input('Pick a number (0-36): '))
            if yourChoice == chosenRoulette:
                please + win
                print('You have won: ', win)
                main_menu(please)
            else:
                print('You have lost')
                print('The number was: ', chosenRoulette)
                main_menu(please)

def slots(please):
    cleanUp()
    bet = int(input('How much would you like to bet? '))
    if bet > please or bet <= 0:
        print('Failed to bet. (You are too broke)')
        main_menu(please)
    else:
        ''
        please -= bet

    print('Get three in a row to win!')
    row1 = ['ð','ð','ð','ð','ð°','ð']
    row2 = ['ð','ð','ð','ð','ð°','ð']
    row3 = ['ð','ð','ð','ð','ð°','ð']

    option1 = random.choice(row1)
    option2 = random.choice(row2)
    option3 = random.choice(row3)

    print(option1, option2, option3)

    payout = bet * 6
    jackpot = bet *1200000

    if option1 != 'ð'and option1 == option2 == option3:
        print('You win a payout!', payout)
        please + payout
        print('Your balance is: ', please)
        main_menu(please)
    elif option1 == option2 == option3 and option1 == 'ð':
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

def rRoulette(please):
    cleanUp()
    bet = int(input('How much would you like to bet? '))
    if bet > please or bet <= 0:
        print('Failed to bet. (You are too broke, maybe get a loan?)')
        main_menu(please)
    else:
        ''
        please -= bet

    shells = [1,2,3,4,5,6]
    shell1 = random.choice(shells)
    shell2 = random.choice(shells)

    win = bet * 99999999999999999999999999999999999999999

    print('Spinning....')
    shellChoice = random.choice(shells)
    print('Pulling...')
    if shellChoice == shell1 or shellChoice == shell2:
        print('Congrats, now run with the money!!!')
        please += win
        main_menu(please)
    else:
        print('Whats that sound...')
        exit()

def menu_yep():
    cleanUp()
    print('####[Welcome to the PyCasino]####')
    please = int(input('Please give me all your life savings: Â£'))
    main_menu(please)

menu_yep()