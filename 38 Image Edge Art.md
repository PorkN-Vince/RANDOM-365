Your program performs edge detection on an image. It loads an image, detects its edges using an algorithm, and then displays the result as a sketch-like image.

⚠ There is also a small mistake in your code that I will point out.

What the Program Does

The program:

Loads an image

Detects the edges (outlines) of objects in the image

Displays the result as a black-and-white sketch

This technique is commonly used in computer vision and image processing.

Line-by-Line Explanation
1. Import OpenCV
import cv2

This imports the OpenCV library.

OpenCV stands for:

Open Source Computer Vision

It is used for:

image processing

object detection

face recognition

video processing

Here it is used to detect edges in an image.

2. Import Matplotlib
import matplotlib.pylot as plt

⚠ This line has an error.

It should be:

import matplotlib.pyplot as plt

matplotlib is used for displaying images and graphs.

plt is just a shorter name used to call its functions.

Example:

plt.show()

displays the image window.

3. Load the Image
img = cv2.imread("g.jpg")

This loads an image file.

g.jpg

must exist in the same folder as your Python script.

What happens here:

OpenCV reads the image

Stores it in a variable called img

Example:

img = matrix of pixel values
4. Detect Edges
edges = cv2.Canny(img, 100, 200)

This line performs edge detection using the Canny Edge Detection algorithm.

Edge detection finds sharp changes in brightness, which represent object boundaries.

Parameters:

Parameter	Meaning
img	the image to process
100	lower threshold
200	upper threshold

These thresholds control edge sensitivity.

Example:

Low values → more edges detected
High values → fewer edges detected

Result:

edges = black image with white outlines
5. Display the Image
plt.imshow(edges, cmap="gray")

This displays the edge-detected image.

cmap="gray" means:

display the image in grayscale

Black = background
White = detected edges

6. Add a Title
plt.title("Edge Detection Sketch")

Adds a title above the image.

Output example:

Edge Detection Sketch
7. Remove Axis
plt.axis("off")

This removes the x and y coordinate axes.

Without it, the image would show numbers like:

0 100 200

Turning it off makes the image cleaner.

8. Show the Image
plt.show()

This opens a window and displays the final result.

Final Program Flow

The program works like this:

Load image
     ↓
Detect edges
     ↓
Display edges as grayscale image
Example Output

Original image:

Photo of a person

Output:

Black background
White outlines of the person

It looks like a pencil sketch.

Practical Applications

Edge detection is very important in computer vision.

1. Face Detection

Used in systems like:

phone face unlock

security cameras

Edges help detect facial features.

2. Self-Driving Cars

Cars detect:

road lines

obstacles

pedestrians

Edge detection helps identify boundaries and shapes.

3. Medical Imaging

Doctors use edge detection to highlight:

tumors

bones

organs

in X-ray or MRI images.

4. Image Filters

Many apps use edge detection to create:

sketch filters
cartoon filters
artistic effects
5. Object Recognition

Robots use edges to detect objects.

Example:

identify a bottle
detect a car
recognize a stop sign
Errors in Your Code
1. Typo in matplotlib

Wrong:

import matplotlib.pylot as plt

Correct:

import matplotlib.pyplot as plt
2. Image file must exist

This file must exist:

g.jpg

Otherwise you will get an error.

Correct Version of the Code
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("g.jpg")

edges = cv2.Canny(img, 100, 200)

plt.imshow(edges, cmap="gray")
plt.title("Edge Detection Sketch")
plt.axis("off")
plt.show()
Summary

This program:

Loads an image

Uses OpenCV's Canny algorithm to detect edges

Displays the edges as a grayscale image

Result: a sketch-like outline of the original image.
