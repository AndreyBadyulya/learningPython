def fuelPrice(litres, pricePerLiter):
    if type(litres) == int or type(pricePerLiter) == int:
        if litres == 2 & litres < 4:
            return round((litres * (pricePerLiter - 0.05)), 2)
        elif litres == 4 & litres < 6:
            return round((litres * (pricePerLiter - 0.10)), 2)
        elif litres == 6 & litres < 8:
            return round((litres * (pricePerLiter - 0.15)), 2)
        elif litres == 8 & litres < 10:
            return round((litres * (pricePerLiter - 0.20)), 2)
        elif litres >= 10:
            return round((litres * (pricePerLiter - 0.25)), 2)
        elif litres <= 1:
            return round((litres * pricePerLiter), 2)