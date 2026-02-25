This program prints a double-sided star pattern (sometimes called a butterfly pattern or mirrored triangle pattern) using loops and string multiplication.

If rows = 5, the output looks like this:

*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

It creates:

• A top expanding shape
• A bottom shrinking shape
• A symmetric figure

Line-by-Line Explanation
1️⃣ Set number of rows
rows = 5

This controls the size (height) of the pattern.

If you increase it to 8, the pattern becomes larger.

TOP SECTION
2️⃣ Loop from 1 to rows
for level in range(1, rows + 1):

This loop runs:

1, 2, 3, 4, 5

Each number represents the current row (called level).

3️⃣ Print the row
print("*" * level + " " * (2 * (rows - level)) + "*" * level)

This line has three parts:

Part 1: Left stars
"*" * level

Prints stars on the left side.

Example:

level	left stars
1	*
2	**
3	***
4	****
5	*****
Part 2: Middle spaces
" " * (2 * (rows - level))

This prints spaces in the middle.

Why multiply by 2?

Because the pattern expands symmetrically from both sides.

Example when rows = 5:

level	rows - level	spaces
1	4	8 spaces
2	3	6 spaces
3	2	4 spaces
4	1	2 spaces
5	0	0 spaces

So the gap shrinks each row.

Part 3: Right stars
"*" * level

Prints the same number of stars again on the right side.

So the full line structure is:

[left stars] + [spaces] + [right stars]
Example Breakdown (Top Half)

For rows = 5:

level = 1
*        *
level = 2
**      **
level = 3
***    ***
level = 4
****  ****
level = 5
**********

The stars meet in the middle.

BOTTOM SECTION
4️⃣ Reverse loop
for level in range(rows - 1, 0, -1):

This counts backwards:

4, 3, 2, 1

We subtract 1 so the middle row isn’t printed twice.

5️⃣ Same print logic
print("*" * level + " " * (2 * (rows - level)) + "*" * level)

This recreates the shrinking pattern:

****  ****
***    ***
**      **
*        *
Final Output (rows = 5)
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

This creates a butterfly-like shape.

Programming Concepts Demonstrated

This simple program teaches:

1️⃣ Looping

Using for loops to repeat actions.

2️⃣ Reverse iteration

Using range(start, stop, step) with -1.

3️⃣ String multiplication
"*" * 4

creates:

****
4️⃣ Mathematical pattern logic

The spacing formula:

2 * (rows - level)

controls symmetry.

Why Multiply Spaces by 2?

Because there are stars on both sides.

If we only used:

rows - level

The center gap would shrink too slowly and look uneven.

Doubling it keeps the pattern balanced.

Practical Applications

Even though this prints stars, the logic behind it is important.

1️⃣ Grid-Based Game Design

Games use coordinate math like this for:

• positioning objects
• mirroring animations
• creating symmetric effects

2️⃣ Graphics & Rendering Engines

Modern engines (like those used by Unity Technologies and Epic Games) use similar coordinate symmetry logic when drawing:

• reflections
• particle effects
• mirrored sprites

3️⃣ Algorithm Training

Pattern problems like this are common in:

• coding interviews
• competitive programming
• computer science exams

They improve:

• logical thinking
• mathematical reasoning
• spatial visualization

4️⃣ Console UI Design

Text-based dashboards use similar spacing techniques to align:

• menus
• tables
• system monitors

Summary

Your program:

Sets a size (rows)

Builds a top expanding pattern

Builds a bottom shrinking pattern

Uses math to keep symmetry

Prints a butterfly-shaped star design
