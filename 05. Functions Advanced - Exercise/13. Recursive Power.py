def recursive_power(*args):
    value = args[0]
    power = args[1]
    if power == 1:
        return value
    elif power == 0:
        return 1
    else:
        return value * recursive_power(value, power - 1)


print(recursive_power(2, 10))