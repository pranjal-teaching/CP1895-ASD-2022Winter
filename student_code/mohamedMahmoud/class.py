class LightBulb:
    def __init__(self, wattage, is_led, brand_name, is_on):
        self.wattage = wattage
        self.is_led = is_led
        self.brand_name = brand_name
        self.is_on = is_on

    def turn_off(self):
        self.is_on = False
        print(f'light is off')

    def turn_on(self):
        self.is_on = True
        print("light is on")

    def it_is_led(self):
        self.is_led = True
        print("light is led")

    def to_string(self):
        print(f'{self.wattage} {self.brand_name} {self.is_on} {self.is_led}')

    def set_brightness(self):
        level = input("enter brightness level from 0-10")
        if level in range(0, 11):
            print(f'level set to {level}')
        else:
            print(" please enter level from 0-10")


light = LightBulb(100, True, "led", False)

light.turn_off()

light.it_is_led()

light.set_brightness()
