def digitize(n):
    m = []
    for i in range(len(str(n))):
        a = int(str(n)[i])
        m.append(a)
    m.reverse()
    return m