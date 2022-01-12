# Ask the user to enter fname, lname and age.
# store that info in a dict
# print that dict

user = {}
user['fname'] = input('Fname:')
user['lname'] = input('Lname:')
user['age'] = int(input('Age'))
print(user)

# allow user to update age
ch = input('Do you want to update age? (y/n)')
if ch == 'y':
    user['age'] = int(input('Age'))

