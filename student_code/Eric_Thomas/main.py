eric = {
    'first_name': 'Eric',
    'last_name': 'Thomas',
    'age': 34,
    'net_worth': 420.69,
    'vaccinated': True
}

print(eric)
print(eric['first_name'])
eric['age'] = 35
print(eric['age'])

eric['nationality'] = 'Canadian'
print(eric)

del eric['net_worth']
print(eric)