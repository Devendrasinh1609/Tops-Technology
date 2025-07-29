"""Module 7) DA - Introduction to Python Assignment
1) What are the types of Applications?
 Python can be used to build many types of application because it is general purpose programming language.  Here main types of application
	Web Application :
o	Websites and web based platforms.
o	Bulit using framework like Django, Flask, FastAPI

	Desktop GUI Application :
o	Software with a graphical interface for PCs. 
o	Build using libraries like Tkinter , PyQt

	Data Science & Data Analysis Applications :
o	Used for analyzing , visualizing , and  processing data.
o	Tools : Pandas, Numpy, Matplotib, Seaborn.

	Artificial Intelligence & Machine Learning Application :
o	AI models , chatbots.
o	Libraries : TensorFlow, Scikit-learn, PyTorch.

	Game Development :
o	Creating 2D/3D games.
o	Libraries: Pygame, Panda 3D.
	Mobile Application:
o	Mobile apps for Android / IOS (less common).
o	Framework: Kivy ,BeeWarte

2) What is programing? 
--> Programming is the process of writing instructions (code) that a computer can   understand and execute to perform specific tasks or solve problems.
3) What is Python?
--> Python is high-level, easy to read, programming language used to build websites, apps, data analysis tools, artificial intelligence, and more.
"""


#4) Write a Python program to check if a number is positive, negative or zero.
num1 = int(input("Enter number for check positive or not :"))
if num1< 0:
    print("Number is negetive")
elif num1 > 0:
    print("Number is positive")
else:
    print("Number is zero")


#5) Write a Python program to get the Factorial number of given numbers. 
num = int(input("Enter a number for factorial: "))
fact = 1
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The fact of 0 is 1.")
else:
    for i in range(1, num + 1):
        fact *= i
    print(f"The fact of {num} is {fact}.")


#6) Write a Python program to get the Fibonacci series of given range
n = int(input("Enter the number of terms for fibo: "))
a, b = 0, 1
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci series up to 1 term:", a)
else:
    print("Fibonacci series:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


"""7) How memory is managed in Python? 
Python uses a dynamic memory management system that includes automatic garbage collection. The memory management in Python is primarily handled by the Python Memory Manager and Garbage Collector.

#8) What is the purpose continuing statement in python? 
 --> The continue statement is used inside loops (for or while) to skip the current iteration and move directly to the next iteration of the loop.
  -- It does not terminate the loop, unlike break.
  -- It just skips the remaining code in the current iteration."""
print()
#9) Write python program that swap two number with temp variable and without temp variable. 
# Swapping with a temporary variable
a = int(input("Enter first number1: "))
b = int(input("Enter second number2: "))

print("\nBefore swapping: a =", a, ", b =", b)

# Method 1: Using a temporary variable
temp = a
a = b
b = temp
print("After swapping with temp variable: a =", a, ", b =", b)

# Resetting values to original
a = int(input("\nEnter first number1 again temp: "))
b = int(input("Enter second number2 again: "))

print("\nBefore swapping: a =", a, ", b =", b)

# Method 2: Without using a temporary variable
a, b = b, a
print("After swapping without temp variable: a =", a, ", b =", b)
print()

#10) Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user. 
num = int(input("Enter a number for Even: "))
if num % 2 == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")


#11) Write a Python program to test whether a passed letter is a vowel or not. 
ch = input("Enter a single letter for vowl or not: ").lower()  # Convert to lowercase
if ch in ('a', 'e', 'i', 'o', 'u'):
    print(f"{ch} is a vowel.")
else:
    print(f"{ch} is not a vowel.")


 
