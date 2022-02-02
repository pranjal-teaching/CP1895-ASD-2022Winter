from dataclasses import dataclass


@dataclass
class City:
    population: int
    name: str
    tax_rate: float

    def collect_taxes(self):
        return self.tax_rate * self.population


if __name__ == '__main__':
    st_johns = City(population=100000, name="St. John's", tax_rate=30)
