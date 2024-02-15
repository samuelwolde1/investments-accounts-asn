#MAin menu
import random
loop = True
accounts = []
for account in range(1, 21):
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
        print('Deposit')
        account_selection = input('Enter the acount number: ')
        deposit_amount = input('Enter amount to deposit: $')
        print('Account ' + str(accounts.index(account_selection)) + (' Previous Balance: ' + str(accounts[account_selection])))

        