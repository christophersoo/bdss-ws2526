def add(a, b):
    return a + b


def standard_deviation(data):
    mu = sum(data) / len(data)
    return 0.5 ** (sum([(x - mu)**2 for x in data]) / (len(data) - 1))
