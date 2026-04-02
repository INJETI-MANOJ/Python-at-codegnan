#1.Check number is zero or non-zero?
num = int(input("Enter the num:"))

if num == 0:
    print("The number is zero")
else:
    print("The number is non-zero")

#2.Check number is +ve or -ve?
if num >= 0:
    print("The number is Positive")
else:
    print("The number is Negative")

#3.Check number is even or odd?
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

#4.Check whether the person is eligible for vote or not?
if num >= 18:
    print("The person is eligible for vote")
else:
    print("The person is not eligible for vote")

#5.Check whether number is divisible by 3 or not?
if num % 3 == 0:
    print("The number is divisible by 3")
else:
    print("The number is not divisible by 3")

#6.Check whether number is divisible with both 3 and 5 or not?
if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by 3 and 5")
else:
    print("The number is not divisible by 3 and 5")

#Find bigger number among two numbers?
num1= int(input("Enter the num1:"))
if num > num1:
    print(num, "is the biggest number")
else:
    print(num1, "is the biggest number")
