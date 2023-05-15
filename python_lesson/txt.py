import time
from datetime import datetime

time_work = 60 * 60
one = ['project', 'terver', 'physic']
two = ['math', 'python', 'analys']
today = input()
array = []
f = open('txt.txt', 'a', encoding='utf-8')
day = datetime.now().day
month = datetime.now().month
f.write(f'{day}.{month}')

if today == 'one':
    for i in one:
        print(f'{i} time {time_work} sec')
        time.sleep(time_work)
        print('ALL')
        text = 'input'

        while True:
            inp = input()
            if not inp: break
            array.append(inp)
        for j in range(len(array)):
            f.write(f'{i}:{j} - {array[j]}\n')
if today == 'two':
    for i in two:
        print(f'{i} time {time_work} min')
        time.sleep(time_work)
        print('ALL')
        text = 'input'

        while True:
            inp = input()
            if not inp: break
            array.append(inp)
        for j in range(len(array)):
            f.write(f'{i}:{j} - {array[j]}\n')
