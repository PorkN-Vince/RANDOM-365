This program ranks students based on their marks (scores) from highest to lowest and prints the results.

It demonstrates the use of:

Dictionaries

Sorting with sorted()

lambda functions

Looping through key–value pairs

🔎 Line-by-Line Explanation
1️⃣ Define the dictionary
students = {
    "Student 1": 85,
    "Student 2": 92,
    "Student 3": 78,
    "Student 4": 90,
}

This creates a dictionary called students.

Structure:

Key → Value
Name → Marks

So we have:

Student	Marks
Student 1	85
Student 2	92
Student 3	78
Student 4	90

A dictionary stores data as key–value pairs.

2️⃣ Sort the dictionary by marks
rank = sorted(students.items(), key=lambda x: x[1], reverse=True)

This is the most important line.

Let’s break it down.

▪ students.items()

This converts the dictionary into pairs:

[
 ('Student 1', 85),
 ('Student 2', 92),
 ('Student 3', 78),
 ('Student 4', 90)
]

Each item is a tuple:

(Name, Marks)
▪ sorted(...)

The sorted() function sorts items.

By default, it sorts alphabetically (by key).

But we override that using:

▪ key=lambda x: x[1]

This tells Python:

“Sort based on the second element of each tuple.”

Since:

x[0] → Student name
x[1] → Marks

We are sorting based on marks.

▪ reverse=True

This makes the sorting descending (highest first).

Without it, it would sort from lowest to highest.

Result of Sorting
[
 ('Student 2', 92),
 ('Student 4', 90),
 ('Student 1', 85),
 ('Student 3', 78)
]

Now they are ranked from highest to lowest.

3️⃣ Loop Through the Sorted List
for key, value in rank:

This loops through each tuple.

For example:

key = "Student 2"
value = 92
4️⃣ Print the Results
print(key, " got", value, " marks.")

Output:

Student 2 got 92 marks.
Student 4 got 90 marks.
Student 1 got 85 marks.
Student 3 got 78 marks.
🧠 What the Program Does Conceptually

Stores student marks in a dictionary

Converts dictionary into sortable format

Sorts students by marks

Prints ranking from highest to lowest

📚 Concepts Demonstrated

This program teaches:

1️⃣ Dictionaries

Storing structured data.

2️⃣ .items()

Accessing key–value pairs.

3️⃣ Sorting with a Custom Key

Using lambda functions.

4️⃣ Lambda Functions

Anonymous functions:

lambda x: x[1]
5️⃣ Reverse Sorting

Using reverse=True.

💡 Practical Applications

This logic is very common in real-world systems.

🎓 School Systems

Ranking students by marks

Generating merit lists

Scholarship selection

📊 Business Applications

Ranking employees by performance

Sorting products by sales

Ordering data by revenue

🏆 Competition Systems

Leaderboards

Game high scores

Contest rankings

📈 Data Analysis

Sorting data by:

Score

Price

Age

Rating

📌 Summary

Your program:

Uses a dictionary to store students and marks

Sorts them by marks using a lambda function

Prints them in ranked order

Demonstrates practical data processing
