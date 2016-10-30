def pattern(n):
    l = "1"
    for i in range(2, n + 1):
        l += "\n" + (("1" + "*" * (i - 1)) + str(i))
        i += 1
    return l
    raise NotImplementedError("TODO: pattern")