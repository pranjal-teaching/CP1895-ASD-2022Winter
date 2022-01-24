def how_many(a_dict):
    total = 0
    for item in a_dict.values():
        total += len(item)
    return total


def main():
    animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey']}
    animals['d'].append('dog')
    animals['d'].append('dingo')
    total = how_many(animals)
    print(total)


if __name__ == "__main__":
    main()
