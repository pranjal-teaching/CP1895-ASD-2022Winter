# create a dict
pranjal = {
    'first_name': 'Pranjal',
    'last_name': 'Patra',
    'age': 35,
    'NetWorth': 420.69,
    'Vaccinated': True
}


# how to print
print(pranjal)

# how to access a single value using the key
print(pranjal['first_name'])

# how to change a value in a dict
pranjal['age'] = 36
print(pranjal)

# how to add key-value pairs to existing dict
pranjal['nationality'] = 'Indian'
print(pranjal)

# delete key-value pair from a dict
del pranjal['NetWorth']
print(pranjal)

