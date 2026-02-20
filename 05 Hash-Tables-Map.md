Purpose of the Code

This program finds the first character in a string that appears only once.

Example:

"swiss miss"

Character counts:

s → many times
w → 1
i → many times

So the first unique character is:

w
Line-by-Line Explanation
Comment
#can be used to find things in the code....

This is a comment.
Python ignores it. It is used to explain what the code is for.

Input String
input_string = "swiss miss"

This stores the text that the program will analyze.

Variable:

input_string

Value:

"swiss miss"

This is the data the function will process.

Function Definition
def find_first_unique_char(text):

This creates a function named:

find_first_unique_char

Purpose of the function:

Accept a string (text)

Return the first character that appears only once.

Example call:

find_first_unique_char("hello")
Dictionary Creation
char_count = {}

This creates an empty dictionary.

Dictionary structure:

{ key : value }

It will store:

character : number_of_times_it_appears

Example later:

{
s: 4
w: 1
i: 2
}
First Loop – Count Characters
for char in text:

This loop goes through every character in the string.

For "swiss miss" it will read:

s
w
i
s
s
(space)
m
i
s
s
Check if Character Already Exists
if char in char_count:

This checks if the character is already stored in the dictionary.

Example:

char_count = { 's':1 }

If we encounter s again → it exists.

Increase Count
char_count[char] += 1

If the character already exists, increase its count by 1.

Example:

Before:

{'s': 1}

After another s:

{'s': 2}
Add New Character
else:
    char_count[char] = 1

If the character is seen for the first time, add it to the dictionary.

Example:

'w' → first time

Dictionary becomes:

{'s':1, 'w':1}
After First Loop

For:

"swiss miss"

Dictionary becomes something like:

{
's': 6,
'w': 1,
'i': 2,
' ': 1,
'm': 1
}

Now the program knows how many times each character appears.

Second Loop – Find First Unique
for char in text:

We loop through the string again.

Why?

Because we want the first unique character in the original order.

Check if Count Equals 1
if char_count[char] == 1:

This checks if the character appears only once.

Example:

'w' → count = 1

So it qualifies.

Return the Character
return char

The function immediately returns the first unique character it finds.

So execution stops here.

For the string:

swiss miss

The output becomes:

w
If No Unique Character Exists
return None

If the loop finishes and no unique character was found, return:

None

This means:

There is no unique character in the string.

Example:

"aabbcc"

Output:

None
Function Call
print(find_first_unique_char(input_string))

Steps happening here:

Call the function.

Pass "swiss miss" into it.

Function finds 'w'.

print() displays it.

Output:

w
Visual Flow of the Program
Input string
      ↓
Count characters
      ↓
Store counts in dictionary
      ↓
Scan string again
      ↓
Return first character with count = 1
Time Complexity (Important for Programming Interviews)

First loop:

O(n)

Second loop:

O(n)

Total:

O(n)

This is considered efficient.

Practical Applications

This concept is used in many real systems.

1. Text Processing

Finding unusual characters in text.

Example:

Spam detection

Data cleaning

typo detection

2. Compilers / Code Analysis

Finding unique tokens or symbols inside code.

Example tools:

linters

syntax analyzers

static code scanners

3. Cybersecurity / Log Analysis

Detecting anomalies in logs.

Example:

aaaaabaaaac

Unique event might signal:

attack

error

suspicious activity

4. Data Validation

Checking irregular data in datasets.

Example:

ID numbers
product codes
serial numbers
5. Search Algorithms

Used in interview problems and algorithm practice.

Popular problem:

First Non-Repeating Character in a String

Often asked in technical interviews.

Key Programming Concepts Demonstrated

Your code uses several important concepts:

Functions

Reusable block of code.

Dictionaries

Fast lookups.

Loops

Processing sequences.

Conditional Logic

Decision making.

Algorithm Thinking

Two-pass solution.

Small Improvement (Optional)

Python can shorten this using collections.

from collections import Counter

counts = Counter(text)


https://www.facebook.com/reel/2640184633025992
