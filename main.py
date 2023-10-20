import math
num = int(input())

f = math.factorial(num)
print(f)
if num % 2 == 0:
    print('Четное')
else:
    print('Нечётное')

