import random

class Crop(object):
    """Our crop is going to be a simple one, it will require a certain amount of light and water and if it
receives sufficient amounts it will grow. As it grows it will develop from a seed to a mature crop"""
    growth = 0
    _days_growing = 0
    #_growth_rate
    light_need = 2
    water_need = 3
    _status = 'seed'
    _type = 'generic'
    _GROWTH_SCALE = {'Seed': 0, 'Seedling': 1, 'Young': 6, 'Mature': 11, 'Old': 16}

    def needs(self, light_need, water_need):
        # returns as dictionary the light_need and water_need of the crop
        self.light_need = 2
        self.water_need = 1
        return

    def report(self, _type, _status, _growth, _days_growing):
        # returns as dictionary what the type, status, growth and number of days_growing of the crop
        pass

    def _update_status(self, growth):
        if growth >= 1:
            return 'Seedling'
        elif growth >= 6:
            return 'Young'
        elif growth >= 11:
            return 'Mature'
        elif growth >= 16:
            return 'Old'
        else:
            return _status


def grow(have_light, have_water):
    if have_light >= Crop.light_need and have_water >= Crop.water_need:
        Crop.growth += 1
    return Crop.growth



def auto_grow(days):
    for i in range(1, days + 1):
        have_light = random.randint(1, 10)
        have_water = random.randint(1, 10)
        grow(have_light, have_water)
        i += 1


def manual_grow(have_light, have_water):
    crop.grow(have_light, have_water)




if __name__ == '__main__':
    print auto_grow(5)
    print Crop.growth

