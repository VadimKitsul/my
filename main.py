import math
num = int(input())

f = math.factorial(num)
print(f)
if num % 2 == 0:
    print('Четное')
else:
    print('Нечётное')
def get_even(number):
    if number % 2 == 0:
        return True
    return False

for i in range(14000):
    a = int(input('A'))
    print(get_even(a))


