import os
import random
from os.path import exists

FLAG = 777
summ = 0
try:
    os.remove("numbers.txt")
except Exception:
    print("File not found")
while summ < FLAG:
    number = input("Input number: ")
    try:
        number = int(number)
        with open("numbers.txt", 'a', encoding='utf-8') as fa:
            if random.randint(1, 13) == 7:
                raise Exception("Unfortunately you have encountered a misfortune...")
            fa.write(f'{number}\n')
        summ += number
    except ValueError:
        print("Please enter an integer value: ")

print(summ)
