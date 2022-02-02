from dataclasses import dataclass

from city import City


@dataclass
class Province:
    name: str
    population: int
    cities: list
    capital: City

    def add_city(self, new_city):
        assert isinstance(new_city, City), 'New city must of type City'
        self.cities.append(new_city)

    def get_urban_population(self):
        total_urban_population = 0
        for city in self.cities:
            total_urban_population += city.population
        return total_urban_population

    def generate_funds(self):
        funds_collected = 0
        for city in self.cities:
            funds_collected += city.collect_taxes()
        return funds_collected


