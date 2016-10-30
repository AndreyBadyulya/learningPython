def sum_mul(n, m):
    if m <= 0 or n <= 0:
        return 'INVALID'
    else:
        return sum(range(n, m, n))