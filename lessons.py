LESSONS = [
    {
        "title": "1. Hello, World!",
        "theory": """\
Welcome to Python! Python is a beginner-friendly, readable programming language used in web development, data science, automation, AI, and more.

Every Python journey starts with printing text to the screen. The built-in print() function displays output.

Syntax:
  print("Your message here")

• Strings (text) are wrapped in quotes — single ' or double ".
• You can print numbers too: print(42)
• You can print multiple things: print("Age:", 30)
""",
        "example": '''\
print("Hello, World!")
print("Welcome to Python!")
print("The answer is", 42)
''',
        "exercise": "Print your name and your favourite number on separate lines.",
        "hint": 'Use print("...") twice — once for your name, once for the number.',
        "solution": '''\
print("Alice")
print(7)
''',
    },
    {
        "title": "2. Variables & Data Types",
        "theory": """\
A variable is a named container that stores a value. Python figures out the type automatically.

Core types:
  int    — whole numbers          e.g. age = 25
  float  — decimal numbers        e.g. price = 9.99
  str    — text (string)          e.g. name = "Bob"
  bool   — True or False          e.g. is_open = True
  None   — absence of value       e.g. result = None

Rules for variable names:
  • Start with a letter or underscore (_)
  • No spaces — use snake_case (my_variable)
  • Case-sensitive: name ≠ Name

Check a variable's type with type():
  print(type(age))   # <class 'int'>
""",
        "example": '''\
name     = "Alice"
age      = 30
height   = 5.7
is_happy = True
nothing  = None

print(name, age, height, is_happy, nothing)
print(type(name))
print(type(age))
print(type(height))
''',
        "exercise": "Create variables for your name, age, and whether you like coding (True/False). Print each one.",
        "hint": "name = \"...\"  |  age = ...  |  likes_coding = True",
        "solution": '''\
name = "Alice"
age = 20
likes_coding = True

print(name)
print(age)
print(likes_coding)
''',
    },
    {
        "title": "3. Strings in Depth",
        "theory": """\
Strings are sequences of characters. Python gives you many tools to work with them.

f-strings (formatted strings) — the modern way to embed values:
  print(f"Hello, {name}! You are {age} years old.")

Useful string methods:
  .upper()          → "hello" → "HELLO"
  .lower()          → "HELLO" → "hello"
  .strip()          → removes leading/trailing whitespace
  .replace(a, b)    → replaces all occurrences of a with b
  .split(sep)       → splits into a list by separator
  len(s)            → returns the number of characters

Indexing & slicing:
  s = "Python"
  s[0]      → "P"    (first character)
  s[-1]     → "n"    (last character)
  s[0:3]    → "Pyt"  (characters 0, 1, 2)
""",
        "example": '''\
name = "Alice"
city = "New York"

# f-string
print(f"Hello, {name}! You live in {city}.")

# Methods
msg = "  python is GREAT  "
print(msg.strip())
print(msg.strip().lower())
print(msg.strip().replace("GREAT", "awesome"))

# Slicing
word = "Hello"
print(word[0])     # H
print(word[-1])    # o
print(word[1:4])   # ell
print(len(word))   # 5
''',
        "exercise": "Ask for someone's first and last name (store in variables), then print a greeting using an f-string and their name in UPPERCASE.",
        "hint": 'full_name = first + " " + last  then use .upper() inside the f-string',
        "solution": '''\
first = "John"
last  = "Doe"
full_name = first + " " + last
print(f"Hello, {full_name.upper()}!")
''',
    },
    {
        "title": "4. Numbers & Math",
        "theory": """\
Python supports all standard arithmetic operations.

Operators:
  +   addition          10 + 3  = 13
  -   subtraction       10 - 3  = 7
  *   multiplication    10 * 3  = 30
  /   true division     10 / 3  = 3.333...
  //  floor division    10 // 3 = 3
  %   modulo            10 % 3  = 1   (remainder)
  **  exponentiation    2 ** 8  = 256

Augmented assignment:
  x += 5   same as  x = x + 5

The math module:
  import math
  math.sqrt(25)   → 5.0
  math.floor(3.7) → 3
  math.ceil(3.2)  → 4
  math.pi         → 3.14159...
  math.abs(-5)    → use built-in abs(-5) = 5

Order of operations follows standard PEMDAS/BODMAS.
""",
        "example": '''\
import math

a, b = 17, 5

print(a + b)   # 22
print(a - b)   # 12
print(a * b)   # 85
print(a / b)   # 3.4
print(a // b)  # 3
print(a % b)   # 2
print(a ** 2)  # 289

# math module
print(math.sqrt(144))   # 12.0
print(math.pi)
print(math.floor(4.9))  # 4
print(math.ceil(4.1))   # 5
''',
        "exercise": "Write a program that calculates the area and circumference of a circle with radius = 7. Use math.pi.",
        "hint": "area = pi * r**2    circumference = 2 * pi * r",
        "solution": '''\
import math

radius = 7
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
''',
    },
    {
        "title": "5. User Input",
        "theory": """\
input() pauses the program and waits for the user to type something.
It always returns a string.

Syntax:
  answer = input("Your prompt: ")

Since input() returns a string, convert it when you need a number:
  age = int(input("Enter your age: "))
  price = float(input("Enter price: "))

Common pattern:
  name = input("Name: ")
  age  = int(input("Age: "))
  print(f"Hello {name}, you are {age} years old.")

⚠️  In this app the editor replaces input() prompts — write your
    inputs as variables at the top so code can run without pausing.
""",
        "example": '''\
# Simulating input() — assign values directly to run in this editor
name = "Bob"
age  = int("25")   # normally: int(input("Age: "))

print(f"Hello, {name}!")
print(f"Next year you will be {age + 1}.")
''',
        "exercise": "Simulate asking for the user's name and birth year. Calculate and print their age (assume current year is 2026).",
        "hint": "age = 2026 - birth_year",
        "solution": '''\
name = "Carol"
birth_year = int("1998")   # simulated input

age = 2026 - birth_year
print(f"Hello, {name}! You are {age} years old.")
''',
    },
    {
        "title": "6. Conditionals",
        "theory": """\
Conditionals let your program make decisions.

if / elif / else:
  if condition:
      ...
  elif another_condition:
      ...
  else:
      ...

Python uses INDENTATION (4 spaces) to define blocks — no curly braces!

Comparison operators:
  ==   equal to
  !=   not equal
  >    greater than
  <    less than
  >=   greater than or equal
  <=   less than or equal

Logical operators:
  and  — both must be True
  or   — at least one must be True
  not  — inverts True/False

Ternary (one-liner):
  result = "pass" if score >= 60 else "fail"
""",
        "example": '''\
score = 82

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}  Grade: {grade}")

# Logical operators
age = 20
has_id = True
if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")

# Ternary
label = "adult" if age >= 18 else "minor"
print(label)
''',
        "exercise": "Write a program that classifies a temperature (in Celsius): below 0 = 'Freezing', 0-15 = 'Cold', 16-25 = 'Comfortable', above 25 = 'Hot'.",
        "hint": "Use if / elif / elif / else with the temperature value.",
        "solution": '''\
temperature = 18

if temperature < 0:
    label = "Freezing"
elif temperature <= 15:
    label = "Cold"
elif temperature <= 25:
    label = "Comfortable"
else:
    label = "Hot"

print(f"{temperature}°C is {label}")
''',
    },
    {
        "title": "7. Lists",
        "theory": """\
A list is an ordered, mutable collection of items.

Creating a list:
  fruits = ["apple", "banana", "cherry"]
  numbers = [1, 2, 3, 4, 5]
  mixed = [1, "hello", True, 3.14]

Indexing (0-based):
  fruits[0]    → "apple"
  fruits[-1]   → "cherry"  (last item)

Slicing:
  fruits[1:3]  → ["banana", "cherry"]

Common operations:
  len(fruits)            → 3
  fruits.append("mango") → adds to end
  fruits.insert(1, "kiwi") → inserts at index 1
  fruits.remove("banana")  → removes first occurrence
  fruits.pop()           → removes & returns last item
  fruits.pop(0)          → removes & returns item at index 0
  fruits.sort()          → sorts in-place
  sorted(fruits)         → returns new sorted list
  "apple" in fruits      → True

List comprehension (concise way to build lists):
  squares = [x**2 for x in range(1, 6)]  → [1, 4, 9, 16, 25]
""",
        "example": '''\
# Creating and indexing
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])    # apple
print(fruits[-1])   # date
print(fruits[1:3])  # ['banana', 'cherry']

# Modifying
fruits.append("elderberry")
fruits.insert(1, "apricot")
fruits.remove("banana")
print(fruits)

# Iteration
for fruit in fruits:
    print(fruit.upper())

# List comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)

# Useful functions
numbers = [3, 1, 4, 1, 5, 9, 2]
print(f"Min: {min(numbers)}  Max: {max(numbers)}  Sum: {sum(numbers)}")
print(sorted(numbers))
''',
        "exercise": "Create a list of 5 numbers. Print the list, its length, the largest value, and a new list with each number doubled.",
        "hint": "doubled = [x * 2 for x in numbers]",
        "solution": '''\
numbers = [4, 7, 2, 9, 1]

print("List:", numbers)
print("Length:", len(numbers))
print("Largest:", max(numbers))

doubled = [x * 2 for x in numbers]
print("Doubled:", doubled)
''',
    },
    {
        "title": "8. Loops",
        "theory": """\
Loops repeat a block of code.

for loop — iterate over a sequence or range:
  for item in collection:
      ...

  for i in range(5):        → 0, 1, 2, 3, 4
  for i in range(2, 10, 2): → 2, 4, 6, 8  (start, stop, step)

while loop — repeat while a condition is True:
  while condition:
      ...

Loop control:
  break    → exit the loop immediately
  continue → skip the rest of this iteration, go to next

enumerate() — get index AND value:
  for i, val in enumerate(fruits):
      print(i, val)

zip() — iterate two lists in parallel:
  for a, b in zip(list1, list2):
      ...
""",
        "example": '''\
# for with range
for i in range(1, 6):
    print(f"{i} * {i} = {i**2}")

# for over a list
colors = ["red", "green", "blue"]
for color in colors:
    print(color)

# enumerate
for idx, color in enumerate(colors):
    print(f"{idx}: {color}")

# while with break/continue
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue        # skip even numbers
    if n > 7:
        break           # stop after 7
    print(n, end=" ")
print()

# zip
names  = ["Alice", "Bob", "Carol"]
scores = [88, 72, 95]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
''',
        "exercise": "Using a for loop and range, print the multiplication table for 7 (7×1 through 7×10).",
        "hint": "for i in range(1, 11):  then print(f'7 x {i} = ...')",
        "solution": '''\
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")
''',
    },
    {
        "title": "9. Dictionaries",
        "theory": """\
A dictionary stores key-value pairs. Great for structured data.

Creating a dict:
  person = {"name": "Alice", "age": 30, "city": "NYC"}

Accessing values:
  person["name"]        → "Alice"
  person.get("email")   → None  (safe — won't crash if key missing)
  person.get("email", "N/A")  → "N/A"  (default value)

Modifying:
  person["age"] = 31          # update existing
  person["email"] = "a@b.com" # add new key
  del person["city"]          # delete a key
  person.pop("city")          # delete & return value

Iterating:
  for key in person:               → iterates keys
  for key, val in person.items():  → iterates key-value pairs
  person.keys()   → all keys
  person.values() → all values

Checking membership:
  "name" in person  → True
""",
        "example": '''\
# Create
student = {
    "name": "Bob",
    "age": 21,
    "grade": "B",
    "courses": ["Math", "Python", "Physics"]
}

# Access
print(student["name"])
print(student.get("email", "No email"))

# Modify
student["age"] = 22
student["email"] = "bob@example.com"
print(student)

# Iterate
for key, value in student.items():
    print(f"{key}: {value}")

# Check
print("courses" in student)   # True
print(len(student))           # number of keys
''',
        "exercise": "Create a dictionary representing a book (title, author, year, pages). Print each field with a label, then add a 'genre' key and print the updated dictionary.",
        "hint": 'book["genre"] = "Fiction"  then print(book)',
        "solution": '''\
book = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925,
    "pages": 180
}

for key, value in book.items():
    print(f"{key}: {value}")

book["genre"] = "Fiction"
print("\\nUpdated book:", book)
''',
    },
    {
        "title": "10. Functions",
        "theory": '''\
A function is a reusable block of code. Define it once, call it many times.

Defining a function:
  def function_name(parameters):
      ...
      return value

  def greet(name):
      return f"Hello, {name}!"

  print(greet("Alice"))   → Hello, Alice!

Default parameters:
  def greet(name, greeting="Hello"):
      return f"{greeting}, {name}!"

  greet("Bob")            → Hello, Bob!
  greet("Bob", "Hi")      → Hi, Bob!

Keyword arguments:
  greet(name="Carol", greeting="Hey")

Return values:
  Functions can return any value — or nothing (returns None).
  You can return multiple values: return x, y  → tuple

Scope:
  Variables defined inside a function are LOCAL — not visible outside.

Docstrings — document what your function does:
  def add(a, b):
      """Returns the sum of a and b."""
      return a + b
''',
        "example": '''\
# Basic function
def greet(name, greeting="Hello"):
    """Return a personalised greeting."""
    return f"{greeting}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))
print(greet(name="Carol", greeting="Hey"))

# Multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 7, 2, 9])
print(f"Min: {low}  Max: {high}")

# Recursive function
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))   # 120

# Lambda (anonymous function)
square = lambda x: x ** 2
print(square(7))   # 49
''',
        "exercise": "Write a function `celsius_to_fahrenheit(c)` that converts Celsius to Fahrenheit (F = c * 9/5 + 32). Test it with 0, 100, and 37.",
        "hint": "def celsius_to_fahrenheit(c):  return ...",
        "solution": '''\
def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return c * 9 / 5 + 32

for temp in [0, 100, 37]:
    f = celsius_to_fahrenheit(temp)
    print(f"{temp}°C = {f:.1f}°F")
''',
    },
    {
        "title": "11. Error Handling",
        "theory": """\
Errors (exceptions) crash your program. try/except lets you handle them gracefully.

Basic structure:
  try:
      risky code here
  except ExceptionType:
      handle the error
  else:
      runs if NO exception occurred
  finally:
      always runs (cleanup)

Common exception types:
  ValueError      — wrong type of value   e.g. int("abc")
  TypeError       — wrong type            e.g. "a" + 1
  ZeroDivisionError — dividing by zero
  IndexError      — list index out of range
  KeyError        — dict key not found
  FileNotFoundError — file doesn't exist

Catching any exception:
  except Exception as e:
      print(f"Error: {e}")

Raising your own exceptions:
  raise ValueError("Age cannot be negative")
""",
        "example": '''\
# Basic try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exceptions
def safe_int(value):
    try:
        return int(value)
    except ValueError:
        print(f"'{value}' is not a valid integer.")
        return None

print(safe_int("42"))
print(safe_int("hello"))

# else / finally
try:
    x = int("100")
except ValueError as e:
    print(f"Error: {e}")
else:
    print(f"Converted successfully: {x}")
finally:
    print("This always runs.")

# Raising an exception
def set_age(age):
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f"Caught: {e}")
''',
        "exercise": "Write a function `safe_divide(a, b)` that returns a/b, but catches ZeroDivisionError and returns None with a message.",
        "hint": "try: return a / b   except ZeroDivisionError: ...",
        "solution": '''\
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

print(safe_divide(10, 2))
print(safe_divide(5, 0))
''',
    },
    {
        "title": "12. Classes & OOP",
        "theory": """\
Object-Oriented Programming (OOP) organises code into objects that combine data (attributes) and behaviour (methods).

Defining a class:
  class Dog:
      def __init__(self, name, breed):   # constructor
          self.name = name               # instance attribute
          self.breed = breed

      def bark(self):                    # method
          return f"{self.name} says Woof!"

Creating instances (objects):
  d = Dog("Rex", "Labrador")
  print(d.bark())

Key concepts:
  __init__   — called automatically when you create an object
  self       — refers to the current object (like "this" in other languages)
  Attributes — data stored on the object (self.name)
  Methods    — functions defined inside the class

Inheritance — a child class extends a parent:
  class GuideDog(Dog):
      def guide(self):
          return f"{self.name} is guiding."

  g = GuideDog("Buddy", "Golden Retriever")
  print(g.bark())    # inherited from Dog
  print(g.guide())   # own method

__str__ — controls how the object is printed:
  def __str__(self):
      return f"Dog({self.name}, {self.breed})"
""",
        "example": '''\
class BankAccount:
    """A simple bank account."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            return None
        self.balance -= amount
        return self.balance

    def __str__(self):
        return f"Account({self.owner}, ${self.balance:.2f})"


# Using the class
acc = BankAccount("Alice", 100)
print(acc)
acc.deposit(50)
acc.withdraw(30)
print(acc)

# Inheritance
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest

sav = SavingsAccount("Bob", 200)
earned = sav.add_interest()
print(f"Interest earned: ${earned:.2f}")
print(sav)
''',
        "exercise": "Create a `Rectangle` class with width and height attributes, and methods `area()` and `perimeter()`. Create two rectangles and print their areas and perimeters.",
        "hint": "area = width * height   perimeter = 2 * (width + height)",
        "solution": '''\
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"

r1 = Rectangle(4, 6)
r2 = Rectangle(3, 9)

for r in [r1, r2]:
    print(f"{r}  Area: {r.area()}  Perimeter: {r.perimeter()}")
''',
    },

    # ── Lesson 13 ────────────────────────────────────────────────────
    {
        "title": "13. Tuples & Sets",
        "theory": """\
Tuples and sets are two more built-in collection types.

TUPLES
• Created with parentheses: coords = (10, 20)
• Immutable — you cannot change their contents after creation
• Great for fixed data (coordinates, RGB colours, function return values)
• Support indexing and slicing just like lists
• Unpacking:  x, y = (10, 20)

SETS
• Created with curly braces: colours = {"red", "green", "blue"}
• Unordered — no guaranteed position
• No duplicates — adding the same value twice keeps only one
• Very fast membership testing:  "red" in colours
• Useful set operations:
    a | b   → union (all items from both)
    a & b   → intersection (items in both)
    a - b   → difference (items in a but not b)

When to use each:
• Tuple  → ordered, fixed data that should not change
• Set    → unordered collection where uniqueness matters
• List   → ordered, mutable sequence
""",
        "example": '''\
# --- Tuples ---
point = (3, 7)
print("x:", point[0], " y:", point[1])

# Unpacking
x, y = point
print(f"Unpacked: x={x}, y={y}")

# Tuples as function return values
def min_max(numbers):
    return (min(numbers), max(numbers))

low, high = min_max([4, 1, 9, 2, 7])
print(f"Min={low}  Max={high}")

# --- Sets ---
fruits = {"apple", "banana", "cherry", "apple"}  # duplicate removed
print("Fruits:", fruits)
print("Has banana:", "banana" in fruits)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Union:       ", a | b)
print("Intersection:", a & b)
print("Difference:  ", a - b)

# Remove duplicates from a list using a set
words = ["hello", "world", "hello", "python", "world"]
unique = list(set(words))
print("Unique words:", sorted(unique))
''',
        "exercise": """\
1. Create a tuple called `dimensions` with values (1920, 1080).
   Unpack it into `width` and `height` and print them.

2. Create two sets:
     `set_a = {1, 2, 3, 4, 5}`
     `set_b = {4, 5, 6, 7, 8}`
   Print their union, intersection, and the items in set_a but not set_b.
""",
        "hint": "Union: a | b   Intersection: a & b   Difference: a - b",
        "solution": '''\
# Part 1
dimensions = (1920, 1080)
width, height = dimensions
print(f"Width: {width}  Height: {height}")

# Part 2
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print("Union:       ", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Only in A:   ", set_a - set_b)
''',
    },

    # ── Lesson 14 ────────────────────────────────────────────────────
    {
        "title": "14. List Comprehensions",
        "theory": """\
List comprehensions are a concise, Pythonic way to build lists.

Basic syntax:
    new_list = [expression  for item in iterable]

With a condition (filter):
    new_list = [expression  for item in iterable  if condition]

Examples:
    squares = [x**2 for x in range(10)]
    evens   = [x   for x in range(20)  if x % 2 == 0]

You can also nest them, though keep readability in mind:
    flat = [x for row in matrix for x in row]

Dictionary comprehensions work the same way:
    squared = {x: x**2 for x in range(5)}

Set comprehensions use curly braces:
    unique_lengths = {len(w) for w in words}

Why use them?
• Shorter and often faster than an equivalent for-loop + append
• Expressive — reads almost like plain English
• Great for transforming and filtering data in one line
""",
        "example": '''\
# Basic: squares of 0-9
squares = [x**2 for x in range(10)]
print("Squares:", squares)

# Filter: only even numbers
evens = [x for x in range(20) if x % 2 == 0]
print("Evens:", evens)

# Transform strings
words = ["hello", "world", "python"]
upper = [w.upper() for w in words]
print("Upper:", upper)

# Combining transform + filter
long_upper = [w.upper() for w in words if len(w) > 4]
print("Long words uppercased:", long_upper)

# Dict comprehension: word → length
lengths = {w: len(w) for w in words}
print("Lengths:", lengths)

# Flatten a 2-D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [n for row in matrix for n in row]
print("Flattened:", flat)
''',
        "exercise": """\
1. Use a list comprehension to create a list of the cubes of numbers 1–10.
2. Use a list comprehension to extract only the words longer than 4 characters
   from:  words = ["cat", "elephant", "dog", "giraffe", "ox"]
3. Use a dict comprehension to create {number: square} for numbers 1–5.
""",
        "hint": "Cube: x**3   Filter: if len(w) > 4   Dict comp: {k: v for ...}",
        "solution": '''\
# 1. Cubes
cubes = [x**3 for x in range(1, 11)]
print("Cubes:", cubes)

# 2. Long words
words = ["cat", "elephant", "dog", "giraffe", "ox"]
long_words = [w for w in words if len(w) > 4]
print("Long words:", long_words)

# 3. Dict comprehension
squares = {n: n**2 for n in range(1, 6)}
print("Squares dict:", squares)
''',
    },

    # ── Lesson 15 ────────────────────────────────────────────────────
    {
        "title": "15. File I/O",
        "theory": """\
Python can read and write files with the built-in `open()` function.

Opening a file:
    f = open("filename.txt", mode)

Common modes:
    "r"   read (default) — file must exist
    "w"   write — creates or overwrites
    "a"   append — adds to end of existing file
    "x"   exclusive create — fails if file already exists

Always use the `with` statement — it closes the file automatically:
    with open("data.txt", "w") as f:
        f.write("Hello!\\n")

Reading:
    f.read()        → entire file as one string
    f.readline()    → one line
    f.readlines()   → list of all lines

Writing:
    f.write(text)   → write a string (add \\n manually)
    f.writelines(list_of_strings)

Working with paths (Python 3.4+):
    from pathlib import Path
    p = Path("data.txt")
    text = p.read_text()
    p.write_text("content")
""",
        "example": '''\
import os

filename = "example.txt"

# --- Writing ---
with open(filename, "w") as f:
    f.write("Line 1: Hello\\n")
    f.write("Line 2: Python\\n")
    f.write("Line 3: File I/O\\n")

print("File written.")

# --- Reading entire file ---
with open(filename, "r") as f:
    content = f.read()
print("Full content:")
print(content)

# --- Reading line by line ---
with open(filename, "r") as f:
    for i, line in enumerate(f, 1):
        print(f"  Line {i}: {line.rstrip()}")

# --- Appending ---
with open(filename, "a") as f:
    f.write("Line 4: Appended!\\n")

# --- Read back to confirm ---
with open(filename, "r") as f:
    lines = f.readlines()
print(f"\\nTotal lines after append: {len(lines)}")

# Cleanup
os.remove(filename)
print("File deleted.")
''',
        "exercise": """\
Write a program that:
1. Creates a file called "notes.txt" and writes at least 3 lines of text to it.
2. Reads the file back and prints each line numbered (1. line text).
3. Appends one more line.
4. Prints the total line count.
(Optional: delete the file at the end with os.remove("notes.txt"))
""",
        "hint": 'Use `with open("notes.txt", "w") as f:` then `f.write(...)`. For reading use a for loop over the file object.',
        "solution": '''\
import os

filename = "notes.txt"

# Write
with open(filename, "w") as f:
    f.write("Python is fun\\n")
    f.write("File I/O is easy\\n")
    f.write("Practice makes perfect\\n")

# Read and print numbered
with open(filename, "r") as f:
    for i, line in enumerate(f, 1):
        print(f"{i}. {line.rstrip()}")

# Append
with open(filename, "a") as f:
    f.write("Keep learning!\\n")

# Count lines
with open(filename, "r") as f:
    total = len(f.readlines())
print(f"Total lines: {total}")

os.remove(filename)
''',
    },

    # ── Lesson 16 ────────────────────────────────────────────────────
    {
        "title": "16. Modules & Imports",
        "theory": """\
A module is simply a Python file. Importing lets you use code from other files
and from Python's large standard library.

Importing styles:
    import math             → use as math.sqrt(16)
    from math import sqrt   → use as sqrt(16)
    from math import *      → imports everything (avoid — pollutes namespace)
    import numpy as np      → alias for long names

Useful standard-library modules:
    math        → sqrt, floor, ceil, pi, e, log …
    random      → random(), randint(), choice(), shuffle() …
    os          → file/directory operations
    sys         → interpreter info, argv, exit …
    datetime    → dates, times, timedeltas
    json        → encode/decode JSON data
    re          → regular expressions

Creating your own module:
    # myutils.py
    def greet(name):
        return f"Hello, {name}!"

    # main.py
    from myutils import greet
    print(greet("World"))

`if __name__ == "__main__":` guard:
    Code inside this block only runs when the file is executed directly,
    not when it is imported by another file.
""",
        "example": '''\
# --- math ---
import math
print("pi:      ", math.pi)
print("sqrt(2): ", math.sqrt(2))
print("ceil(4.3):", math.ceil(4.3))

# --- random ---
import random
print("\\nRandom float:  ", random.random())
print("Random 1-10:   ", random.randint(1, 10))

colours = ["red", "green", "blue", "yellow"]
print("Random choice: ", random.choice(colours))

random.shuffle(colours)
print("Shuffled:      ", colours)

# --- datetime ---
from datetime import datetime, date
now = datetime.now()
print(f"\\nNow:   {now:%Y-%m-%d %H:%M:%S}")

today = date.today()
print(f"Today: {today}")

# --- json ---
import json
data = {"name": "Alice", "scores": [95, 87, 92]}
json_str = json.dumps(data, indent=2)
print("\\nJSON string:")
print(json_str)

loaded = json.loads(json_str)
print("Name from JSON:", loaded["name"])
''',
        "exercise": """\
1. Use the `math` module to print:
     • The value of pi to 6 decimal places
     • The hypotenuse of a right triangle with sides 3 and 4  (hint: math.hypot)

2. Use the `random` module to simulate rolling two 6-sided dice 5 times.
   Print each roll and the total.

3. Use `datetime.date.today()` to print how many days are left until
   1 January 2027.
""",
        "hint": "math.hypot(a, b)  |  random.randint(1, 6)  |  date(2027,1,1) - date.today()  → .days",
        "solution": '''\
import math
import random
from datetime import date

# 1. Math
print(f"pi = {math.pi:.6f}")
print(f"Hypotenuse of 3-4 triangle: {math.hypot(3, 4)}")

# 2. Dice rolls
print("\\nDice rolls:")
for _ in range(5):
    d1, d2 = random.randint(1, 6), random.randint(1, 6)
    print(f"  {d1} + {d2} = {d1 + d2}")

# 3. Days until 2027
target = date(2027, 1, 1)
today  = date.today()
days   = (target - today).days
print(f"\\nDays until 2027-01-01: {days}")
''',
    },
]
