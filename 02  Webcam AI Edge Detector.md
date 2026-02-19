If ModuleNotFoundError: No module named 'cv2' shows in the terminal

Here's the fix


ModuleNotFoundError: No module named 'cv2'
means OpenCV is not installed in your Python environment.

cv2 is the module name for OpenCV, and Python can’t find it.


Solution: Install OpenCV
Open your terminal or command prompt and run:

pip install opencv-python
If that doesn’t work, try:

python -m pip install opencv-python
Or if you use Python 3 specifically:

python3 -m pip install opencv-python


If You’re Using VS Code

Sometimes VS Code uses a different Python interpreter.

Press Ctrl + Shift + P

Type: Python: Select Interpreter

Choose the correct Python version

Then install OpenCV again


If You’re Using a Virtual Environment

Activate it first:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate


Then install:

pip install opencv-python

Test if It’s Installed

After installing, try this in Python:

import cv2
print(cv2.__version__)


If it prints a version number, you're good
