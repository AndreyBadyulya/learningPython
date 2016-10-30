def get_planet_name(id):
    # This doesn't work; Fix it!
    name=""
    for i in str(id):
        if i=='1': name = "Mercury"
        if i=='2': name = "Venus"
        if i=='3': name = "Earth"
        if i=='4': name = "Mars"
        if i=='5': name = "Jupiter"
        if i=='6': name = "Saturn"
        if i=='7': name = "Uranus"  
        if i=='8': name = "Neptune"
    return name