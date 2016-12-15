def dict_planet():
    solar_system = {
    'Mercury' : 57.9,
    'Venus' : 108.2,
    'Earth' : 149.6,
    'Mars' : 227.9,
    'Jupiter' : 778.3,
    'Saturn' : 1427.0,
    'Uranus' : 2871,
    'Neptune' : 4497.1
    }
    print 'Rasstoyanie ot Solnca:'
    for k in solar_system.keys():
        print "Planeta {planet} nahoditsya na rasstoyanii {dist} mln.km ot Solnca".format(planet = k, dist = solar_system.get(k))
        k += k
    print 'next'
    for k in solar_system.keys():
        sorted(solar_system, key=solar_system.items())
        print "Planeta {planet} nahoditsya na rasstoyanii {dist} mln.km ot Solnca".format(planet = k, dist = solar_system.get(k))
        k += k
if __name__ == "__main__":
	dict_planet()