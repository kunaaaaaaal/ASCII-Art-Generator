# ASCII-Art-Generator

ASCII(American Standard Code for Information Interchange) is a common encoding format used for representing strings and text data in computers.

I have used Opencv and Pillow libraries to write the code.

Also, I have written the code for generating a Pencil Sketch of an image using Opencv exclusively.

1. ASCII Art Generator

I made a character map of ASCII characters of increasing order of brightness.
I also added colors to the ASCII characters.
Then, I Stored the output.

2. Pencil Sketch Generator

Created a Pencil Sketch of an image using Opencv exclusively.
First I converted the image into a grayscale image.
The inverted the image.
Then I applies Gaussian Blur to the image.
Then I obtained the sketch by performing Bitwise division between the Grayscale image and the inverted Blurred image.
Then, I saved the created Sketch.
