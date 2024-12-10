data = ['Jan', 'Petr', 'Nina']

# result = ['J', 'P', 'N']

result = []

for item in data:
    result.append(item[0])

print(result)

# list comprehension
# generátorová notace
result2 = [item[0] for item in data]

print(result2)

# dict comprehension
d = {'A': 1, 'B': 2, 'C': 2}
d2 = {d[key]: key for key in d}
print(d2)
