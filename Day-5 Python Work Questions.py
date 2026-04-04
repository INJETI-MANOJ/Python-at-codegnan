#1) Write a program to add two numbers and print the result.
num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
result = num1 + num2
print('Addition of two number is:',result)

#2) Take two integers as input and print their quotient and remainder?
num3 = int(input("Enter num4:"))
num4 = int(input("Enter num4:"))
print('Quotient is:', num3/num4, 'and remainder is:' ,num3%num4)

#3) Given a number, check if it is even or odd using the modulus operator.
num5 = int(input("Enter num5:"))
if num5 % 2 == 0:
    print(num5,'is even number')
else:
    print(num5,'is odd number')
    
#4) Write a program to swap two variables using arithmetic operators (without a third variable).
a = int(input('Enter a value:'))
b = int(input('Enter b value:'))
a = a+b
b = a - b
a = a - b
print(a,b)

#5) Take three numbers and print the largest using comparison operators.
n1 = int(input('Enter the n1 value:'))
n2 = int(input('Enter the n2 value:'))
n3 = int(input('Enter the n3 value:'))
if n1>n2 and n1>n3:
    print('The largest number is:',n1)
elif n2>n1 and n2>n3:
    print('The largest number is:',n2)
else:
    print('The largest number is:',n3)

#6. Write a program to calculate the square of a number using the exponent operator (**).
num6 = int(input("Enter num6:"))
num7 = int(input("Enter the exponent number:"))
print('The square of the number is:',num6**num7)

#7) Given two numbers, check if the first is divisible by the second.
num8 = int(input("Enter num8:"))
num9 = int(input("Enter num9:"))
if num8%num9==0:
    print('first is divisble by the second')
else:
    print('first is not divisble by the second')

#8) Write a program to calculate the area of a rectangle using multiplication operator.
x = int(input('Enter the length:'))
y = int(input('Enter the breadth:'))
print('Area of a rectangle is:', x*y)

#9) Take a number and print whether it is positive, negative, or zero.
num10 = int(input("Enter num10:"))
if num10 == 0:
    print('The number is Zero')
elif num10>0:
    print('The number is Positive')
else:
    print('The number is Negative')
    
#10. Write a program to check if two numbers are equal using the equality operator (==).
num11 = int(input("Enter num11:"))
num12 = int(input("Enter num12:"))
if num11 == num12:
    print('The numbers are equal')
else:
    print('The numbers are not equal')


#Problems on Conditional Statements



#11) Write a program to check if a person is eligible to vote (age ≥ 18).
age = int(input('Enter your age:'))
if age >=18:
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')

#12) Take a number and check if it is a multiple of both 3 and 5.
num13 = int(input("Enter num13:"))
if num13 % 3 == 0 and num13 == 0:
    print(num13,'is multiple of both 3 and 5')
else:
    print(num13,'is not multiple of both 3 and 5')

#13) Write a program to find the greatest of three numbers using nested if.
n4 = int(input('Enter the n4 value:'))
n5 = int(input('Enter the n5 value:'))
n6 = int(input('Enter the n6 value:'))
if n4>n5:
    if n4>n6:
        print('The largest number is:',n4)
elif n5>n4:
    if n5>n6:
        print('The largest number is:',n5)
    else:
        print('The largest number is:',n6)
#14) Given a year, check if it is a leap year. Write a program to classify a character as vowel or consonant.
year = int(input("Enter a year: "))
ch = input("Enter a character: ")

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
if ch.isalpha():
    if ch in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        print("Vowel")
    else:
        print("Consonant")
#15) Take marks as input and print grade according to conditions:

'''             >90 → A
                75-89 - B
                50-74 → C
                <50 → Fail'''
marks = int(input("Enter your marks:"))
if marks >= 90 and marks <=100:
    print("Grade A")
elif marks >= 75 and marks <=89:
    print("Grade B")
elif marks >= 50 and marks <=74:
    print("Grade c")
elif marks < 50 and marks >=0:
    print("Grade Fail")
else:
    print("Invalid Marks")

#16) Write a program to check if a number is prime.
g = int(input('Enter the num:'))
if g <=1:
    print(g,'is not a prime number')
elif g == 2 or g == 3 or g == 5:
    print(g,'is a prime number')
else:
    if g % 2 == 0 or g % 3 == 0 or g % 5 == 0:
        print(g,'is not a prime number')
    else:
        print(g,'is a prime number')
        
#17) Take a number and check if it is a palindrome.
m= input('Enter any value:')
if m[::-1] == m:
    print(m[::-1],'is a palindrome')
else:
    print(m[::-1],'is a not palindrome')
#18) Write a program to calculate electricity bill:

'''Up to 100 units ₹5/unit

101-200 units ₹7/unit

Above 200 units ₹10/unit'''
units = float(input('Enter the units:'))
if units >=0 and units<=100:
    print('The electricity bill is:',units*5)
elif units >100 and units<=200:
    print('The electricity bill is:',units*7)
else:
    print('The electricity bill is:',units*10)
#19) Write a program to check if a given year is a century year (ends with 00) and also if it is a leap century
y = int(input("Enter a year: "))

if y % 100 == 0:
    print(y, "is a Century Year")
    
    if y % 400 == 0:
        print("It is also a Leap Century Year")
    else:
        print("It is NOT a Leap Century Year")

else:
    print(y, "is NOT a Century Year")
