import pickle

pranjal = {
    'first_name': 'Pranjal',
    'last_name': 'Patra',
    'age': 35,
    'NetWorth': 420.69,
    'Vaccinated': True
}

with open("pranjal.bin", 'wb') as pranjal_file:
    pickle.dump(pranjal, pranjal_file)

with open('pranjal.bin', 'rb') as pranjal_file:
    pranjal_from_bin_file = pickle.load(pranjal_file)

print(pranjal_from_bin_file)
