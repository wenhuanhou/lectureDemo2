
intVarialbe=4
floatVariable=4.5
stringVariable= "software 1 is fun"

print(intVarialbe)
print(floatVariable)
print(stringVariable)

print(type(intVarialbe))
print(type(floatVariable))
print(type(stringVariable))a

intvariable=int(floatVariable)
print("here is the int version of float variable",intVariable)

shareOfloan=500.50/3
print(shareOfloan)
print(int(shareOfloan))

######

num1 =int(input("enter a number: "))
num2 =float(input("enter another number: "))
sum = num1 + num2

print(sum)

#####

name = input("enter your name: ")
school = input("enter your school: ")

print("you are : ", name, "and your school name is:", school)
print(f"your name is: {name}, and your school name is: {school}")

rds=float(input("enter a number:"))
area=3.14*rds**2
print(f"if your rds is: {rds}, the area is : {area}")
#####

# ###1###
user= input('enter your name: ')
print("Hello,"+ user)
###2###
rds=float(input("enter a number:"))
area=3.14*rds**2
print(f"if your rds is: {rds}, the area is : {area}")
###3###
length = float(input('enter the length of a rectangle: '))
width = float(input('enter the width of a rectangle: '))
C= (length+width)*2
a= length*width
print(f'the C is:{C}, the AREA is :{a}')
##4###
number1 = int(input('enter the first number: '))
number2 = int(input('enter the second number: '))
number3 = int(input('enter the third number: '))
sum = number1+number2+number3
product = number1*number2*number3
average = (number1+number2+number3)/3
print(f'the sum is {sum}, the product is {product}, the average is {average}')
# ###5###
talent = float(input('enter the talent :'))
pound = float(input('enter the pound: '))
lot = float(input('enter the lot'))

talent1 = 20*32*13.3*talent
pound1 = 32*13.3*pound
lot1 = 13.3*lot
sum = talent1+pound1+lot1

kilogram = int(sum/1000)
gram = float(sum%1000)
print(f'The weight in modern units:{kilogram} kilograms and {gram:.2f} grams.')
###6####
import math
import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
num3 = random.randint(0, 9)
num4 = random.randint(0, 9)
num5 = random.randint(0, 9)
num6 = random.randint(0, 9)
print(num1,num2,num3)
print(num4,num5,num6)

num7 = random.randint(1, 6)
num8 = random.randint(1, 6)
num9 = random.randint(1, 6)
num10 = random.randint(1, 6)
num11 = random.randint(1, 6)
num12 = random.randint(1, 6)
num13 = random.randint(1, 6)
num14 = random.randint(1, 6)
print(num7,num8,num9,num10)
print(num11,num12,num13,num14)