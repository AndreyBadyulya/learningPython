def evil(n):
    if (str(bin(n)).count('1')) % 2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"