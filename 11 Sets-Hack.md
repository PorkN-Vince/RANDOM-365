This Python code demonstrates how to use sets to compare two lists of numbers. It finds their union, intersection, difference, and symmetric difference, then prints the results in sorted order.

What the Program Does Overall

The program:

Stores two lists of numbers.

Converts them into sets.

Performs set operations to compare them.

Prints the results neatly.

These operations are common in data analysis, database comparisons, and filtering duplicates.

Line-by-Line Explanation
Create the first list
a = [21, -6, 26, 11, 1, 16]

This creates a list named a containing six numbers.

Example contents:

21, -6, 26, 11, 1, 16

Lists can contain duplicates and preserve order.

Create the second list
b = [17, 26, 7, 21, -2, 12]

This creates another list named b.

17, 26, 7, 21, -2, 12

Notice that 21 and 26 appear in both lists.

Union of the two lists
union = set(a) | set(b)
Step 1: Convert lists to sets
set(a)
set(b)

A set:

• removes duplicates
• ignores order
• allows mathematical set operations

Example:

set(a) = {21, -6, 26, 11, 1, 16}
set(b) = {17, 26, 7, 21, -2, 12}
Step 2: Union operator |

Union means:

all unique elements from both sets

Result:

{1, 7, 11, 12, 16, 17, 21, 26, -6, -2}
Intersection
intersection = set(a) & set(b)

Operator:

&

Intersection means:

values that appear in both lists

Common values:

21
26

So:

{21, 26}
Difference
difference = set(a) - set(b)

Operator:

-

Difference means:

values in a but NOT in b

From list a:

21, -6, 26, 11, 1, 16

Remove those that appear in b:

21
26

Remaining:

{-6, 11, 1, 16}
Symmetric Difference
symmetric_diff = set(a) ^ set(b)

Operator:

^

Symmetric difference means:

values that appear in one list but not both

So remove the common values (21 and 26).

Result:

{-6, 11, 1, 16, 17, 7, -2, 12}
Print the union
print(f"{sorted(union)=}")

sorted() sorts the numbers from smallest to largest.

Example output:

sorted(union)=[-6, -2, 1, 7, 11, 12, 16, 17, 21, 26]

The f string automatically prints the variable name and value.

Print intersection
print(f"{sorted(intersection)=}")

Output:

sorted(intersection)=[21, 26]
Print difference
print(f"{sorted(difference)=}")

Output:

sorted(difference)=[-6, 1, 11, 16]
Print symmetric difference
print(f"{sorted(symmetric_diff)=}")

Output:

sorted(symmetric_diff)=[-6, -2, 1, 7, 11, 12, 16, 17]
Final Output Example
sorted(union)=[-6, -2, 1, 7, 11, 12, 16, 17, 21, 26]
sorted(intersection)=[21, 26]
sorted(difference)=[-6, 1, 11, 16]
sorted(symmetric_diff)=[-6, -2, 1, 7, 11, 12, 16, 17]
Key Concepts Demonstrated
Lists

Ordered collections that can contain duplicates.

Sets

Unordered collections of unique values.

Set Operations

Mathematical comparisons between data collections.

Operation	Symbol	Meaning
Union	`	`
Intersection	&	common elements
Difference	-	elements only in first set
Symmetric difference	^	elements not shared
Practical Applications
1. Removing Duplicate Data

If two datasets contain repeated values, sets can clean them.

Example:

user IDs
product codes
email lists
2. Comparing Databases

Companies often compare two datasets to find:

• matching records
• missing records
• conflicts

Example:

registered users vs active users
3. Cybersecurity / Log Analysis

Security analysts compare logs to find anomalies.

Example:

known safe IPs
vs
current network traffic
4. Recommendation Systems

Streaming platforms compare preferences.

Example logic:

users who watched A
∩
users who watched B
5. Data Science

Set operations help analyze datasets quickly.

Used in:

• machine learning preprocessing
• cleaning datasets
• comparing experiment results

Simple Visual Example

List A

21  -6  26  11  1  16

List B

17  26  7  21  -2  12

Common section:

21   26

Everything combined:

-6 -2 1 7 11 12 16 17 21 26
