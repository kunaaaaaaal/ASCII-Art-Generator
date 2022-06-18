# ASCII-Art-Generator

ASCII(American Standard Code for Information Interchange) is a common encoding format used for representing strings and text data in computers.

I have used Opencv and Pillow libraries to write the code.

Also, I have written the code for generating a Pencil Sketch of an image using Opencv exclusively.

1. ASCII Art Generator

I made a character map of ASCII characters of increasing order of brightness.
I also added colors to the ASCII characters.
Then, I Stored the output.

![Input-6](https://user-images.githubusercontent.com/99754070/174424843-8f689ee2-5c78-4360-a6e1-41b175e451b2.jpg)

![output-6](https://user-images.githubusercontent.com/99754070/174424849-6d255325-3dad-4da5-b6f3-f5c4162b4965.jpg)



2. Pencil Sketch Generator

Created a Pencil Sketch of an image using Opencv exclusively.
First I converted the image into a grayscale image.
The inverted the image.
Then I applies Gaussian Blur to the image.
Then I obtained the sketch by performing Bitwise division between the Grayscale image and the inverted Blurred image.
Then, I saved the created Sketch.

