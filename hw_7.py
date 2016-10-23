def super_size(n):
    if len(str(n)) > 1:
        x = int(''.join(sorted(str(n))[::-1]))
        return x
    else:
        return n