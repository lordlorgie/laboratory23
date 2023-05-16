def series_sum(n):
    sum = 0
    for i in range(1, n+1):
        term = 1 / (1 + (3 * (i - 1)))
        sum += term
    return "{:.2f}".format(sum)
