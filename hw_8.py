def no_boring_zeros(n):
    #if str(n).isdigit() == True:
        v = len(str(n))
        for i in range(v):
            i += 1
            str(n)[-i] == 0
            m = (v - i) + 1
        else:
            k = str(n)[:int(m):]
            return int(k)