"""Module 7) DA - Introduction to Python Assignment
1) What are the types of Applications?
-> Python can be used to build many types of application because it is general purpose programming language.  Here main types of application
    ➤ Web Application :
    -> Websites and web based platforms.
    -> Bulit using framework like Django, Flask, FastAPI

	➤ Desktop GUI Application :
	-> Software with a graphical interface for PCs. 
	-> Build using libraries like Tkinter , PyQt

	➤ Data Science & Data Analysis Applications :
	-> Used for analyzing , visualizing , and  processing data.
	-> Tools : Pandas, Numpy, Matplotib, Seaborn.

	➤ Artificial Intelligence & Machine Learning Application :
	-> AI models , chatbots.
	-> Libraries : TensorFlow, Scikit-learn, PyTorch.

	➤ Game Development :
	-> Creating 2D/3D games.
	-> Libraries: Pygame, Panda 3D.
	-> Mobile Application:
	-> Mobile apps for Android / IOS (less common).
	-> Framework: Kivy ,BeeWarte

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
n = int(input("Enter how many terms: "))
a, b = 0, 1     
print(a, b, end=" ")

for i in range(2, n):   
    c = a + b           # next number = sum of previous two
    print(c, end=" ")
    a = b              
    b = c     

"""7) How memory is managed in Python? 
Python uses a dynamic memory management system that includes automatic garbage collection. The memory management in Python is primarily handled by the Python Memory Manager and Garbage Collector.

#8) What is the purpose continuing statement in python? 
 --> The continue statement is used inside loops (for or while) to skip the current iteration and move directly to the next iteration of the loop.
  -- It does not terminate the loop, unlike break.
  -- It just skips the remaining code in the current iteration."""

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

# Method 2: Without using a temporary variable
a = int(input("\nEnter first number1 again temp: "))
b = int(input("Enter second number2 again: "))

print("\nBefore swapping: a =", a, ", b =", b)
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


#12) Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 
a = int(input("Enter num1 : "))
b = int(input("Enter num2 : "))
c = int(input("Enter num3 : "))

if a==b or b==c or a==c:
    print("Two number are equals sum not possible")
else:
    print("Sum of three digit is: ",a + b + c)

#13) Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == b or a + b == 5 or abs(a - b) == 5:
    print(True)
else:
    print(False)

#14) Write a python program to sum of the first n positive integers
n = int(input("Enter a positive integer: "))

total = 0
for i in range(1, n + 1):
    total += i

print("Sum of the first", n, "positive integers is:", total)

#15) Write a Python program to calculate the length of a string. 
text = input("Enter a string: ")
length = len(text)
print("The length of the string is:", length)

# 16) Write a Python program to count the number of characters (character frequency) in a string 
text = input("Enter a string: ")
char_count = {} # Empty dict for count
for char in text:
    if char in char_count:
        char_count[char] += 1  # Increment count if already present
    else:
        char_count[char] = 1   # Add new character with count 1
print("Character frequency:")
for key, value in char_count.items():
    print(f"'{key}': {value}")

#17) What are negative indexes and why are they used? 
""" In Python, negative indexes are a way to access elements from the end of a sequence (like a string, list, or tuple) 
     instead of from the beginning.
    
   ➤ Why negative indexes are used
    1) Quick access to elements from the end without needing to calculate their position.
    2) Useful when length is unknown — avoids manual counting from the front.
    3) Works consistently with strings, lists, tuples, and other sequence types."""

#18) Write a Python program to count occurrences of a substring in a string. 
text = input("Enter the main string: ")
sub = input("Enter the substring to search: ")
count = text.count(sub) 
print(f"The substring '{sub}' appears {count} time(s) in the given string.")

#19) Write a Python program to count the occurrences of each word in a given sentence 
sentence = input("Enter a sentence: ")
sentence = sentence.lower()
words = sentence.split() # Split the sentence into words (.split() breaks a string into a list of words wherever it finds spaces.)

word_count = {} # Create a dictionary to store word counts
for word in words:
    if word in word_count:
        word_count[word] += 1  # Increment count
    else:
        word_count[word] = 1   # Add word with count 1
print("\nWord frequency:")
for word, count in word_count.items():
    print(f"'{word}': {count}")

#20) Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
new_str1 = str2[:2] + str1[2:] # Swap the first two characters of each string
new_str2 = str1[:2] + str2[2:]
result = new_str1 + " " + new_str2
print("Result:", result)

#21) Write a Python program to add 'in' at the end of a given string (length should be at least 3).
#  If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged. 

text = input("Enter a string: ")
if len(text) < 3:
    result = text  
elif text.endswith("ing"):
    result = text + "ly"  # Add 'ly' if it ends with 'ing'
else:
    result = text + "ing"  # Otherwise, add 'ing'
print("Result:", result)

#22) Write a Python function to reverses a string if its length is a multiple of 4. 
def reverse_if_multiple_of_4(s):
    if len(s) % 4 == 0:
        return s[::-1]  # Reverse string using slicing
    else:
        return s
print(reverse_if_multiple_of_4("abcd"))    
print(reverse_if_multiple_of_4("abcdef"))  
print(reverse_if_multiple_of_4("abcdefgh"))  

# 23)	Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
#  If the string length is less than 2, return instead of the empty string. 
def first_last_two(s):
    if len(s) < 2:
        return ""   
    else:
        return s[:2] + s[-2:]   # first 2 + last 2
print(first_last_two("Hello Python"))   
print(first_last_two("Hi"))     

# 24)	Write a Python function to insert a string in the middle of a string. 
def insert_middle(main_str, insert_str):
    middle = len(main_str) // 2
    # Insert the new string at the middle
    return main_str[:middle] + insert_str + main_str[middle:]
print(insert_middle("HelloWorld", "Python")) 

# 25)	What is List? How will you reverse a list? 
"""
➤ A list is a collection data type in Python.
➤ It can store multiple items in a single variable.
➤ Items can be of different data types (int, float, string, etc.).
➤ Lists are ordered, mutable (can be changed), and allow duplicates. 

➤ There are several ways:

1. Using reverse() method (in-place)
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)   # [5, 4, 3, 2, 1]


This changes the original list.

2. Using slicing [::-1] (creates new list)
numbers = [1, 2, 3, 4, 5]
rev = numbers[::-1]
print(rev)       # [5, 4, 3, 2, 1]


This returns a new reversed list, original remains same.
"""

# 26)	How will you remove last object from a list
"""
1. Using pop() (most common)
my_list = [10, 20, 30, 40]
my_list.pop()   # removes last element (40)
print(my_list)  # [10, 20, 30]


pop() removes and returns the last element.

You can also specify an index: my_list.pop(0) removes the first element.

2. Using slicing
my_list = [10, 20, 30, 40]
my_list = my_list[:-1]   # remove last element
print(my_list)           # [10, 20, 30]


Creates a new list without the last item.
"""
# 27)	Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [1]?
# Ans is 33

# 28)	Differentiate between append () and extend () methods? 
"""
1) append() Method

--> Adds a single element (object) to the end of the list.
--> If you append another list, it will be added as a nested list (not merged).

Example:

list1 = [1, 2, 3]
list1.append(4)  
print(list1)     

list1.append([5, 6])   
print(list1)           

2) extend() Method

--> Takes an iterable (like a list, tuple, string) and adds each element to the list individually.
--> It merges elements instead of nesting.

 Example:

list2 = [1, 2, 3]
list2.extend([4, 5])   # add multiple elements
print(list2)           # [1, 2, 3, 4, 5]

list2.extend("Hi")     # iterable string, adds each character
print(list2)           # [1, 2, 3, 4, 5, 'H', 'i']
"""

# 29)	Write a Python function to get the largest number, smallest num and sum of all from a list. 
def list_stats(numbers):
    largest = max(numbers)    
    smallest = min(numbers)   
    total = sum(numbers)      
    
    return largest, smallest, total
nums = [1, 3, 2, 4, 6,5]
largest, smallest, total = list_stats(nums)

print("Largest number:", largest)
print("Smallest number:", smallest)
print("Sum of all numbers:", total)

# 30)	How will you compare two lists? 
"""
1. Check if two lists are exactly equal (same elements in the same order)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [3, 2, 1]

print(list1 == list2)   # True  (same order & elements)
print(list1 == list3)   # False (order different)

2. Check if two lists have the same elements (ignoring order)
--> You can use sorting:

list1 = [1, 2, 3]
list2 = [3, 2, 1]

print(sorted(list1) == sorted(list2))  # True
"""

# 31)	Write a Python program to count the number of strings where the string  length is 2 or more and the first 
#    and last character are same from a given list of strings.
def match_strings(words):
    count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:  
            count += 1
    return count
string_list = ['abc', 'xyz', 'aba', 'aa', 'x']
print("Number of matching strings:", match_strings(string_list))

# 32)	Write a Python program to remove duplicates from a list. 
my_list = [1, 2, 3, 2, 4, 1, 5, 3]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

print("Original List:", my_list)
print("List without duplicates:", unique_list)

# 33)	Write a Python program to check a list is empty or not. 
def check_empty(lst):
    if len(lst) == 0:
        print("The list is empty")
    else:
        print("The list is not empty")
check_empty([])        # The list is empty
check_empty([10])      # The list is not empty

# 34)	Write a Python function that takes two lists and returns true if they have at least one common member. 
def common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True, item   
    return False, None
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]

result, common = common_member(a, b)
if result:
    print("Common element found:", common)
else:
    print("No common element")

# 35)  Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30. 
squares = [x**2 for x in range(1, 31)]
print("First 5 elements:", squares[:5])
print("Last 5 elements:", squares[-5:])

# 36)	Write a Python function that takes a list and returns a new list with unique elements of the first list. 
def unique_elements(lst):
    unique = []
    for item in lst:
        if item not in unique:   # check if not already added
            unique.append(item)
    return unique
numbers = [1, 2, 2, 3, 4, 4, 5, 1]
print("Original list:", numbers)
print("Unique elements:", unique_elements(numbers))

# 37)	Write a Python program to convert a list of characters into a string. 
chars = ['H', 'e', 'l', 'l', 'o']
result = ''.join(chars) # join() combines list elements into a single string
print("List:", chars)
print("String:", result)

# 38)	Write a Python program to select an item randomly from a list. 
import random
items = [10, 20, 30, 40, 50]
random_item = random.choice(items) # using random function
print("List:", items)
print("Randomly selected item:", random_item)

# 39)	Write a Python program to find the second smallest number in a list. 
def second_smallest(numbers):
    numbers.sort()       # sort the list
    return numbers[1]    # second element
nums = [10, 20, 4, 45, 99]
print("Second smallest number:", second_smallest(nums))

# 40)	Write a Python program to get unique values from a list 
numbers = [1, 2, 2, 3, 4, 4, 5, 1]

unique_values = list(set(numbers))
print("Unique values:", unique_values)

# 41)	Write a Python program to check whether a list contains a sub list 
main_list = [1, 2, 3, 4, 5, 6]
sub_list = [3, 4, 5]

main_length = len(main_list)
sub_length = len(sub_list)
is_found = False

for start_index in range(main_length - sub_length + 1):
    if main_list[start_index:start_index + sub_length] == sub_list: # This slices a portion of the main list equal to the size of sub_list.
        is_found = True
        break

print("Main List:", main_list)
print("Sub List:", sub_list)

if is_found:
    print("Sublist found inside the main list")
else:
    print("Sublist not found")


# 42)	Write a Python program to split a list into different variables. 
my_list = [10, 20, 30]
a, b, c = my_list
print("a =", a)
print("b =", b)
print("c =", c)

# 43)	What is tuple? Difference between list and tuple
"""
--> A tuple is a collection of ordered elements (like a list).
--> It can contain elements of different data types (numbers, strings, etc.).
--> But unlike lists, tuples are immutable → once created, you cannot change, add, or remove elements.
--> Tuples are written with parentheses ().

➤ Difference between List and Tuple

-------------------------------------------------------
Feature          | List                      | Tuple
-------------------------------------------------------
Syntax           | Written with []           | Written with ()
Mutability       | Mutable (can change)      | Immutable (cannot change)
Performance      | Slower, more memory       | Faster, memory efficient
Use Case         | Data may change           | Data must stay constant
Methods          | append(), remove(), etc.  | count(), index() only
"""

# 44)	Write a Python program to create a tuple with different data types. 
my_tuple = (10, 3.14, "Hello", True)

print("Tuple with different data types:", my_tuple)

# 45)	Write a Python program to unzip a list of tuples into individual lists
data = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*data) # zip is built in function
numbers = list(numbers) # convert list
letters = list(letters)
print("Original list of tuples:", data)
print("Numbers list:", numbers)
print("Letters list:", letters)

# 46)	Write a Python program to convert a list of tuples into a dictionary. 
data = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
my_dict = dict(data) # Built - in function
print("Original list of tuples:", data)
print("Converted dictionary:", my_dict)

# 47)	How will you create a dictionary using tuples in python? 
data = ((1, "red"), (2, "green"), (3, "blue"))
my_dict = dict(data)
print(my_dict)

# 48)	Write a Python script to sort (ascending and descending) a dictionary by value. 
my_dict = {"apple": 40, "banana": 10, "cherry": 30, "date": 20}
asc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))
desc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Ascending:", asc_sorted)
print("Descending:", desc_sorted)


# 49)	Write a Python script to concatenate following dictionaries to create a new one. 
dict1 = {1: "apple", 2: "banana"}
dict2 = {3: "cherry", 4: "date"}
dict3 = {5: "elderberry", 6: "fig"}

print("Original Dictionaries:")
print("dict1:", dict1)
print("dict2:", dict2)
print("dict3:", dict3)

new_dict = {}
for d in (dict1, dict2, dict3):   
    new_dict.update(d)
print("\nConcatenated Dictionary:", new_dict)

# 50)	Write a Python script to check if a given key already exists in a dictionary. 

my_dict = {"id": 101, "name": "Devendra", "age": 21}
key_to_check = "name"
if key_to_check in my_dict:
    print(f"Key '{key_to_check}' exists in the dictionary.")
else:
    print(f"Key '{key_to_check}' does not exist in the dictionary.")


#  51) Do You Traverse Through a Dictionary Object in Python? 
"""
➤ Yes you can traverse (iterate) through a dictionary in Python.
➤ Since a dictionary stores key–value pairs, you can loop over:
"""

# 52)	How Do You Check the Presence of a Key in A Dictionary? 
"""
➤ Using the in Operator 
my_dict = {"id": 101, "name": "Devendra", "age": 21}

if "name" in my_dict:
    print("Key exists")
else:
    print("Key does not exist"

➤ Using .keys()
my_dict = {"id": 101, "name": "Devendra", "age": 21}
if "age" in my_dict.keys():
    print("Key exists")
"""
# 53)	Write a Python script to print a dictionary where the keys are numbers between 1 and 15. 
my_dict = {}
for i in range(1, 16):
    my_dict[i] = i * i

print("Dictionary with squares:", my_dict)

# 54)	Write a Python program to check multiple keys exists in a dictionary 
my_dict = {"id": 101, "name": "Devendra", "age": 21, "city": "Ahmedabad"}
keys_to_check = ["id", "age"]
if all(key in my_dict for key in keys_to_check):
    print("All keys exist")
else:
    print("Some keys are missing")


# 55)	Write a Python script to merge two Python dictionaries 
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = dict1.copy()   # make a copy so dict1 is not changed
merged.update(dict2)

print("Merged Dictionary:", merged)

# 56)	Write a Python program to map two lists into a dictionary 
keys = ["name", "age", "city"]
values = ["Devendra", 21, "Ahmedabad"]
my_dict = dict(zip(keys, values)) # zip(keys, values) → pairs each element from keys with each element from values or dict its convert in dictionary
print("Mapped Dictionary:", my_dict)

# 57)	Write a Python program to find the highest 3 values in a dictionary 
my_dict = {'a': 50, 'b': 200, 'c': 400, 'd': 100, 'e': 700}
values = list(my_dict.values()) # Convert in list
values.sort(reverse=True)
print("Top 3 highest values:", values[:3])

# 58)	Write a Python program to combine values in python list of dictionaries. 
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, o {'item': 'item1', 'amount': 750}] 
# Expected Output: Counter ({'item1': 1150, 'item2': 300}) 

# 59)	Write a Python program to create a dictionary from a string. Note: Track the count of the letters from the string. 
string = "Hello"
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1  # increase count if already exists
    else:
        char_count[char] = 1   # set count = 1 if first time
print("String:", string)
print("Character count dictionary:", char_count)

# 60)	Sample 	string: 'w3resource' Expected output: {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1} 
string = "w3resource"
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] += 1  # increase count if already exists
    else:
        char_count[char] = 1   # set count = 1 if first time
print("String:", string)
print("Character count dictionary:", char_count)

# 61)	Write a Python function to calculate the factorial of a number (a nonnegative integer) 
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
num = 5
print("Factorial of", num, "is:", factorial(num))

# 62)	Write a Python function to check whether a number is in a given range 
def check_in_range(num, start, end):
    if start <= num <= end:
        print(num, "is in the range", start, "to", end)
    else:
        print(num, "is NOT in the range", start, "to", end)
check_in_range(7, 5, 15)
check_in_range(20, 1, 10)

# 63)	Write a Python function to check whether a number is perfect or not. 
def is_perfect(num):
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i

    if divisor_sum == num:
        print(num, "is a Perfect Number")
    else:
        print(num, "is NOT a Perfect Number")
is_perfect(6)  # 6 = 1+2+3 → Perfect Number
is_perfect(12) # 12 ≠ 1+2+3+4+6 → NOT Perfect Number

# 64)	Write a Python function that checks whether a passed string is palindrome or not 
def is_palindrome(s):
    s = s.lower()
    if s == s[::-1]:  # Compare string with its reverse
        print(s, "is a Palindrome")
    else:
        print(s, "is NOT a Palindrome")
is_palindrome("madam")
is_palindrome("hello")

# 65)	How Many Basic Types of Functions Are Available in Python? 
""""
➤ 1. Built-in Functions

-> These are already provided by Python.
-> You can use them directly without defining them.

Examples:

-> print() → prints output
-> len() → finds length of string, list, etc.
-> type() → shows type of variable
-> max(), min(), sum(), range() etc.

➤  2. User-defined Functions

-> These are functions created by the programmer using the def keyword.
-> Purpose: Reuse code, make program cleaner.

Example:

def greet(name):
    return "Hello, " + name
print(greet("Dev"))

"""

# 66)	How can you pick a random item from a list or tuple? 
#For list 
import random
my_list = [10, 20, 30, 40, 50]
item = random.choice(my_list)
print("Random item from list:", item)

# For tuple
import random
my_tuple = ('apple', 'banana', 'cherry', 'mango')
item = random.choice(my_tuple)
print("Random item from tuple:", item)

# 67)	How can you pick a random item from a range? 
import random
num = random.randrange(10)
print("Random number:", num)

# 68)	How can you get a random number in python? 
import random
num = random.random()
print("Random float between 0 and 1:", num)


# 69)	How will you set the starting value in generating random numbers? 
import random
print(random.randint(1, 100))  # different every time

# 70)	How will you randomize the items of a list in place? 
import random
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list) # Shuffle the list in place
print("Shuffled list:", my_list)

# 71)	What is File function in python? What are keywords to create and write file. 
""" 
--> In Python, file functions are used to create, read, write, and close files.
The most common built-in function for handling files is open().

--> Syntax:
file_object = open(filename, mode)

--> filename → Name of the file (e.g., "data.txt")
--> mode → Tells Python what you want to do with the file

➤ Functions 

"r" -->	Read (default)  opens file for reading, error if file doesn’t exist
"w" --> Write creates a new file or overwrites if file exists
"a"	--> Append  adds content at the end of the file
"x"	--> Create  creates a new file, error if it already exists
"r+"--> Read + Write
"w+"--> Write + Read (overwrites file)
"a+"--> Append + Read
"""

# 72)	Write a Python program to read an entire text file. 
with open(r"E:\Tops technology\pyfile\pythonfile.txt", "r") as f:
    content = f.read()
    print(content)

# 73)	Write a Python program to append text to a file and display the text. 
with open(r"E:\Tops technology\pyfile\pythonfile.txt", "a") as f:
    f.write("\nThis is the newly appended line.")
with open(r"E:\Tops technology\pyfile\pythonfile.txt", "r") as f:
    content = f.read()
    print("Updated File Content:\n")
    print(content)

# 74)	Write a Python program to read first n lines of a file. 
n = int(input("Enter number of lines to read: "))

# Open the file in read mode
with open(r"E:\Tops technology\pyfile\pythonfile.txt", "r") as f:
    lines = f.readlines()

    # Case 1: n is less than or equal to total lines
    if n <= len(lines):
        for i in range(n):
            print(lines[i], end="")

    # Case 2: n is greater than total lines
    else:
        for line in lines:   # print all available lines
            print(line, end="")
        print(f"\n\nOnly {len(lines)} lines available, you asked for {n}.")


# 75)	Write a Python program to read last n lines of a file
n = int(input("\nEnter number of lines to read from the end: "))

# Open the file in read mode
with open(r"E:\Tops technology\pyfile\pythonfile.txt", "r") as f:
    lines = f.readlines()
    total = len(lines)
    if n <= total: # Case 1: if user asked less than or equal to total lines
        for i in range(total - n, total):   # start from last n lines
            print(lines[i], end="")

    else:    # Case 2: if user asked more than total lines
        for line in lines:   # print all available lines
            print(line, end="")
        print(f"\n\nOnly {total} lines available, you asked for {n}.")

# 76)	Write a Python program to read a file line by line and store it into a list 
lines = []   # empty list
with open(r"E:\Tops technology\pyfile\filelist.txt", "r") as f:
    for line in f:                  # read file line by line
        lines.append(line.strip())  

print("File content stored in list:")
print(lines)

# 77) Write a Python program to read a file line by line store it into a variable. 
with open(r"E:\Tops technology\pyfile\filelist.txt", "r") as f:
    # Use strip() to remove \n from each line because When Python reads each line, the newline character (\n) is part of that line 
    #  (except maybe the last one if the file doesn’t end with a newline).
    data = [line.strip() for line in f.readlines()] 
    print("File content stored in variable:")
print(data)


# 78)	Write a python program to find the longest words. 
with open(r"E:\Tops technology\pyfile\filelist.txt", "r") as f:
    words = f.read().split()   # split file into words
longest_word = words[0]
for w in words:
    if len(w) > len(longest_word):
        longest_word = w
print("Longest word:", longest_word)
print("Length:", len(longest_word))

# 79)	Write a Python program to count the number of lines in a text file. 
with open(r"E:\Tops technology\pyfile\filelist.txt", "r") as f:
    count = 0
    for line in f:  
        count += 1  
print("Total number of lines in file:", count)

# 80)	Write a Python program to count the frequency of words in a file. 
with open(r"E:\Tops technology\pyfile\filelist.txt", "r") as f:
    text = f.read()   
words = text.split()
freq = {} # dictionary to store word frequency
for w in words:
    w = w.lower()  # optional: convert to lowercase
    freq[w] = freq.get(w, 0) + 1  # increase count 
    # The get() method in Python dictionaries is used to safely fetch a value for a key.
print("Word Frequency in File:")
for key, value in freq.items():
    print(key, ":", value)

# 81)	Write a Python program to write a list to a file. 
foods = ["Pizza", "Burger", "Pasta", "Sandwich"]
with open(r"E:\Tops technology\pyfile\listfile.txt", "a") as f:
    for item in foods:
        f.write(item + "\n")
print("List appended successfully.")

# 82)	Write a Python program to copy the contents of a file to another file
with open(r"E:\Tops technology\pyfile\pythonfile.txt", "r") as f1:
    data = f1.read()      # read whole content at once
with open(r"E:\Tops technology\pyfile\copyfile.txt", "w") as f2:
    f2.write(data)     
print("File copied successfully!")
with open(r"E:\Tops technology\pyfile\copyfile.txt", "r") as f1:
    data = f1.read()      # read whole content at once
    print(data)

# 83)	Explain Exception handling? What is an Error in Python? 
"""
➤  Exception handling 
--> Exception handling is the process of catching errors and allowing the program to continue instead of crashing.
--> In Python, we use try - except - else - finally for handling exceptions.

➤ Error  
--> An error is something that stops your Python program from running correctly.
--> It means Python doesn't understand what you wrote (or it can't execute it).
--> Two types of error
1) Syntax error --> mistake in writing code
2) Runtime error --> Code is written correctly → but when running, something goes wrong (like 10 / 0)
"""

# 84)	How many except statements can a try-except block have? Name Some built-in exception classes: 
""" 
-> A try block in Python can have multiple except statements.
-> Each except handles a different type of error (exception class).
-> Python checks them top to bottom and runs the first one that matches.
-> Some built-in function given below:
    -> ZeroDivisionError
    -> TypeError
    -> ValueError
    -> Index Error
    -> KeyError (Accessing missing key in a dictionary)
    -> FileNotFoundError (Trying open not existing file)
"""

# 85)	When will the else part of try-except-else be executed? 
"""
-> The else block is executed only if no exception occurs in the try block.
-> That is, if the code inside try runs successfully without raising any errors, the else block will run.
-> If an exception occurs in try, the else block is skipped, and the matching except block is executed instead.
"""

# 86)	Can one block of except statements handle multiple exception? 
"""
-> In Python, a single except block can handle multiple exception types by specifying them as a tuple.
-> If any of the exceptions in the tuple occurs, that except block will execute.

➤ Example 
try:
    num = int("abc")      # Raises ValueError
    result = "10" + 5     # Raises TypeError
except (ValueError, TypeError): #Because in paranthese so its called tuple
    print("Caught either ValueError or TypeError")
"""

# 87)	When is the finally block executed? 
"""
-> The finally block is always executed, regardless of whether an exception occurs or not in the try block.
-> It is used to clean up resources, like closing files, releasing network connections, or freeing memory.
"""

# 88)	What happens when "1" == 1 is executed? 
# -> Since their types are different, the comparison returns False.

# 89)	How Do You Handle Exceptions with Try/Except/Finally in Python? Explain with coding snippets. 
"""
Python provides a structured way to handle errors using:
-> try block → Write code that might raise an exception.
-> except block → Handle specific exceptions that occur in the try block.
-> finally block → Always execute code, whether an exception occurs or not (commonly used for cleanup).
 
➤ Example 
try:
    num = 10 / 0
except ZeroDivisionError:
    print(" Error: Cannot divide by zero")
finally:
    print("This block always runs.")
"""

# 90)	Write python program that user to enter only odd numbers, else will raise an exception. 
try:
    num = int(input("Enter an odd number: ")) 
    if num % 2 == 0:                           
        raise Exception("Error: This is not an odd number!")
    else:
        print(f"Good! You entered odd number: {num}")
except ValueError:
    print("Error: Invalid input! Please enter an integer.")
except Exception as e:
    print(e)
finally:
    print("Program finished.")
