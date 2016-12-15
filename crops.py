import random
from animals import Cow, Sheep

class Crop(object):

    GROWTH_SCALE = {
        'Seed': lambda growth: growth == 0,
        'Seedling': lambda growth: 0 < growth <= 5,
        'Young': lambda growth: 5 < growth <= 10,
        'Mature': lambda growth: 10 < growth <= 15,
        'Old': lambda growth: growth > 15
    }

    def __init__(self, growth_rate, light_need, water_need):
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._type = 'generic'
        self._status = 'seed'

    def needs(self):
        return {'light_need': self._light_need, 'water need': self._water_need}

    def report(self):
        return {
            'type': self._type,
            'status': self._status,
            'growth': self._growth,
            'days growing': self._days_growing
        }

    def _update_status(self):
        if self.GROWTH_SCALE['Seed'](self._growth):
            self._status = 'Seed'
        elif self.GROWTH_SCALE['Seedling'](self._growth):
            self._status = 'Seedling'
        elif self.GROWTH_SCALE['Young'](self._growth):
            self._status = 'Young'
        elif self.GROWTH_SCALE['Mature'](self._growth):
            self._status = 'Mature'
        elif self.GROWTH_SCALE['Old'](self._growth):
            self._status = 'Old'

    def grow(self, light, water):
        if water >= self._water_need and light >= self._light_need:
            self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()

def auto_grow(crop, number_of_days):
    for _ in range(number_of_days):
        light = random.randint(1, 10)
        water = random.randint(1, 10)
        crop.grow(light, water)

def manual_grow(crop):
    is_valid = False
    while not is_valid:
        try:
            input_value = raw_input('Please enter a light value (1-10): ')
            light = int(input_value)
            if 1 <= light <= 10:
                is_valid = True
            else:
                print('{} is not a valid option. Please choose from 1 to 10'.format(input_value))
        except Exception:
            print('{} is not a valid option. Please choose from 1 to 10'.format(input_value))
    is_valid = False
    while not is_valid:
        try:
            input_value = raw_input('Please enter a water value (1-10): ')
            water = int(input_value)
            if 1 <= water <= 10:
                is_valid = True
            else:
                print('{} is not a valid option. Please choose from 1 to 10'.format(input_value))
        except Exception:
            print('{} is not a valid option. Please choose from 1 to 10'.format(input_value))
    crop.grow(light, water)

def display_menu(): 
    print('1. Grow manually over 1 day')
    print('2. Grow automatically over 30 days')
    print('3. Report status')
    print('4. Exit test program')
    print('Please select option from the above menu')

def instatiate_crop():
    is_valid = False
    while not is_valid:
        print('Please choose the crop or animal from available tupes:')
        print('1. Wheat')
        print('2. Potato')
        print('3. Cow')
        print('4. Sheep')
        input_value = raw_input('Option selected: ')
        if input_value.isdigit() and int(input_value) in (1, 2, 3, 4):
            is_valid = True
        else:
            print('{} is not a valid option. Please choose from 1 to 4'.format(input_value))
    if int(input_value) == 1:
        return Wheat(3, 4, 4)
    if int(input_value) == 2:
        return Potato(4, 3, 3)
    if int(input_value) == 3:
        return Cow('Star')
    if int(input_value) == 4:
        return Sheep('Vasya')

def get_menu_choice():
    is_valid = False
    while not is_valid:
        try:
            input_value = raw_input('Option selected: ')
            choice = int(input_value)
            if 1 <= choice <= 4:
                is_valid = True
            else:
                print('{} is not a valid option. Please choose from 1 to 4'.format(input_value))
        except Exception:
            print('{} is not a valid option. Please choose from 1 to 4'.format(input_value))
    return choice

def manage_crop(crop):
    print('This is a crop management program')
    print('________________________________________________________________')
    no_exit = True
    while no_exit:
        display_menu()
        option = get_menu_choice()
        if option == 1:
            manual_grow(crop)
        elif option == 2:
            auto_grow(crop, 30)
        elif option == 3:
            print(crop.report())
        elif option == 4:
            no_exit = False
        print('________________________________________________________________')
    print('Thank you for using our crop management program')

class Wheat(Crop):
    def __init__(self, growth_rate, light_need, water_need):
        self._growth = 0
        self._days_growing = 0
        self._type = 'wheat'
        self._growth_rate = growth_rate
        self._status = 'seed'
        self._light_need = light_need
        self._water_need = water_need

    def _update_status(self):
        previous_status = self._status
        super(Wheat, self)._update_status()
        if previous_status is not self._status:
            if self._status == 'Seedling':
                self._growth_rate *= 1.5
            elif self._status == 'Young':
                self._growth_rate *= 1.25
            elif self._status == 'Old':
                self._growth_rate *= 0.5
            else:
                self._growth_rate *= 1

class Potato(Crop):
    def __init__(self, growth_rate, light_need, water_need):
        self._growth = 0
        self._days_growing = 0
        self._type = 'potato'
        self._growth_rate = growth_rate
        self._status = 'seed'
        self._light_need = light_need
        self._water_need = water_need

    def _update_status(self):
        previous_status = self._status
        super(Potato, self)._update_status()
        if previous_status is not self._status:
            if self._status == 'Seedling':
                self._growth_rate *= 1.5
            elif self._status == 'Young':
                self._growth_rate *= 1.25

if __name__ == '__main__':
    my_crop = instatiate_crop()
    manage_crop(my_crop)