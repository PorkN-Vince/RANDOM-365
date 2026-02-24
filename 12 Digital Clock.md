This program creates a live digital clock window using Python’s built-in GUI library Tkinter.
It displays the current time and updates every second.

What the Program Does Overall

Creates a window.

Places a large text label in the middle.

Gets the current time from the system.

Updates the label every second.

Runs continuously like a real digital clock.

Line-by-Line Explanation
Import Tkinter
import tkinter as tk

This imports the Tkinter library and gives it the shorter name tk.

Why this is useful:

Instead of writing:

tkinter.Label()

you can write:

tk.Label()

Tkinter is used to create:

windows

buttons

menus

text displays

applications

Import time formatting function
from time import strftime

This imports the function strftime from Python’s time module.

strftime means:

string format time

It converts the current time into a readable string.

Example:

21:34:05
Create the main application window
root = tk.Tk()

This creates the main program window.

root is the base container that holds everything in the interface.

Without this line, there would be no window.

Set the window title
root.title("Digital Clock")

This changes the text shown at the top of the window.

The title bar will display:

Digital Clock
Create the clock label
clock_label = tk.Label(root, font=("Helvetica", 48), bg="black", fg="cyan")

This creates a label widget that will display the time.

Explanation of parameters:

Parameter	Meaning
root	parent window
font	text style and size
bg	background color
fg	text color

So the clock will appear:

• large font (48)
• black background
• cyan glowing text

Place the label inside the window
clock_label.pack(anchor="center", fill="both", expand=True)

pack() tells Tkinter where and how to place the widget.

Options used:

anchor="center"
Centers the label.

fill="both"
Allows the label to stretch horizontally and vertically.

expand=True
Allows it to grow if the window size increases.

Result:
The clock fills the entire window.

Define the update function
def update_time():

This creates a function that will:

Get the current time

Display it

repeat every second

Functions allow code to be reused.

Get the current system time
current_time = strftime("%H:%M:%S")

This formats the current time.

Format codes:

Code	Meaning
%H	hour (24-hour format)
%M	minutes
%S	seconds

Example result:

19:42:08
Update the label text
clock_label.config(text=current_time)

This changes the label content.

So the clock display becomes:

19:42:08

config() is used to modify widget settings after creation.

Schedule the next update
clock_label.after(1000, update_time)

This tells Tkinter:

Run update_time() again after 1000 milliseconds.

1000 milliseconds = 1 second

So the clock refreshes every second.

This creates a continuous loop without freezing the program.

Start the clock
update_time()

This runs the function the first time.

After that, .after() keeps calling it repeatedly.

Start the GUI program
root.mainloop()

This starts the Tkinter event loop.

The program now:

• listens for events
• updates widgets
• keeps the window open

Without this line, the window would close immediately.

What the Program Looks Like
-------------------------
|      Digital Clock     |
|                        |
|        20:14:33        |
|                        |
-------------------------

The time updates every second.

Programming Concepts Demonstrated

This small program teaches several important ideas.

GUI Programming

Creating graphical applications instead of console programs.

Functions

Organizing reusable logic.

Event Loops

Programs that continuously run and respond to events.

Scheduling Tasks

Using .after() to run tasks repeatedly.

Real-time Data Display

Updating information dynamically.

Practical Applications
1. Desktop Widgets

Clocks, calendars, weather widgets.

2. Dashboard Displays

Used in monitoring systems:

server dashboards

stock prices

analytics screens

3. Real-Time Monitoring Software

Programs that update information continuously:

CPU monitors

network activity

security monitoring

4. Time-Based Applications

Apps like:

timers

alarms

countdown clocks

productivity tools

5. Learning GUI Development

Tkinter is often the first step before learning advanced frameworks like PyQt or Kivy.

Simple Summary

Your code:

Opens a window

Displays the current time

Updates every second

Keeps running like a real digital clock
