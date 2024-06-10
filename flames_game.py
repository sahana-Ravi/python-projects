n1, n2 = map(list, input("Enter two names: ").split(" "))
print(n1, n2)
for i in n1:
    if i in n2:
        n1.remove(i)
        n2.remove(i)
word = n1 + n2
print(word)
l = len(word)
j = 0
print(l)
x = ['Friends', 'Love', 'Affectionate', 'Marriage', 'Enemy', 'Sibling']
while (len(x) > 1):
    letters = []
    for i in range(l):
        if (j == len(x)):
            j = 0

        letter = x[j]
        j = j+1
    x.remove(letter)
    j = j-1
print(x[0])
