results, odds, evens = [], [], []


def enter_results(*inp):
    global results, odds, evens
    
    results += inp
    odds, evens = results[::2], results[1::2]


def get_sum():
    return round(sum(odds),2), round(sum(evens),2)


def get_average():
    return round(sum(odds) / len(odds), 2), round(sum(evens) / len(odds), 2)

enter_results(3.5, 2.14, 45.2, 37.99)
print(get_sum(), get_average())
enter_results(5.2, 7.3)
print(get_sum(), get_average())
enter_results(1.23, 4.56, 3.14, 2.71, 0, 0)
print(get_sum(), get_average())