def find_digit(num, nth):
    if nth <= 0:
        return -1
    elif num < 0:
        return int(str(abs(num))[-nth])
    elif nth > len(str(num)):
        return 0
    else:
        return int(str(num)[-nth])
