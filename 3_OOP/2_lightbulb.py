class LightBulb:
    def __init__(self, watt:int, is_led:bool, brand:str, is_on:bool = False, brightness:int = 0):
        self.wattage = watt
        self.is_led = is_led
        self.brand = brand
        self.is_on = is_on
        self.brightness = brightness

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_brightness(self, level):
        assert 0 <= level <= 10, 'Level outside bounds'
        self.brightness = level

    def to_string(self):
        print(f'I am a lighbulb. Made by {self.brand}. My wattage is {self.wattage} watts')

my_lbulb = LightBulb(6, True, 'Phillips')
my_lbulb.to_string()