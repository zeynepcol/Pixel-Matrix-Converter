<h1 align="left">Image Pixel Data Extraction Script</h1>

This project uses **Python's PIL (Pillow)** library to load, process, and extract pixel data from an image file. The program iterates over each pixel, computes an "intensity" value, and outputs pixel data in a format suitable for C++ array use, making it ideal for projects that involve image analysis or pixel-based graphical effects.
<h3 align="left">FEATURES</h3>

**1. Image Loading**



Opens an image file using **PIL.Image**.



**2. Image Resizing**


Optionally resizes the image to specified dimensions (default: 50x50 pixels).



**3. RGB Conversion**


 Converts the image to RGB mode, ensuring compatibility with RGB-based calculations.
 

**4. Intensity Calculation**

Computes pixel intensity based on the average RGB values.


**5. C++ Array Output**

Outputs the pixel data in a C++ compatible array format for easy integration.



<h3 align="left">Requirements</h3>


**Python 3.6+** 




**Pillow library (pip install pillow)**
