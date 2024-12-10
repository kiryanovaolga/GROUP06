# functional_map.py

data = [2, 8, 9]

# pomocí list comprehension
# zjistit druhou mocninu každého čísla
# [4, 64, 81]
# [??? for x in data]
# x ** 2
# x * x

# list comprehension
result = [x * x for x in data]
print(result)

# map with lambda
result = map(lambda x: x * x, data)
print(list(result))

def get_pow(cislo):
    return cislo * cislo

# map with own function
result = map(get_pow, data)
print(list(result))
