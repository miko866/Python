print ('Calculate the interest.')

interest = float(input('Enter the interest: '))
interest = interest / 100
num_years = int(input('Enter the number of years: '))
account_balance = float(input('Enter the account balance: '))


new_account_balance = account_balance * ( 1.0 + interest) ** num_years

print ('The new account balance is: ', new_account_balance)


