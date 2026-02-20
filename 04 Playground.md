1️⃣ Swap Two Variables
a, b = b, a
What it does

This swaps the values of a and b.

How it works

Python evaluates the right side first:

(b, a)

Then assigns them to the left side:

a = b
b = a

But safely in one step.

Example
a = 5
b = 10

a, b = b, a

Result:

a = 10
b = 5
Practical Applications

Used in:

Sorting algorithms

Game programming

Value switching

Data rearrangement

Example (sorting):

if arr[i] > arr[j]:
    arr[i], arr[j] = arr[j], arr[i]
2️⃣ Reverse a String
reversed_s = s[::-1]
What it does

Creates a reversed version of the string s.

Explanation

Python slicing format:

[start : end : step]

Here:

[::-1]

means:

Start from end

Move backwards

Step = -1

Example
s = "hello"

Result:

"olleh"
Practical Applications

Used in:

Palindrome checking

Text processing

Data transformation

Cryptography basics

Example:

Original: 12345
Reverse: 54321
3️⃣ Palindrome Checker
is_palindrome = (s == s[::-1])
What it does

Checks whether a word reads the same forward and backward.

Step-by-step

Reverse the string

s[::-1]

Compare with original

s == reversed

Result becomes True or False.

Example
s = "racecar"

Result:

True
Practical Applications

Used in:

Input validation

Coding interviews

DNA sequence analysis

Word games

Data verification

Example apps:

Spell checkers

Puzzle games

4️⃣ Factorial Calculation
import math
factorial = math.prod(range(1, n + 1))
What it does

Calculates:

n!

Factorial of a number.

Explanation
range(1, n + 1)

Creates numbers:

1, 2, 3, ..., n

Then:

math.prod(...)

Multiplies all numbers together.

Example for n = 5:

1 × 2 × 3 × 4 × 5 = 120
Practical Applications

Used in:

Probability

Statistics

Machine learning

Combinatorics

Algorithms

Example:

Number of ways to arrange items:

n!
5️⃣ Flatten a Nested List
flat_list = [i for sub in lst for i in sub]
What it does

Turns a list of lists into a single list.

Example
lst = [[1,2], [3,4], [5,6]]

Result:

[1,2,3,4,5,6]
How it works

Loop structure:

for sub in lst
    for i in sub

Meaning:

Take each sublist

Take each item inside it

Practical Applications

Used in:

Data science

Data cleaning

Matrix operations

JSON processing

Web scraping

Example:

Combining multiple datasets.

6️⃣ Filter Even Numbers
evens = [x for x in range(10) if x % 2 == 0]
What it does

Creates a list of even numbers from 0–9.

Explanation
range(10)

Generates:

0 1 2 3 4 5 6 7 8 9

Condition:

x % 2 == 0

Means divisible by 2.

Result
[0, 2, 4, 6, 8]
Practical Applications

Used in:

Data filtering

Input validation

Number analysis

Data pipelines

Example:

Filtering valid user IDs or records.

7️⃣ Merge Two Dictionaries
merged_dict = {**d1, **d2}
What it does

Combines two dictionaries.

Example
d1 = {"a":1, "b":2}
d2 = {"c":3}

Result:

{'a':1, 'b':2, 'c':3}
Important Note

If keys overlap:

d1 = {"a":1}
d2 = {"a":5}

Result:

{'a':5}

Second dictionary overrides.

Practical Applications

Used in:

Config systems

API responses

Data merging

Software settings

Example:

Combining default settings + user settings.

8️⃣ Count Items in a List
from collections import Counter
item_counts = Counter(lst)
What it does

Counts how many times each element appears.

Example
lst = ["apple", "banana", "apple"]

Result:

{'apple': 2, 'banana': 1}
Practical Applications

Used in:

Data analysis

Word frequency

Log analysis

Market basket analysis

NLP (Natural Language Processing)

Example:

Counting most used words in tweets.

9️⃣ Remove Duplicates
unique_elements = set(lst)
What it does

Removes duplicate values from a list.

Example
lst = [1,2,2,3,3,4]

Result:

{1,2,3,4}

Note: sets do not preserve order.

Practical Applications

Used in:

Data cleaning

Removing repeated records

Database preparation

Machine learning preprocessing

🔟 Join List into a String
string_joined = ' '.join(lst)
What it does

Combines list items into one string separated by spaces.

Example
lst = ["Hello", "World"]

Result:

"Hello World"
Explanation
' '.join(lst)

Means:

Join items with " " between them.

Practical Applications

Used in:

Sentence generation

File writing

Chat messages

Data formatting

CSV creation

Example:

words → sentence
🧠 Big Picture

These lines demonstrate important Python concepts:

Concept	Example
Tuple unpacking	a, b = b, a
Slicing	s[::-1]
Boolean checks	palindrome
Built-in libraries	math, collections
List comprehensions	filtering / flattening
Dictionary merging	{**d1, **d2}
Sets	remove duplicates
String manipulation	.join()
