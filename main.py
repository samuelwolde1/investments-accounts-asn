#MAin menu
import random
loop = True
accounts = []
for account in range(20):
    rand_num = random.randint(1, 5001)
    accounts.append([rand_num])

while loop == True:
    print('Main Menu')
    print('\n1: Print Accounts')
    print('\n2: Deposit')
    print('\n3: Withdrawal')
    print('\n4: Count Under $2000')
    print('\n5: Generous Donor')
    print('\n6: Hacker Attack')
    print('\n7: Exit')
    selection = input('Enter Option #: ')

    if selection == '1':
        for account in accounts:
            print("Account " + str(accounts.index(account)) + ": $" + str(accounts[accounts.index(account)]))
    elif selection == '2':
        print('\nDEPOSIT')
        account_selection = input('Enter the acount number: ')
        deposit_amount = input('Enter amount to deposit: $')
        print('Account ' + str(account_selection) + ' Previous Balance: $'  + str(accounts[int(account_selection)][0]))
        print('Account ' + str(account_selection) + ' New Balance: $'  + str(accounts[int(account_selection)][0] + int(deposit_amount)))
    elif selection == '3':
        print('\nWITHDRAWAL')
        account_number = input('Enter account #: ')
        withdrawal_amount = input('Enter amount to withdraw: $')
        if accounts[int(account_number)][0] < int(withdrawal_amount):
            print('Sorry, insufficient funds.')
        else:
            print('Account ' + str(account_number) + ' Previous Balance: $'  + str(accounts[int(account_number)][0]))
            print('Account ' + str(account_number) + ' New Balance: $'  + str(accounts[int(account_number)][0] - int(withdrawal_amount)))
    elif selection == '4':
        for account in accounts:
            if accounts[accounts.index(account)][0] < 2000:
                print('Account ' + str(accounts.index(account)) + ": $" + str(accounts[accounts.index(account)][0]))
    elif selection == '5':
        for account in accounts:
            if accounts[accounts.index(account)][0] < 2000:
                new_account_bal = int(accounts[accounts.index(account)][0]) + 500
                print('Account ' + str(accounts.index(account)) + " Previous Balance: $" + str(accounts[accounts.index(account)][0]))
                print('Account ' + str(accounts.index(account)) + " New Balance: $" + str(new_account_bal))
                
    elif selection == '6':
        hacker_bal = 0
        print('Hacker Attack')
        for account in accounts:
            new_bal = int(accounts[accounts.index(account)][0]) * 0.05
            hacker_bal += new_bal
        print('Total stolen is: $' + str(hacker_bal))                  
    elif selection == '7':
        exit()
        