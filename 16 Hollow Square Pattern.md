This Python program prints a hollow square pattern of stars (*). It teaches loops, conditional statements, and string manipulation.

If rows = 5, the output will look like:

*****
*   *
*   *
*   *
*****
Line-by-Line Explanation
1️⃣ Set the size of the square
rows = 5

This variable determines:

the height of the square

the width of the square

Changing rows to 3 will produce a smaller square:

***
* *
***
2️⃣ Start a loop over each row
for i in range(rows):

range(rows) produces numbers: 0, 1, 2, 3, 4

Each i represents the current row

The loop runs rows times (once per row)

3️⃣ Check if it's the first or last row
if i == 0 or i == rows - 1:

i == 0 → first row

i == rows - 1 → last row (5 - 1 = 4)

These rows are fully filled with stars to form the top and bottom of the square.

4️⃣ Print a full row of stars (top/bottom)
print("*" * rows)

* repeated rows times

For rows = 5, prints:

*****

This is the top or bottom border of the square.

5️⃣ Print hollow row (middle rows)
else:
    print("*" + " " * (rows - 2) + "*")

Explanation:

First * → left border

" " * (rows - 2) → middle spaces (empty)

rows - 2 because two stars occupy the ends

Last * → right border

For rows = 5:

*   *
Step-by-Step Example (rows = 5)
i	Condition	Output
0	first row	*****
1	middle	* *
2	middle	* *
3	middle	* *
4	last row	*****
Programming Concepts Demonstrated

Loops – Repeating code for each row.

Conditional Statements (if-else) – Different behavior for borders and middle rows.

String Multiplication – "*" repeated to create a pattern.

Basic Geometry in Programming – Understanding coordinates and spaces for shapes.

Practical Applications

Even though it prints a simple pattern, the logic is widely applicable.

1️⃣ UI / Console Design

Text-based menus

ASCII art borders

Layouts in terminal applications

Example:

+-------+
|       |
| MENU  |
|       |
+-------+
2️⃣ Game Development

Grid-based games

Map borders

Maze designs

3️⃣ Algorithm Practice

Loop and condition exercises

Prepares for more complex shapes and pattern problems

4️⃣ Data Visualization

Aligning data in rows and columns

Creating empty frames for charts

Summary

Your code:

Defines the square size (rows)

Loops over each row

Prints a full line of stars for top and bottom

Prints hollow lines for the middle

Creates a hollow square pattern
