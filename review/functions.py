def restaurant_bouncer(age:int, fully_vaxed:bool = False) -> bool:
    """
    checks if the person is allowed to enter restaurant or not.
    raises exception if age <= 0 and not int
    raises exception if fully_vaxed is not a bool
    :param age: (int) age of the individual
    :param fully_vaxed: (bool) vaccination status, default is False
    :return: (bool) True if allowed else False
    """
    assert isinstance(age, int), 'age must be an int'
    assert isinstance(fully_vaxed, bool), 'fully_vaxed must be a bool'
    assert age >= 0, 'age cannot be negative'
    if fully_vaxed or age < 18:
        print('Allowed to enter restaurant')
        return True
    else:
        print('Sorry, not allowed in')
        return False


while True:
    try:
        age = int(input('Enter Age'))
        vaccine_count = int(input('Enter vaccines taken: '))
        if vaccine_count >= 2:
            double_vaccinated = True
        restaurant_bouncer(age, double_vaccinated)
        break
    except Exception as e:
        print(e)
