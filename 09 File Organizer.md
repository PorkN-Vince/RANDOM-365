This program is a simple desktop file organizer with a graphical interface. It lets a user choose a folder, then automatically sorts the files inside it into categories like Images, Documents, Audio, and Code.

I’ll explain it line by line and also what each part is used for in real life.

1. Program Title Comment
# Simple File Organizer

This is just a comment.
Comments explain the code but are ignored by Python.

Purpose: Helps developers understand what the program does.

2. Importing Libraries
import tkinter as tk
from tkinter import filedialog
import os, shutil
tkinter

Used to create the window (GUI).

as tk is just a shorter name so we can type tk instead of tkinter.

filedialog

Allows the user to select a folder using a popup window.

os

Used for working with files and folders.

Examples:

reading folders

creating directories

checking paths

shutil

Used for moving files.

Practical use:
Programs like this use these libraries to build desktop utilities.

3. Create the Main Window
root = tk.Tk()

Creates the main application window.

Think of this as:

starting the GUI program.

4. Window Title
root.title("File Organizer")

Sets the title at the top of the window.

Result:

File Organizer
5. Window Size
root.geometry("400x200")

Sets the window size.

Width = 400 pixels
Height = 200 pixels

6. Background Color
root.configure(bg="#000")

Changes background color.

#000 = black.

7. Status Text Variable
status_var = tk.StringVar(value="Ready to organize files.")

This creates a dynamic text variable.

Why use this?

Because we want to change the message later without recreating the label.

Initial text:

Ready to organize files.
8. Status Label
tk.Label(root, textvariable=status_var, bg="#111", fg="#0ff", font=("Arial", 16, "bold"), height=2).pack(fill="x", padx=10, pady=20)

Creates a label that shows messages.

Explanation:

textvariable=status_var → displays the variable

bg="#111" → dark background

fg="#0ff" → cyan text

font=("Arial",16,"bold") → style

height=2 → label height

.pack() → places it in the window

Spacing:

padx=10 horizontal padding

pady=20 vertical padding

9. File Categories Dictionary
TYPES ={
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Code": [".py", ".js", ".html", ".css", ".java"]
}

This dictionary defines how files will be sorted.

Example:

.jpg → Images folder
.pdf → Documents folder
.mp3 → Audio folder
.py → Code folder

Structure:

Category : List of file extensions

Example result in a folder:

Downloads
 ├ Images
 ├ Documents
 ├ Audio
 └ Code
10. Function That Organizes Files
def organize_files(event):

This function runs when the user clicks the button.

event is passed because the button is using a mouse click binding.

11. Ask User to Choose Folder
folder = filedialog.askdirectory()

Opens a dialog like:

Select Folder

User chooses a directory.

Example:

Downloads
Desktop
Documents
12. Cancel Protection
if not folder: return

If the user cancels, the function stops.

Prevents errors.

13. Counter
count = 0

Counts how many files were moved.

14. Loop Through Files
for file in os.listdir(folder):

Reads every file in the selected folder.

Example list:

photo.jpg
song.mp3
report.pdf
script.py
15. Ignore Files Without Extensions
if "." not in file: continue

If there is no file extension, skip it.

Example skipped:

README
LICENSE
16. Get File Extension
ext = os.path.splitext(file)[1].lower()

Breakdown:

splitext() splits filename into:

("photo", ".jpg")

[1] gets the extension.

.lower() ensures:

.JPG
.jpg
.Jpg

all become

.jpg
17. Loop Through Categories
for category, extensions in TYPES.items():

Example iteration:

category = Images
extensions = [.jpg, .png, .gif]
18. Check if File Matches Category
if ext in extensions:

Example:

.jpg in Images list → TRUE
19. Create Folder Path
target_dir = os.path.join(folder, category)

Example:

Downloads + Images

Result:

Downloads/Images
20. Create Folder if Missing
if not os.path.exists(target_dir): os.makedirs(target_dir)

If the folder doesn’t exist, create it.

Example:

Downloads/Images
21. Move File
shutil.move(os.path.join(folder, file), os.path.join(target_dir, file))

Moves file.

Example:

Before

Downloads/photo.jpg

After

Downloads/Images/photo.jpg
22. Increase Counter
count += 1

Tracks how many files were organized.

23. Stop Checking Other Categories
break

Once matched, exit the category loop.

Prevents duplicate moves.

24. Update Status Message
status_var.set(f"Moved {count} files.")

Changes the GUI message.

Example output:

Moved 23 files.
25. Create Frame
frame = tk.Frame(root, bg="#000")
frame.pack(pady=20)

A container to hold the button.

26. Button Text
btn_text = "SELEVT FOLDER"

Text displayed on the button.

There’s a small typo — should be SELECT.

27. Create Button (Styled Label)
btn_widget = tk.Label(frame, text=btn_text, bg="#f39c12", fg="white", font=("Arial", 14, "bold"), width=20, height=2, relief = "flat")

This is a label styled like a button.

Color:

Orange background

White text

28. Mouse Click Event
btn_widget.bind("<Button-1>", organize_files)

When the user clicks:

Left Mouse Button

Run:

organize_files()
29. Show the Button
btn_widget.pack()

Displays it in the window.

30. Info Text
tk.Label(root, text="Sorts: Images, Documents, Audio, Code.", bg="#000", fg="#555", font=("Arial", 10)).pack(side="bottom", pady=10)

Adds a description at the bottom.

31. Start the App
root.mainloop()

This starts the program loop.

Without this, the window would instantly close.

Final Program Flow

Window opens

User clicks SELECT FOLDER

Chooses a directory

Program scans files

Files get sorted into folders

Status message updates

Practical Real-World Applications
1. Cleaning Downloads Folder

Automatically organize:

Downloads
 ├ Images
 ├ Documents
 ├ Audio
 └ Code
2. Office Document Management

Companies can auto-sort:

Invoices
Reports
Spreadsheets
Presentations
3. Photo Organization

Photographers can sort:

RAW
PNG
JPG
Edited
4. Developer File Management

Sort project folders into:

Python
JavaScript
HTML
CSS
Skills This Program Demonstrates

GUI development

File system automation

Event handling

Dictionaries

Loops

Real-world utility software

This is actually a good beginner portfolio project.
