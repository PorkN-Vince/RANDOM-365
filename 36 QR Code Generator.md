This Python program generates a QR code image from a link and saves it as a file. Anyone who scans the QR code with a phone will be directed to the link inside it.

Below is a line-by-line explanation of the code and its practical applications.

1. Import the QR Code Library
import qrcode

What it does:

Imports the qrcode library, which allows Python to generate QR codes.

Why it's needed:
Without this library, Python would not know how to create QR codes.

Example use:

Creating QR codes for links

Generating contact QR codes

WiFi connection QR codes

2. Define the QR Code Function
def generate_qr_code(text, file_name):

What it does:

Creates a function called generate_qr_code.

Parameters:

Parameter	Meaning
text	The data to store inside the QR code
file_name	The name of the image file that will be saved

Example:

text = website link
file_name = qr.png
3. Create the QR Code Object
qr = qrcode.QRCode(

This line creates a QR code generator object.

It allows you to configure how the QR code will look.

4. QR Code Settings
version=1,

What it means:

Controls the size of the QR code.

QR versions range from 1 to 40.

Version	Size
1	Small QR
40	Very large QR

Version 1 = 21×21 grid.

error_correction=qrcode.constants.ERROR_CORRECT_L

Error correction allows QR codes to still work even if damaged.

Levels:

Level	Damage tolerance
L	7%
M	15%
Q	25%
H	30%

Your code uses L, which is the lowest.

box_size=10

Controls how big each square is in pixels.

Example:

box_size	Result
5	small QR
10	medium QR
20	large QR
border=3

Controls the white border around the QR code.

Most scanners require a border to scan properly.

5. Add Data to the QR Code
qr.add_data(text)

This line puts the text or link into the QR code.

Example stored data:

https://www.instagram.com/pycode.dev

When scanned, it opens that link.

6. Generate the QR Code Pattern
qr.make(fit=True)

This tells Python to generate the QR code grid.

fit=True means:

Automatically adjust the size if the data is too large.

7. Create the QR Code Image
img = qr.make_image(fill_color="#4B8BBE", back_color="white")

This converts the QR code into an image.

Color settings:

Parameter	Meaning
fill_color	QR code color
back_color	background color

Your QR code color:

#4B8BBE

This is the Python programming language blue.

8. Save the QR Code
img.save(file_name)

This saves the QR code image to a file.

Example result:

instagram_qr.png
9. Program Entry Point
if __name__ == "__main__":

This ensures the code only runs when the script is executed directly.

It prevents the code from running if the file is imported as a module.

10. QR Code Data
text = "https://www.instagram.com/pycode.dev?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="

This is the data stored in the QR code.

In this case:

an Instagram profile link

11. Output File Name
file_name = "instagram_qr.png"

Defines the file name for the generated QR code image.

12. Generate the QR Code
generate_qr_code(text, file_name)

Calls the function and generates the QR code.

Steps performed:

Create QR object

Add link data

Generate QR pattern

Create image

Save image

13. Confirmation Message
print(f"QR code saved as {file_name}")

Prints a message in the terminal.

Example output:

QR code saved as instagram_qr.png
Final Program Flow

The program works like this:

Import QR library
       ↓
Create QR code settings
       ↓
Insert link into QR code
       ↓
Generate QR pattern
       ↓
Create image
       ↓
Save image file
Practical Applications

This type of program is used in many real-world systems.

1️⃣ Marketing

Companies create QR codes for:

websites

Instagram pages

promotions

Example:

Restaurant menu QR code
2️⃣ Contact Sharing

QR codes can store:

Name
Phone number
Email

Scanning automatically saves a contact.

3️⃣ WiFi Access

QR codes can store WiFi credentials.

When scanned, phones automatically connect.

4️⃣ Payments

Many payment systems use QR codes:

GCash

PayPal

PayMaya

5️⃣ Event Tickets

QR codes are used for:

concert tickets
boarding passes
conference passes
Example Output

Your program generates:

instagram_qr.png

Scanning the QR code opens:

instagram.com/pycode.dev

✅ Summary:
This Python script creates a QR code from a link and saves it as an image file, which can be scanned by smartphones to open the stored data.
