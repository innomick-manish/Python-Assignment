#Display entered name 50 times
name= input('enter the name:')
for i in range(50):
    print(name)

#Display entered 10 different numbers
dif_num = list(map(int, input("Enter 10 different numbers: ").split()))
print(dif_num)

#Display your good name as many times you want to display
good_name= input('enter the good name:')
num_to_repeat= int(input('times to repeat:'))
for i in range(num_to_repeat):
    print(good_name)

#Generate 1, 2, 3, ........................................., 100
for i in range(1,101):
    print(i)

#Generate 100, 99, 98, ...................................., 1
for k in range(100,0,-1):
    print(k)

#Generate 2, 4, 6, 8, ....................................., 100
for f in range(1,101):
    if f%2==0:
        print(f)

#Generate 1, 3, 5, 7, ....................................., 100
for h in range(1,101):
    if h%2!=0:
        print(h)

#Generate 5, 10, 15, 20, ................................, 100
for s in range(1,101):
    if s%5==0:
        print(s)

#Generate 100 even numbers
for e in range(1,201):
    if e%2==0:
        print(e)

#Display tables from 2-10
for i in range(2, 10+1):
    print('{} table'.format(i))
    for j in range(i, (i*10)+1, i):
            print(j, end="\t")
    print('\n')

#Display the table from desired number to desired number
x, y = [int(x) for x in input("Enter two value: ").split()]
for i in range(x, y+1):
    print('{} table'.format(i))
    for j in range(i, (i*10)+1, i):
            print(j, end="\t")
    print('\n')

# generate star pattern-1
n=int(input('Number of lines: '))
for i in range(0, n):
    for j in range(0, i+1):
        print("* ", end="")
    print('\r')

# generate star pattern-2
n=int(input('Number of lines: '))
for i in range(n, 0,-1):
    for j in range(0, i):
        print("* ", end="")
    print('\r')

# generate star pattern-3
n=int(input('Number of lines: '))
k = 2 * n - 2
for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        print("* ", end="")
    print("\r")
