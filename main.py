#MAin menu
import random
loop = True
accounts = []
for account in range(1, 21):
    rand_num = random.randint(1, 5001)
    accounts.append([rand_num])

while loop == True:
    print('\nMain Menu')
    print('\n1: Print Accounts')
    print('\n2: Deposit')
    print('\n3: Withdrawal')
    print('\n4: Count Under $2000')
    print('\n5: Generous Donor')
    print('\n6: Hacker Attack')
    print('\n7: Exit')
    selection = input('Enter Option #: ')

    if selection == '1':
        print('\nACCOUNT BALANCES')
        for account in accounts:
            print("Account " + str(accounts.index(account)) + ": $" + str(accounts[accounts.index(account)][0]))
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
                print(account)
