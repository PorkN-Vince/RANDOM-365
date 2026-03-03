This program is an infinite random fact generator.
Every time the user presses Enter, it displays a new random fact.

It demonstrates:

Using external libraries

Infinite loops

User interaction

String formatting

🔎 Line-by-Line Explanation
1️⃣ Import the library
import randfacts

This imports the external Python package randfacts.

randfacts is a library that:

Fetches random facts

Optionally filters inappropriate content

⚠️ Note: This library must be installed using:

pip install randfacts
2️⃣ Print program title
print("---- Infinite Fact Generator ----")

This simply prints a header so the user knows what the program does.

Output:

---- Infinite Fact Generator ----
3️⃣ Infinite Loop
while True:

This creates an infinite loop.

Meaning:

The program will keep running forever

It will only stop if manually terminated (Ctrl+C)

4️⃣ Wait for User Input
input("Press Enter to get a random fact...")

This:

Pauses the program

Waits until the user presses Enter

Does not store the input

It simply acts as a trigger.

5️⃣ Get a Random Fact
fact = randfacts.get_fact(filter_enabled=True)

This calls the function:

randfacts.get_fact()

The parameter:

filter_enabled=True

Means:

Inappropriate or offensive facts are filtered out

The fact returned is safer for general audiences

Example returned fact:

Honey never spoils.
6️⃣ Print the Fact
print("Did you know? " + fact)

This prints:

Did you know? Honey never spoils.
7️⃣ Print Divider Line
print("-" * 30)

This prints:

------------------------------

It separates each fact visually.

🧠 What the Program Does Conceptually

Shows a title

Enters infinite loop

Waits for user to press Enter

Fetches a random fact

Prints it

Repeats forever

📚 Concepts Demonstrated

This program teaches:

1️⃣ External Libraries

Using third-party packages.

2️⃣ Infinite Loops

while True for continuous programs.

3️⃣ User Interaction

Using input() to pause execution.

4️⃣ Function Calls

Calling get_fact() from a module.

5️⃣ String Multiplication

"-" * 30 to create a divider.

💡 Practical Applications

Even though this prints fun facts, the structure is powerful.

📱 Chatbots

Similar logic is used in:

Chat systems

AI assistants

Interactive bots

🎮 Games

Used for:

Random events

Random tips

Loading screen trivia

📊 Educational Tools

Apps that:

Display daily facts

Show motivational quotes

Provide trivia questions

🌐 API-Based Applications

The pattern:

get data → display → repeat

Is used in:

Weather apps

News feeds

Stock trackers

📌 Summary

Your program:

Imports an external fact generator

Runs forever using while True

Waits for user interaction

Fetches a safe random fact

Prints it neatly
