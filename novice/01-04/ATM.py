print('\nWelcome to Karepmu ATM')
print('\nPlease select your transaction')
print('press [1] Deposit \npress [2] Withdraw \npress [3] Balance \npress [4] Exit')

balance = 0
while True:
    choice = input('\nWhat would you like to press: ')
    if choice == '1':
        input_saldo = int(input('\nHow much money you want to deposit: '))
        action = input(f'Are you sure you want to deposit {input_saldo}? [y / n]: ')
        if action == 'y':
            print(f'\nCongratulation, {input_saldo} added to your balance')
            other_action = input('\nWant to make other transaction? [y / n] ')
            if other_action == 'y':
                balance += input_saldo
                continue
            elif other_action == 'n':
                break
            else:
                break
        if action == 'n':
            print('\nYour deposit canceled !!')
            other_action = input('\nWant to make other transaction? [y / n] ')
            if other_action == 'y':
                continue
            elif other_action == 'n':
                break
            else:
                break
    elif choice == '2':
        withdraw_balance = int(input('How much money you want to withdraw?'))
        action = (input(f'Are you sure withdraw {withdraw_balance}? [y / n] '))
        if action == 'y':
            print('\nPlease take your money')
            other_action = input('\nWant to make other transaction? [y / n] ')
            if other_action == 'y':
                balance -= withdraw_balance
                continue
            elif other_action == 'n':
                break
            else:
                break
        if action == 'n':
            print('\nYour withdrawn canceled !!')
            other_action = input('\nWant to make other transaction? [y / n] ')
            if other_action == 'y':
                continue
            elif other_action == 'n':
                break
            else:
                break
    elif choice == '3':
        action = input(f'\nYour balance: {balance} \nWant to make other transaction? [y / n] ')
        if action == 'y':
            continue
        elif action == 'n':
            break
        else:
            break
    elif choice == '4':
        action = input('\nAre you sure want to exit? [y / n] ')
        if action == 'y':
            print('\nThankyou for choosing us')
            break
        if action == 'n':
            other_action = choice
    else:
        print('Not in options!!!')
        break