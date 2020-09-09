#Write a function to draw a line
def line(num):
    for i in range(num):
        print('_',end='')
line(50)

#Write a function to draw a line with our specified character
def line(str):
    for i in range(50):
        print(str,end='')
line('a')

#Write a function to draw a line with our specified character and that character, specified times
str= str(input('enter the character :'))
def line(str):
    num= int(input('enter the number :'))
    for i in range(num):
        print(str,end='')
line(str)

#Write a function to display Average [Use with argument and no return value function]
x= int(input('enter the x value :'))
y= int(input('enter the y value :'))
def avg(x,y):
    print('average of x,y are:', (x+y)/2)
avg(x,y)

#Write a function to display Average [Use with argument and return value function]
x= int(input('enter the x value :'))
y= int(input('enter the y value :'))
def avg(x,y):
    return (x+y)/2
k= avg(x,y)
print('average of x and y is',k)

# Write functions to perform the job, selected from menu, which is laid in main function, for 2 numbers.
# Get both numbers in sub function, perform calculation and display result in the same
#1. Addition 2. Subtraction 3. Multiplication 4. Division
x= int(input('enter the x value :'))
y= int(input('enter the y value :'))
num= int(input('select a number from 1 to 4 :'))
def calculate(x,y):
    addition= x+y
    substraction= x-y
    multiply= x*y
    division= x/y
    if num==1:
        return addition
    elif num==2:
        return substraction
    elif num==3:
        return multiply
    elif num==4:
        return division
    else:
        print('enter the correct number')
g= calculate(x,y)
print('result is',g)



