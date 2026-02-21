The Code
# Case Changing Methods

text = "tHis Is a MiXeD CaSe StRiNg."


# All upperase
print("UPPER:", text.upper())

# All lowercase
print("lower:", text.lower())

# First char uppercase
print("Capitilize:", text.capitalize())

# First char of each word uppercase
print("Title:", text.title())

# Swap upper/lower case
print("Swapcase:", text.swapcase())
Line-by-Line Explanation
1️⃣ Comment
# Case Changing Methods

This is a comment.
Python ignores it.

Its purpose is to describe what the code demonstrates.

2️⃣ Create a String
text = "tHis Is a MiXeD CaSe StRiNg."

This creates a variable named text.

Value stored:

tHis Is a MiXeD CaSe StRiNg.

This string intentionally has random capitalization to show how each method works.

3️⃣ Convert to Uppercase
print("UPPER:", text.upper())
text.upper()

This converts all letters in the string to uppercase.

Example transformation:

tHis Is a MiXeD CaSe StRiNg.

becomes

THIS IS A MIXED CASE STRING.
Output
UPPER: THIS IS A MIXED CASE STRING.
Practical Applications

Used for:

Standardizing data

Case-insensitive comparisons

Product codes

IDs

Database normalization

Example:

user_input.upper() == "YES"
4️⃣ Convert to Lowercase
print("lower:", text.lower())
text.lower()

Converts all letters to lowercase.

Result:

this is a mixed case string.
Output
lower: this is a mixed case string.
Practical Applications

Used in:

Search engines

username comparisons

filtering text

natural language processing

Example:

email = email.lower()

So that:

John@gmail.com
john@gmail.com

are treated the same.

5️⃣ Capitalize the Sentence
print("Capitilize:", text.capitalize())
text.capitalize()

Changes:

first character → uppercase

all other characters → lowercase

Result:

This is a mixed case string.
Output
Capitilize: This is a mixed case string.
Practical Applications

Used in:

formatting messages

sentence corrections

auto-formatting user input

chat systems

Example:

hello world → Hello world
6️⃣ Title Case
print("Title:", text.title())
text.title()

Capitalizes the first letter of each word.

Result:

This Is A Mixed Case String.
Output
Title: This Is A Mixed Case String.
Practical Applications

Used for:

book titles

article headings

UI labels

formatting names

Example:

harry potter and the goblet of fire
↓
Harry Potter And The Goblet Of Fire
7️⃣ Swap Case
print("Swapcase:", text.swapcase())
text.swapcase()

Reverses the case of every letter:

uppercase → lowercase

lowercase → uppercase

Example:

tHis Is a MiXeD CaSe StRiNg.

becomes

ThIS iS A mIxEd cAsE sTrInG.
Output
Swapcase: ThIS iS A mIxEd cAsE sTrInG.
Practical Applications

Used in:

debugging text issues

text transformations

security testing

programming exercises

Sometimes used in puzzles or encoding exercises.

Final Output of the Whole Program
UPPER: THIS IS A MIXED CASE STRING.
lower: this is a mixed case string.
Capitilize: This is a mixed case string.
Title: This Is A Mixed Case String.
Swapcase: ThIS iS A mIxEd cAsE sTrInG.
Key Programming Concepts Demonstrated
Strings

Text data in Python.

String Methods

Functions built into string objects.

Output formatting

Using print() with labels.

Data transformation

Changing text format without altering original data.

Important note:

These methods do not modify the original string.

Example:

print(text)

Still prints:

tHis Is a MiXeD CaSe StRiNg.

Because strings are immutable in Python.

Real-World Systems That Use This
Search engines

Convert everything to lowercase before searching.

Databases

Normalize user input.

Chat applications

Auto-correct formatting.

AI / NLP systems

Standardize text before analysis.

File systems

Normalize filenames.

Example preprocessing step:

text = text.lower().strip()
Short Summary

This code demonstrates how to:

Convert text to uppercase

Convert text to lowercase

Capitalize sentences

Capitalize each word

Reverse capitalization

These operations are fundamental in text processing, data cleaning, and software development.
