#2
text = input("Введите текст:")
print(text[::-1])

#3
n = 5
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')

#4
a = int(input())
b = int(input())
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)

#5
a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(i)

