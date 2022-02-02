from province import Province
from city import City

st_johns = City(population=100000, name="St. John's", tax_rate=30)
corner_brook = City(population=30000, name='Corner Brook', tax_rate=25)
nl = Province(name="Newfoundland and Labrador",
              population=500000,
              cities=[st_johns, corner_brook],
              capital=st_johns)

print(nl.generate_funds())
print(nl.get_urban_population())


mt_pearl = City(population=25000, name="Mt. Pearl", tax_rate=28)
nl.add_city(mt_pearl)

print(nl.generate_funds())
print(nl.get_urban_population())

# nl.add_city('Stephenville')