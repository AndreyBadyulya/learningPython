def animals(heads, legs):
    #return (Chickens, Cows)
    if heads == 0 and legs == 0:
        return (0, 0)
    elif legs % 2 != 0 or heads > 1000 or legs > 1000 or heads <= 0 or legs <= 0 or legs / heads > 4 or legs / heads < 2:
        return "No solutions"
    else:
        x = ((heads * 4) - legs) / 2
        return (x, heads - x)