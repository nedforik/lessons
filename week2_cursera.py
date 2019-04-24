# pro1 какое число больше
# a = int(input())
# b = int(input())
# if a < b:
#    print(b)
# else:
#    print(a)

# pro2 написать 1 ,2 или 0
# a = int(input())
# b = int(input())
# if a < b:
#    print('2')
# else:
#    if a > b:
#        print('1')
#    else:
#        print('0')

# pro3 наибольшее из трёх чисел
"""a = int(input())
b = int(input())
c = int(input())
if a < b and a < c:
    if b < c:
        print(c)
    else:
        print(b)
elif a < c and b < c:
    print(c)
elif a < b and b > c:
    print(b)
elif b < c:
    print(a)
else:
    print(a)"""

# pro4 высокосный год
"""N = int(input())
if ((N % 4) == 0 and (N % 100) != 0) or (N % 400) == 0:
    print("YES")
else:
    print("NO")"""

# pro5 про коров
"""N = int(input())
if N == 1 or (N % 10 == 1 and N // 10 >= 2):
    print(N, 'korova')
elif N == 2 or (N % 10 == 2 and N // 10 >= 2):
    print(N, 'korovy')
elif N == 3 or (N % 10 == 3 and N // 10 >= 2):
    print(N, 'korovy')
elif N == 4 or (N % 10 == 4 and N // 10 >= 2):
    print(N, 'korovy')
else:
    print(N, 'korov')"""

# pro6 возрастание из трёх чисел
"""a = int(input())
b = int(input())
c = int(input())
if a < b and a < c:
    print(a)
    if b < c:
        print(b)
        print(c)
    else:
        print(c)
        print(b)
elif a < c and b < c:
    print(b)
    print(a)
    print(c)
elif a < b and b > c:
    print(c)
    print(a)
    print(b)
elif b < c:
    print(b)
    print(c)
    print(a)
else:
    print(c)
    print(b)
    print(a)"""

# pro7 сколько чисел совпадает
"""a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a == b or b == c or c == a:
    print(2)
else:
    print(0)"""

# pro8 про замок
"""A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
if A <= D and B <= E or B <= D and A <= E:
    print("YES")
elif B <= D and C <= E or C <= D and B <= E:
    print("YES")
elif C <= D and A <= E or A <= D and C <= E:
    print("YES")
else:
    print("NO")"""

'''# pro9 проо корбоки ???
A1 = int(input())
B1 = int(input())
C1 = int(input())
A2 = int(input())
B2 = int(input())
C2 = int(input())
buffer = 0
if A1 < B1 and A1 < C1:
    A1 = A1
    print(A1)
elif (A1 > B1) and (A1 < C1):
    B1 = buffer

print("Boxes are equal")
print("The first box is smaller than the second one")
print("The first box is larger than the second one")
print("Boxes are incomparable")'''

# pro10 про квадраты
N = int(input())
i = 1
res = 0
while res < N:
    res = i*i
    if res <= N:
        print(res)
    i = i+1
