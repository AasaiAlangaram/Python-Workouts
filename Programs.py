"""
#1.Write a program to print the following string
#'Hi
#   I am your friend
#       I am from India
#Bye
#   Nice to meet you

#Solution:

print("Hi\n\tI am your friend\n\t\tI am from India\nBye\n\tNice to meet you")

#2.Write a program to print the version of python you are using

#Solution

import sys
print("Sys version info:",sys.version_info)
print("Sys version info:major:",sys.version_info[0])#specify index to get specific value
print("python.version:",sys.version)#sys.version get the version of python using

#61.Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

#Solution

def dictfunc():
    d = dict()
    for i in range(1,21):
        d[i] = i**2
    return d

print('The Dictionary is:',dictfunc())

#62.Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
# The function should just print the keys only.

#Solution

def dictfunc():
    d = dict()
    for i in range(1,21):
        d[i] = i**2
    return d.keys()

print('The Key:',dictfunc())

#63.


#3.write a python code to print current date and time

#solution

import datetime
now = datetime.datetime.now()
print("Current date and time:",now)


#4.write a program to find a radius of a circle

#Solution

#Area of a circle = pi*r^2

from math import pi
radius = float(input("Enter the radius of the circle:"))
Area = pi*radius**2
print("Area of a circle with radius"+str(radius)+"is:%.2f"%Area)
print("Area of a circle with radius"+str(radius)+"is:",Area)


#5.write a program to get a user name and print them in reverse order and print the total length

#Solution

fname = input("Enter your first name:")
lname = input("Enter your last name:")
length = len(fname)+len(lname) #len Function calculates length of a given word
print("Your name is :"+lname + ' ' + fname)
print("Total no of characters in your name is:",length)


#6.write a program that accept integer  and compute the value of n+nn+nnn

#solution

no = int(input("enter the no:"))
n1 = int("%s"%no)
n2 = int("%s%s"%(no,no))
n3 = int("%s%s%s"%(no,no,no))
sum = n1+n2+n3
print("n+nn+nnn:",sum)


#7.print the calender of a given month and year

#Solution

import calendar
year = int(input("Enter the Year:"))
month = int(input("Enter the month:"))
print(calendar.month(year,month))


#8.write a code that find a number of days between two days

#Solution

from datetime import date
fdate = date(2019,1,10)
sdate = date(2020,1,10)
bdays = sdate - fdate
print("No of days between two dates:",bdays)


#9.write a program to find volume of sphere

#Solution

from math import pi
radius = float(input("Enter the radius:"))
volume = 4/3*pi*radius**3
print("volume of a sphere:%.2f"%volume)


#10.write a program to get the difference between a numbers,if number1 is greater than number 2 then return double the difference

#Solution

n1 = int(input("enter first number:"))
n2 = int(input("enter second number:"))

if n1 > n2:
    print((n1-n2)*2)
else:
    print(n1-n2)


#11.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200

#Solution

list = []#method 1
list2 = []

for i in range(2000,4000):
    if(i%7==0) and (i%5!=0):
        list.append(str(i))
        list2.append(str(i))

print(','.join(list))
print(list2)


#12.Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program8,Then, the output should be:40320

#Solution

def factorial(n):
    if n>1:
        return n*factorial(n-1)
    else:
        return 1

x = int(input("enter a number:"))
print("The factorial of an given number:",factorial(x))


#13.Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
#Suppose the following input is supplied to the program:34,67,55,33,12,98
#Then, the output should be:['34', '67', '55', '33', '12', '98']('34', '67', '55', '33', '12', '98')

#Solution

values = input("Enter the values:")
list = values.split(',')
tuple = tuple(list)
print(list)
print(tuple)


#14. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.

#Solution

def sumof3no(n1,n2,n3):

    total = n1+n2+n3
    if n1 == n2 == n3:
        return total*3
    else:
        return total

n1 = int(input("enter first no:"))
n2 = int(input("enter second no:"))
n3 = int(input("enter third no:"))

print("Sum of three no :",sumof3no(n1,n2,n3))


#15. Write a Python program to get a new string from a given string where "Is" has been added to the front.
#If the given string already begins with "Is" then return the string unchanged.


def getstring(str):

    if len(str) > 2 and str[:2] == 'Is':
        return str
    else:
        return 'Is' + str

print(getstring('Aasai'))
print(getstring('Istemple'))


#16. Write a Python program to get a string which is n (non-negative integer) copies of a given string

#Solution

def chkstr(str,n):

#Method1

    result = ''
    result = str*n
    return result
#Method 2

#    result = ''
#   for i in range(n):
#        result = result + str
#    return result

print(chkstr('Aasai',3))
print(chkstr('Alan',5))


#17. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user

#Solution:

no = int(input("Enter an no:"))

if no%2 == 0:
    print("Given no is even")
else:
    print("Given no is odd")


#18.Write a program to find no of 4's in given list

#Solution

def count_no_of_4(no):

    count = 0
    for num in no:
        if num == 4:
            count += 1
    return count

list = [1,4,4,2,4,5]

print("The no of 4's in given list:",count_no_of_4(list))


#19.Program to find area and circumference of circle.

#Solution
from math import pi

def area(rad):

    area = pi*rad**2
    return float(area)
def circum(rad):

    circum = 2*pi*rad
    return float(circum)

radius = float(input("Enter a no:"))
print("Area:%.2f"%area(radius))
print("Circumference:%.2f"%circum(radius))


#20.Define a class which has at least two methods:getString: to get a string from console input
# printString: to print the string in upper case.

#Solution

class InputOutputString():

    def __init__(self):
        self.s = ''
    def getstr(self):
        self.s = input("enter a name:")
    def printstr(self):
        print(self.s.upper())

strobj = InputOutputString()
strobj.getstr()
strobj.printstr()

#21.Write a program that calculates and prints the value according to the given formula:Q = Square root of [(2 * C * D)/H]

#solution

import math

c=50
h=30
value = []
item = [x for x in input().split(',')]
for d in item:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(','.join(value))


#22.Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

#Solution

import datetime

while True:
    name = input("Enter your name:")
    age = int(input ("Enter your age:"))

    now = datetime.datetime.now()
    this_year = now.year

    print(name + " become 100 yrs old in " + str(this_year - age + 100))
    print()
    again = input("Do you want to continue if yes enter 1 else enter 0:")

    if again == '0':
        break


#23.Odd Or Even
'''
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. Hint: how does an even / odd
number react differently when divided by 2?

Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one
number to divide by (check). If check divides evenly into num, tell that
to the user. If not, print a different appropriate message.

'''

num = int(input("Enter a num:"))
check = int(input("Enter a num:"))

result = "The entered no is even no" if num%2==0 else "The entered no is even odd"
result += "\nit is multiple of 4" if num%4 == 0 else "not multiple of 4"
result_divided = "divided" if num%check == 0 else "not divides"
result += "\nyour no is {divided} by {check}".format(divided=result_divided,check=check)

print(result)


#24.List Less Than Ten
'''
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

1. Instead of printing the elements one by one, make a new list that has all the elements
less than 5 from this list in it and print out this new list.
2. Write this in one line of Python.
3. Ask the user for a number and return a list that contains only elements from the
original list a that are smaller than that number given by the user.

'''

#Solution:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print("Solution")
for i in a:
    if i < 5:
        print(i)

cutoff = int(input("Enter a number:"))
new_list = [i for i in a if i<=cutoff]
print(new_list)


#25.Program to find greatest in 3 numbers.

n1 = int(input("Enter a no:"))
n2 = int(input("Enter a no:"))
n3 = int(input("Enter a no:"))

if n1>n2 and n1>n3:
    print("n1 is greater")
elif n2>n1 and n2>n3:
    print("n2 is greater")
else:
    print("n3 is greater")


#26.Program to display first 10 natural no. & their sum.

#Solution
sum = 0
for i in range(1,11,1):
    print("first no is " + str(i))
    sum = sum+i

print("sum of all natural no is:{0}".format(sum))


#27.Program to print Fibonacci series up to 100.

#Solution

a,b,fib = 1,1,0
list = [a,b]

for i in range(0,9,1):
    if fib < 100:
        fib = a+b
        list.append(fib)

    a=b
    b=fib

print(list)


#28.Program to print a factorial of a number

#Solution

def fact(a):

    c=a
    while a>1:
        c= c*(a-1)
        a=a-1;
    return c
number = int(input("Enter a number:"))
print(fact(number))


#29.Program to find a given no is prime or not

def prime(no):
    loop=2

    while loop<no:

        if no%loop != 0:
            count = 1
            break
        else:
            count = 0
        loop=loop+1

    return count

number = int(input("Enter a number:"))
print(prime(number))
if prime(number) == 1:
    print("The given no is prime")
else:
    print("The given no is not an prime")


#30.Program to display sum of series 1+1/2+1/3+..........+1/n.

#Solution

no = int(input("Enter a number:"))
sum =0
for i in range(1,no+1,1):
    sum = sum + i

print("1/{0}".format(sum))


#31.Program to display series and find sum of 1+3+5+........+n.

#Solution

no = int(input("Enter a number:"))
sum = 0
for i in range(1,no+1,2):
    sum = sum+i
print(sum)


#32.Program to show sum of 10 elements of array & show the average.

array = []

no = int(input("Enter a number:"))
for i in range(1,no+1,1):
    val = int(input("Enter a value:"))
    array.insert(i,val)

print(array)
total = 0
#print(array[1])
for i in range(len(array)):
    total = total + array[i]
print("Sum of the array:",total)


#33.Find the sum of all multiples of 3 or 5 below 1000

#Solution
print("This Program will print the sum of all no below 1000 which are multiples of 3 & 5")
sum = 0
sum_list = []
for i in range(1000):
    if i%3 == 0 or i%5 == 0:
        sum += i
        sum_list.append(i)
    else:
        pass
print("Sum :",sum)
print("Sum_List :",sum_list)


#34.Even Fibonacci Series
#Fibonacci sequence whose values donot exceed four million,find the sum of the even-valued terms

#Solution

fib_list = []
def fibo(n):

    a,b = 0,1
    while b<n:
        a,b=b,a+b
        fib_list.append(a)
    return fib_list

def seq(fib_list):
    sum = 0
    for n in range(len(fib_list)):
        if fib_list[n]%2 == 0:
            sum += fib_list[n]
    return sum

fib = fibo(4000000)
print("Sequence is :",fib)
sumoffib = seq(fib)
print("Sum of even no in fib series:",sumoffib)


#35.Find the Largest Prime factor of a number

import numpy as np
def find_smallest_prime_factor(number):
    upper_bound = int(np.sqrt(number))+1

    for i in range(2,upper_bound):
        if number%i==0:
            print(i)
            return i
    return number

def find_largest_prime_factor(number):
    while True:
        smallest_factor = find_smallest_prime_factor(number)
        if smallest_factor<number:
            print(number)
            number //= smallest_factor
        else:
            return number

result = find_largest_prime_factor(10)
print('Result :',result)

#36.Define a class which has at least two methods:

#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.

#Solution

class Get_String():
    def __init__(self):
        pass
    def get_str(self):
        print('Enter a string')
        self.str = input()
        print('InputString :',self.str)
    def print_str(self):
        print('OutputString :',self.str.upper())

#Test Method

str1 = Get_String()
str1.get_str()
str1.print_str()

#37.Write a program that calculates and prints the value according to the given formula:Q = Square root of [(2 * C * D)/H]

#Following are the fixed values of C and H:C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma-separated sequence.
# For example Let us assume the following comma separated input sequence is given to the program:100,150,180
#The output of the program should be:18,22,24

#Solution


#import sqrt func from math
import math

C,H = 50,30 #Initialize C and H with given values

output = []

def cal(D):
    return (str(int(round(math.sqrt(2*C*float(D)/H)))))

D = [x for x in input().split()]

D = [int(x) for x in D]

print('The Given Input is :',D)

D = [cal(x) for x in D]

D = [str(x) for x in D]

print('The Output is :',D)



#38.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i * j.
#Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
#Then, the output of the program should be:[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

dimensions = [x for x in input().split()]
print(dimensions)
lst = []

try:
    x=int(dimensions[0])
    y=int(dimensions[1])
except ValueError:
    pass

for i in range(x):
    tmp = []
    for j in range(y):
        tmp.append(i * j)
    lst.append(tmp)

print(lst)


#39.Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

#Suppose the following input is supplied to the program:without,hello,bag,world
#Then, the output should be:bag,hello,without,world

lst = input('Enter here :').split()
print(lst.sort())# The Sorted list
print(','.join(lst))


#40.Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
#Suppose the following input is supplied to the program:
#Hello world
#Practice makes perfect
#Then, the output should be:
#HELLO WORLD
#PRACTICE MAKES PERFECT

list = []

while True:
    x = input('Enter :')
    if len(x)==0:
        break;
    list.append(x.upper())

for line in list:
    print(line)


#41.Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

#Suppose the following input is supplied to the program:hello world and practice makes perfect and hello world again
#Then, the output should be:again and hello makes perfect practice world

input = input('enter :').split()
print('Given Input :',input)
input = sorted(input)
print('Output :',' '.join(input))


#42.Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then
# check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

#Example:0100,0011,1010,1001
#Then the output should be:1010

#Solution

values = [x for x in input('Enter a value:').split()]
int_values = []
nodivisible = []
for i in range(len(values)):
    int_values.append(int(values[i],2))
    if int_values[i]%5 == 0:
        nodivisible.append(bin(int_values[i])[2:].zfill(4))

print(int_values)
print(nodivisible)



#43.Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

#Solution

Out = []

for i in range(1000,3000):
    nostr = str(i)
    if int(nostr[0])%2 == 0 and int(nostr[1])%2 == 0 and int(nostr[2])%2 == 0 and int(nostr[3])%2 == 0:
        Out.append(str(i))

print(Out)#Print List
print(','.join(Out))


#44.Write a program that accepts a sentence and calculate the number of letters and digits.

Words = input('Enter a word:')
letters = 0
digits = 0

for i in Words:
    if i.isalpha() == True:
        letters += 1
    elif i.isnumeric() == True:
        digits += 1
    else:
        pass
print('Number of letters is %d and numbers is %d'%(letters,digits))



#45.Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

#Solution

Words = input('Enter a word:')
upper = 0
lower = 0

for i in Words:
    if i.isupper() == True:
        upper += 1
    elif i.islower() == True:
        lower += 1
    else:
        pass

print('Number of uppercase letter is %d and lowercase letter is %d'%(upper,lower))


#46.Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

#Solution

def fn(value,n):
    return int(str(value)*n)

sum = 0
for i in range(1,int(input('Enter a number:'))+1):
        sum += fn(9,i)

print('The sum is %d'%(sum))


#47.Use a list comprehension to find the odd numbers in the list

#Solution

lst = [i for i in input('Enter Numbers:').split() if int(i)%2 != 0]
print(lst)
print(','.join(lst))


#48.Write a program that computes the net amount of a bank account based a
#transaction log from console input. The transaction log format is shown as following:

#Solution

def net_Amount(sd,sw):
    return (sd - sw)

sd = 0
get_deposit_details = input('Enter your Deposit Details:').split()
get_deposit_details = [int(i) for i in get_deposit_details ]
for i in get_deposit_details:
    sd += i
get_deposit_details = sd

sw = 0
get_withdraw_details = input('Enter your Withdraw Details:').split()
get_withdraw_details = [int(i) for i in get_withdraw_details]
for i in get_withdraw_details:
    sw += i
get_withdraw_details = sw


print('The net balance is %d$'%(net_Amount(get_deposit_details,get_withdraw_details)))


#49.A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

#Following are the criteria for checking the password:

#At least 1 letter between [a-z]
#At least 1 number between [0-9]
#At least 1 letter between [A-Z]
#At least 1 character from [$#@]
#Minimum length of transaction password: 6
#Maximum length of transaction password: 12

def check(x):
    upper,lower,number,special,count = 0,0,0,0,0
    for i in x:
        if i.isupper():
            upper = 1

    for i in x:
        if i.islower():
            lower = 1

    for i in x:
        if i.isnumeric():
            number = 1

    for i in x:
        if i == '$' or i == '#' or i == '@':
            special = 1

    #print(upper,lower,number,special)

    if upper == 1 and lower == 1 and number ==1 and special ==1:
        count = 1

    return count

#print(check('Aasai123'))
passwords = input('Enter your passwords:').split()
lst = []

for i in passwords:
    length = len(i)
    if 6<=length and length<=12 and check(i)==1:
        lst.append(i)

print(','.join(lst))


#50.Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

#Solution

class Test:
    def generator(self,n):
        return [i for i in range(n) if i%7==0]   # returns the values as a list if an element is divisible by 7

n = int(input())
num = Test()
lst = num.generator(n)
print(lst)


#51.File Operations

f = open('File.txt','a')
f.write(' I am Asai\n')
f.write('i am an Software engg')
f = open('File.txt','r')
for lines in f:
    print(f.read())
f.close()


#52.Inheritance

class Vehicle:

    def __init__(self, name, color):
        self.__name = name  # __name is private to Vehicle class
        self.__color = color

    def getColor(self):  # getColor() function is accessible to class Car
        return self.__color

    def setColor(self, color):  # setColor is accessible outside the class
        self.__color = color

    def getName(self):  # getName() is accessible outside the class
        return self.__name


class Car(Vehicle):

    def __init__(self, name, color, model):
        # call parent constructor to set name and color
        super().__init__(name, color)
        self.__model = model

    def getDescription(self):
        return self.getName() + self.__model + " in " + self.getColor() + " color"


# in method getDescrition we are able to call getName(), getColor() because they are
# accessible to child class through inheritance

c = Car("Ford Mustang", "red", "GT350")
print(c.getDescription())
print(c.getName())  # car has no method getName() but it is accessible through class Vehicle


#53.A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

i = 100
product = 0
palin_list = []

def reverse(n):
    Reverse = 0
    while(n > 0):
        Reminder = n % 10
        Reverse = (Reverse *10) + Reminder
        n = n //10
    return Reverse


for i in range(100,1000):
    for j in range(100,1000):
        #print('i,j:\n',i,j)
        product = i*j
        get = reverse(product)

        if product == get:
            print('i,j:\n', i, j)
            palin_list.append(product)

        product = 0
        get =0

print(max(palin_list))


#54.2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

list = []
small_no = 0
i = 1
rem = 0

for i in range(1,300000000):
    for j in range(1,20):
       rem = i%j
       small_no += rem
    if small_no == 0:
        #print('%d is divisible by all elements in i' % (i))
        list.append(i)

    else:
        print(i)
        small_no = 0    #Reset Small_no variable
        #print('%d is not divisible by all elements in i'%(i))

print(list)


#55.The sum of the squares of the first ten natural numbers is,12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

i=1

#Function to find sumofsquare
def sumofsquare(n):
    fsum = 0
    for i in range(1,n+1):
        fsum += i
        #print(fsum)
    return (fsum*fsum)

#Function to find Squareofsum
def squareofsum(n):
    ssum = 0
    for i in range(1,n+1):
        ssum += (i*i)
    return ssum

#Function to find difference between sumofsquare And Squareofsum
def diff_of_sofsqu_and_squofsum(n1,n2):

    #n1 = sumofsquare answer
    #n2 = squareofsum answer

    return (n1-n2)

g1 = sumofsquare(100)
g2 = squareofsum(100)
print(diff_of_sofsqu_and_squofsum(g1,g2))


#56.By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

def getprimes(x):
    primes = []
    # Loop through 9999 possible prime numbers
    for i in range(2, 200000):

        for j in range(2, i):

            if i % j == 0:
                break

        else:

            primes.append(i)

        if len(primes) == x:
            print('size of list :',len(primes))
            return primes

print('Elements in list :\n',getprimes(100))


from operator import itemgetter

# Get Input Value from console

# while True:
#     var = input('Enter the name,age,score:\n')
#     var = var.split(' ') # split by space
#     if not var[0]:
#         break
#     lst.append(tuple(var))

lst = [('Tom','19','80'),('John','20','90'),('Jony','17','91'),('Jony','17','93'),('Json','21','85')]

# https://docs.python.org/3/library/functions.html#sorted
# https://docs.python.org/3/howto/sorting.html

Ascending_ordered = sorted(lst, key=itemgetter(0,1,2),reverse = False)
print('Ascending_ordered :',Ascending_ordered)
Descending_ordered = sorted(lst, key=itemgetter(0,1,2),reverse = True)
print('Descending_ordered :',Descending_ordered)





#57.Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n

#Solution

class nodivby7:
    def check(self,n):
        l = []
        for i in range(n):
           if i%7 == 0:
                l.append(i)
        return l
    #using list comprehension
    #    return [i for i in range(n) if i%7 == 0]

num = int(input("Enter the range:"))
find = nodivby7()
print(find.check(num))
print('The number of elements that are divisible by 7 withn {n} : {ans}'.format(n=num,ans=len(find.check(num))))



#58.Write a program to compute the frequency of the words from the input.

from collections import Counter

ss = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'.split()
# counter function simply counts the items count return as dictionary
ss = Counter(ss)         # returns key & frequency as a dictionary
print(ss)
# sorting the items in dictionary
ss = sorted(ss.items())  # returns as a tuple list
print(ss)

for i in ss:
    print("%s:%d"%(i[0],i[1]))



#59.Write a method which can calculate square value of number

def square(num):
    return (num*num)

no = int(input('enter the number to square:'))
print('the square of the number is',square(no))


# 60. You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:

# 1: Sort based on name
# 2: Then sort based on age
# 3: Then sort by score
# The priority is that name > age > score.

from operator import itemgetter

# Get Input Value from console 

# while True:
#     var = input('Enter the name,age,score:\n')
#     var = var.split(' ') # split by space
#     if not var[0]:
#         break
#     lst.append(tuple(var))

lst = [('Tom','19','80'),('John','20','90'),('Jony','17','91'),('Jony','17','93'),('Json','21','85')]

# https://docs.python.org/3/library/functions.html#sorted
# https://docs.python.org/3/howto/sorting.html

Ascending_ordered = sorted(lst, key=itemgetter(0,1,2),reverse = False)
print('Ascending_ordered :',Ascending_ordered)
Descending_ordered = sorted(lst, key=itemgetter(0,1,2),reverse = True)
print('Descending_ordered :',Descending_ordered)

#61.Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

#Solution

def dictfunc():
    d = dict()
    for i in range(1,21):
        d[i] = i**2
    return d

print('The Dictionary is:',dictfunc())

#62.Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
# The function should just print the keys only.

#Solution

def dictfunc():
    d = dict()
    for i in range(1,21):
        d[i] = i**2
    return d.keys()

print('The Key:',dictfunc())

#63.Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

#Solution

def listfunction():
    l = []
    for i in range(1, 21):
        l.append(i**2)
    return l

result = listfunction()
print('The Expected list is:', listfunction())

for k in range(0,20):
    print('The value at index {index} is {value}\n'.format(index = k,value = result[k]))

#64.Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the first 5 elements in the list.

#Solution

def listfunction():

    l =[]
    for i in range(1,21):
        l.append(i**2)

    print('The list is :',l)

    print('The First Five elements are :',l[:5])

listfunction()

#64.Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the last 5 elements in the list.

#Solution

def listfunction():

    l =[]
    for i in range(1,21):
        l.append(i**2)

    print('The list is :',l)

    print('The Last Five elements are :',l[-6:])

listfunction()


#65.With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.

#Solution

tp = (1,2,3,4,5,6,7,8,9,10)

print('The Original Tuple:',tp)

splitted = [print('Splitted List :{List}'.format(List = tp[x:x+5])) for x in range(0,len(tp),5)]
"""

#66.Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

#Solution

tp = (1,2,3,4,5,6,7,8,9,10)
even_tp = ()
even_tp  = tuple(i for i in tp if i%2==0)
print("The Original Tuple:",tp)
print("The Even Tuple :",even_tp)

#67.Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

#Solution

input = input('Enter string:')

output = ''.join(['Yes' if input == 'yes' or input =='YES' or input =='Yes' or input =='YeS' else 'No' ])

print(str(output))

#68.Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

#Solution

input = [1,2,3,4,5,6,7,8,9,10]

squaredlist = list(map(lambda x:x**2,input))
print('The Original List is:',input)
print('The Squared List is:',squaredlist)

#69.Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

#Solution

input = [1,2,3,4,5,6,7,8,9,10]

output = ''.join(list(map(lambda x:x**2,filter(lambda i:i%2==0,input))))

print('The input is:',input)
print('The output is:',output)