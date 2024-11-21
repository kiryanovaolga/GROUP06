mesta = ['Praha', 'Brno', 'Plzeň']

# ['Praha5', 'Brno4', 'Plzeň5']

data = []

for mesto in mesta:
    # print(mesto + str(len(mesto)))
    data.append(mesto + str(len(mesto)))

print(data)

"""
1. definuji si prázdný list
2. procházím mesta for cyklus
3. pro každé mesto, zjistím počet znaků pomocí len()
4. spojím nazev a počet znaků (počet musím převést na str)
5. print spojený text
"""
