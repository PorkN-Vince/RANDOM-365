This program prints a right-aligned increasing triangle made of stars (*).
It demonstrates how to combine spaces and stars to control alignment.

If rows = 5, the output will be:

    *
   **
  ***
 ****
*****
🔎 Line-by-Line Explanation
1️⃣ Define the size
rows = 5

This controls the height of the triangle.

It also controls the maximum number of stars printed.

If you change it to rows = 3, the output becomes:

  *
 **
***
2️⃣ Create the loop
for level in range(1, rows + 1):

This generates:

1, 2, 3, 4, 5

level represents the current row number.

The loop runs 5 times.

3️⃣ The Print Statement
print(" " * (rows - level) + "*" * level)

This line builds each row in two parts:

▪ Part A: Left Spaces
" " * (rows - level)

This creates indentation.

For rows = 5:

level	spaces
1	4 spaces
2	3 spaces
3	2 spaces
4	1 space
5	0 spaces

As level increases, spaces decrease.

▪ Part B: Stars
"*" * level

This prints stars equal to the current row number.

level	stars
1	*
2	**
3	***
4	****
5	*****
🔁 Step-by-Step Execution
level = 1
    *
level = 2
   **
level = 3
  ***

And so on.

🧠 What the Program Does Conceptually

It:

Starts with many spaces and one star

Reduces spaces each row

Increases stars each row

Creates a right-aligned triangle

📚 Concepts Demonstrated

This program teaches:

Loops (for)

Range with start and stop

String multiplication

Alignment using spaces

Basic pattern mathematics

💡 Practical Applications

Even though this prints stars, the logic is widely used.

1️⃣ Text-Based UI Layout

Used in:

Console menus

Centered headings

Decorative layouts

2️⃣ Progress Indicators

Example:

    #
   ##
  ###
 ####
#####
3️⃣ Graphics Programming

The same idea applies to:

Pixel alignment

Right-justified text

Coordinate positioning

4️⃣ Data Formatting

Right-aligning numbers in tables uses similar spacing logic.

Example:

   5
  25
 300
4000
📌 Summary

Your code:

Sets the height of the triangle

Loops from 1 to that height

Prints decreasing spaces

Prints increasing stars

Forms a right-aligned growing triangle
