#Program to decode the message from an encoded image

import cv2
import numpy as np

#This function is to convert data into binary
def messageToBinary(message):
    if type(message) == str:
        return ''.join([format(ord(i), "08b") for i in message])
    elif type(message) == bytes or type(message) == np.ndarray:
        return [format(i, "08b") for i in message]
    elif type(message) == int or type(message) == np.uint8:
        return format(message, "08b")
    else:
        raise TypeError("Input type not supported")

def decodeData(image):
    binary_data = ""
    for values in image:
        for pixel in values:
            #Converting RGB to binary
            r,g,b = messageToBinary(pixel)
            binary_data += r[-1] #LSB of red pixel
            binary_data += g[-1] #LSB of red pixel
            binary_data += b[-1] #LSB of red pixel
    
    #Converting to bytes
    all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data), 8)]

    #Converting bytes to characters
    decoded_message = ""
    for byte in all_bytes:
        decoded_message += chr(int(byte, 2))
        if decoded_message.endswith("####"): #Delimiter to terminate
            break

    #Returning the decoded message
    return decoded_message[:-4] #Removing delimiter

#Imputing the name of the file and printing the message
def print_text():
    image_name = input("Enter the name of the image with ext: ") #Obtaining the name of the file
    image = cv2.imread(image_name) #Opening the file with OpenCV

    print("The stego image is: ") #Display the original image
    cv2.imshow("Stego image", image)
    cv2.waitKey()

    #Obtaining the message
    text = decodeData(image)
    print("The embedded message is: ", text)

#Main function
print_text()
