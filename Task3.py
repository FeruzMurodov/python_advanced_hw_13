import random

FLAG = 777
summ = 0
while summ < FLAG:
    number = int(input("Input number: "))
    try:
        with open("numbers.txt", 'a', encoding='utf-8') as fa:
            if random.randint(1, 13) == 7:
                raise Exception("Unfortunately you have encountered a misfortune...")
            fa.write(f'{number}\n')
        summ += number
    except FileNotFoundError:
        print('File not found')

print(summ)
