# Image-Steganography
Python programs of the Image Steganography project at BISAG
Consists of an encoder program and a decoder program

**Encoder Program**
Encoder program works by taking the message to be embedded and converting it into bits.
This is then embedded into the LSB of the RGB values of each pixel taken serially.
This is continued till the stop sequence is reached.
A change in the LSB is undetectable to the human eye and is not considered suspicious by computers.
Each pixel has 3 values Red Green and Blue and one bit can be encoded into the LSB of each of this. Thus each pixel can store 3 bits.
The total number of bytes that can possibly be encoded in an image is:
(Length of image in pxl) * (Breadth of image in pxl) * 3 // 8

This program can work on any lossless image format such as PNG or BMP.
JPG/ JPEG cannot be used as JPG format utilises a lossly compression method.

**Decoder Program**
Decoder program works just the opposite way as the encoder program
A stego image is taken and each pixel is read for the RGB values and the LSB is taken from it.
This is continued across all pixels
The bits taken from the LSB are converted into bytes in sets of 8 and stopped when the stop sequence is reached.
This is then converted into ASCII and the message is shown.

**Possible Improvements**
1. The encoder program does not utilise any encryption techniques on the message. The security of the message can be greatly improved by using any encryption technique.
2. Instead of serially embedding the message various other methods such as a circular method using the mid point technique can secure the message against possible steganalysis.
