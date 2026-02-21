The Code
rows = 5
for level in range(rows, 0, -1):
    print(" " * (rows - level) + "*" * (2 * level - 1))
Line-by-Line Explanation
1️⃣ Set the pyramid height
rows = 5

This variable determines how many lines the pattern will have.

So the program will print 5 rows.

If you change it:

rows = 8

the pyramid will become larger.

2️⃣ Loop from top to bottom
for level in range(rows, 0, -1):

This loop controls the current row being printed.

Understanding the range

range(start, stop, step)

Here:

start = rows
stop = 0
step = -1

So if rows = 5, the loop values are:

5
4
3
2
1

This is why the pyramid prints from largest row to smallest row.

3️⃣ Print spaces and stars
print(" " * (rows - level) + "*" * (2 * level - 1))

Each line is made from:

spaces + stars

This combination creates the inverted pyramid shape.

Part A — Leading spaces
" " * (rows - level)

This adds spaces before the stars to keep the shape centered.

Example values:

Level	Spaces
5	0
4	1
3	2
2	3
1	4

As the pyramid goes down, spaces increase.

Part B — Stars
"*" * (2 * level - 1)

This determines how many stars appear on each row.

Formula:

2 × level − 1

Example:

Level	Stars
5	9
4	7
3	5
2	3
1	1

This creates a symmetric triangle.

Step-by-Step Output
Level 5
*********
Level 4
 *******
Level 3
  *****
Level 2
   ***
Level 1
    *

Final result:

*********
 *******
  *****
   ***
    *

This is the inverse of a standard pyramid.

Why the Formula Works

The star counts follow odd numbers:

1
3
5
7
9

Using:

2n − 1

ensures the triangle remains centered and symmetrical.

Programming Concepts Demonstrated

This small code uses several core programming ideas:

Loops

Repeating a task multiple times.

Range with negative step

Counting backward.

String multiplication

Python allows repeating characters easily:

"*" * 5

Output:

*****
Mathematical pattern logic

Using formulas to control shapes.

Practical Applications

Even though this looks like a simple classroom example, the concepts apply to real software.

1️⃣ Graphics and Game Development

Game engines generate structures using loops and formulas.

Examples:

terrain generation

pixel art

procedural graphics

2️⃣ Terminal UI Design

Command-line programs often draw shapes like:

menus
progress bars
charts
trees
loading animations
3️⃣ Data Visualization in Console

You can use this logic to create text-based graphs.

Example:

Sales Trend
*********
 *******
  *****
   ***
    *
4️⃣ Algorithm Practice / Coding Interviews

Pattern problems test whether a programmer understands:

loops

indexing

mathematical logic

formatting

Many programming exams include similar questions.

5️⃣ Learning Computational Thinking

This teaches developers how to break a visual pattern into:

spaces
+
symbols
+
rules

That same thinking is used in:

UI rendering

layout systems

simulations

Quick Comparison

Normal pyramid:

    *
   ***
  *****
 *******
*********

Your code prints the inverted version:

*********
 *******
  *****
   ***
    *
