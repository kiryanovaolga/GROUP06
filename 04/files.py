# files.py
# práce se soubory

def read():
    with open('04/soubor.txt', mode='r', encoding='utf-8') as file:
        # file.readline() - 1 řádek
        # file.read() - celý soubor

        for line in file:
            print(line)


def write():
    # vždy přepisuje obsah na novou hodnotu
    with open('04/test.txt', mode='w', encoding='utf-8') as file:
        file.write('HELLO FROM PYTHON!')

def append():
    # vždy přidávat nový řádek  do souboru test2.txt
    with open('04/append.txt', mode='a', encoding='utf-8') as file:
        file.write('Hello\n')

append()
# read()