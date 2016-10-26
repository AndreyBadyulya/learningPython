def sum_array(a):
    if len(a) > 1:
        m = 0
        for i in range(len(a)):
            m += a[i]
            i += 1
        return m
    else:
        return 0