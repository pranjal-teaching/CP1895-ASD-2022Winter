#In [1]:
animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
animals['d'] = 'donkey'

#coati
print(animals['c'])

#error
#print(animals['donkey'])

#4
print(len(animals))

#anteater
animals['a'] = 'anteater'
print(animals['a'])

#8
print(len(animals['a']))

#False
print('baboon' in animals)

#True
print('donkey' in animals.values())

#True
print('b' in animals)

#dict_keys(['a', 'b', 'c', 'd'])
print(animals.keys())

#3
del animals['b']
print(len(animals))

#dict_values(['anteater', 'coati', 'donkey'])
print(animals.values())
