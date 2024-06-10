import random

a, b = map(int, input("Enter Range:").split(" "))
x = random.randint(a, b)

ans = 0
while (ans != x):
    ans = int(input("Enter number(Not Zero):"))
    if (ans < x):
        print("Higher Value")
    if (ans > x):
        print("lower Value")
print("Correct Guess!!")
