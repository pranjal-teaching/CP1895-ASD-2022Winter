def restaurant_bouncer(age:int, fully_vaxed:bool = False) -> bool:
    """
    checks if the person is allowed to enter restaurant or not.
    :param age: (int) age of the individual
    :param fully_vaxed: (bool) vaccination status
    :return: (bool) True if allowed else False
    """
    if fully_vaxed or age < 18:
        print('Allowed to enter restaurant')
        return True
    else:
        print('Sorry, not allowed in')
        return False

# print(help(restaurant_bouncer))
# restaurant_bouncer(20, True)
# restaurant_bouncer(4, False)
# restaurant_bouncer(60, True)


restaurant_bouncer('60', 3.14)
