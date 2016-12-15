class Animal(object):

    GROWTH_SCALE = {
        'Born': lambda weight: weight == 1,
        'Baby': lambda weight: 1 < weight <= 10,
        'Child': lambda weight: 10 < weight <= 20,
        'Young': lambda weight: 20 < weight <= 35,
        'Mature': lambda weight: 35 < weight <= 50,
        'Old': lambda weight: weight > 50,
    }

    def __init__(self, name, growth_rate, food_need, water_need):
        self._weight = 1
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._type = 'generic'
        self._status = 'born'
        self.name = name

    def needs(self):
        return {'food_need': self._food_need, 'water need': self._water_need}

    def report(self):
        return {
            'type': self._type,
            'name': self.name,
            'status': self._status,
            'weight': self._weight,
            'days growing': self._days_growing
        }

    def grow(self, food, water):
        if water >= self._water_need and food >= self._food_need:
            self._weight += self._growth_rate
        self._days_growing += 1
        self._update_status()

    def _update_status(self):
        if self.GROWTH_SCALE['Born'](self._weight):
            self._status = 'Born'
        elif self.GROWTH_SCALE['Baby'](self._weight):
            self._status = 'Baby'
        elif self.GROWTH_SCALE['Child'](self._weight):
            self._status = 'Child'
        elif self.GROWTH_SCALE['Young'](self._weight):
            self._status = 'Young'
        elif self.GROWTH_SCALE['Mature'](self._weight):
            self._status = 'Mature'
        elif self.GROWTH_SCALE['Old'](self._weight):
            self._status = 'Old'

class Cow(Animal):
    def __init__(self, name):
        super(Cow, self).__init__(name, 3, 5, 4)
        self._type = 'Cow'

    def grow(self, food, water):
        if water >= self._water_need and food >= self._food_need:
            if self.GROWTH_SCALE['Born'](self._weight):
                self._weight += self._growth_rate * 1.5
            elif self.GROWTH_SCALE['Baby'](self._weight):
                self._weight += self._growth_rate * 1.5
            elif self.GROWTH_SCALE['Child'](self._weight):
                self._weight += self._growth_rate * 1.25
            elif self.GROWTH_SCALE['Young'](self._weight):
                self._weight += self._growth_rate
            elif self.GROWTH_SCALE['Mature'](self._weight):
                self._weight += self._growth_rate
            elif self.GROWTH_SCALE['Old'](self._weight):
                self._weight += self._growth_rate * 0.75
        self._days_growing += 1
        self._update_status()

class Sheep(Animal):
    def __init__(self, name):
        super(Sheep, self).__init__(name, 5, 3, 3)
        self._type = 'Sheep'

    def grow(self, food, water):
        if water >= self._water_need and food >= self._food_need:
            if self.GROWTH_SCALE['Born'](self._weight):
                self._weight += self._growth_rate * 1.4
            elif self.GROWTH_SCALE['Baby'](self._weight):
                self._weight += self._growth_rate * 1.3
            elif self.GROWTH_SCALE['Child'](self._weight):
                self._weight += self._growth_rate
            elif self.GROWTH_SCALE['Young'](self._weight):
                self._weight += self._growth_rate
            elif self.GROWTH_SCALE['Mature'](self._weight):
                self._weight += self._growth_rate
            elif self.GROWTH_SCALE['Old'](self._weight):
                self._weight += self._growth_rate * 0.5
        self._days_growing += 1
        self._update_status()


if __name__ == '__main__':
    cow = Animal('star', 4, 5, 3)