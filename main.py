from os import times

print("Введите координаты первой точки")
a1 = int(input()) #столб
b1 = int(input()) #строка

print("Введите координаты второй точки")
a2 = int(input())
b2 = int(input())

c = a1
d = b1

if a1 == a2 and b1 > b2:
    print("1 условие - YES")
else:
    print("1 условие - NO")

if a1 == a2 and b1 < b2:
    print("2 условие - YES")
else:
    print("2 условие - NO")

if a1 < a2 and b1 == b2:
    print("3 условие - YES")
else:
    print("3 условие - NO")

if a1 > a2 and b1 == b2:
    print("4 условие - YES")
else:
    print("4 условие - NO")

print("5 условие")
a1 = c
b1 = d
while (a1 > 1 and a1 <= 7) and (b1 > 1 and b1 <= 7):
    a1 = a1 - 1
    b1 = b1 - 1
#    print("%d %d" % (a1, b1))
    if a1 == a2 and b1 == b2:
        print("YES")
    else:
        print('NO')


print("6 условие")
a1 = c
b1 = d
while (a1 > 1 and a1 <= 7) and (b1 > 1 and b1 <= 7):
    a1 = a1 + 1
    b1 = b1 - 1
#    print("%d %d" % (a1, b1))
    if a1 == a2 and b1 == b2:
        print("YES")
    else:
        print('NO')

print("7 условие")
a1 = c
b1 = d
while (a1 > 1 and a1 <= 7) and (b1 > 1 and b1 <= 7):
    a1 = a1 - 1
    b1 = b1 + 1
#    print("%d %d" % (a1, b1))
    if a1 == a2 and b1 == b2:
        print("YES")
    else:
        print('NO')

print("8 условие")
a1 = c
b1 = d
while (a1 > 1 and a1 <= 7) and (b1 > 1 and b1 <= 7):
    a1 = a1 + 1
    b1 = b1 + 1
#   print("%d %d" % (a1, b1))
    if a1 == a2 and b1 == b2:
        print("YES")
    else:
        print('NO')










