#if-elif-else:

marks = int(input("Enter your marks:"))
if marks >= 90 and marks <=100:
    print("Grade A")
elif marks >= 80 and marks <=89:
    print("Grade B")
elif marks >= 60 and marks <=79:
    print("Grade d")
elif marks >= 40 and marks <=59:
    print("Grade B")
elif marks <= 40 and marks >=0:
    print("Grade Fail")
else:
    print("Invalid Marks")
