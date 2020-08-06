#Program to embed a secret message into an image

import cv2
import numpy as np


#This funtion is to convert data to binary
def messageToBinary(message):
    if type(message) == str:
        return ''.join([format(ord(i), "08b") for i in message])
    elif type(message) == bytes or type(message) == np.ndarray:
        return [format(i, "08b") for i in message]
    elif type(message) == int or type(message) == np.uint8:
        return format(message, "08b")
    else:
        raise TypeError("Input type not supported")


#This function is to embed the message into the image
def embedData(image, secret_message):

    #Calculating the maximum amount of bytes to be encoded
    n_bytes = image.shape[0] * image.shape[1] * 3 // 8

    print("Size of message: ", len(secret_message))
    print("Maximum bytes possible to encode:", n_bytes)

    #Checking if message is smaller than maximum no. of bytes
    if (len(secret_message) > n_bytes):
        raise ValueError("Image not of sufficient size to encode this message")

    secret_message += "####" #Serves as the delimiter to terminate

    data_index = 0 #To tell the position of the bit we are encoding

    binary_message = messageToBinary(secret_message) #To convert secret message to binary

    data_len = len(binary_message) #Length of data to encode

    for values in image:
        for pixel in values:
            #Converting RGB to binary
            r,g,b = messageToBinary(pixel)

            #If statements to encode message only if data left to encode

            #Red
            if data_index < data_len:
                pixel[0] = int(r[:-1] + binary_message[data_index], 2)
                data_index += 1
            
            #Green
            if data_index < data_len:
                pixel[1] = int(g[:-1] + binary_message[data_index], 2)
                data_index += 1

            #Blue
            if data_index < data_len:
                pixel[2] = int(b[:-1] + binary_message[data_index], 2)
                data_index += 1

            #Exiting loop if complete
            if data_index >= data_len:
                break
    
    return image

#Taking image and message from user
def  get_text():
    image_name = input("Enter the name of the image with ext: ") #Obtaining the name of the file
    image = cv2.imread(image_name) #Opening the file with OpenCV

    print("The original image is: ") #Display the original image
    cv2.imshow("Original image", image)
    cv2.waitKey()

    data = input("Enter the message to be encoded: ")
    if (len(data) == 0):
        raise ValueError("Data is empty")

    new_image = input("Enter the name of the encoded image with ext: ")
    encoded_image = embedData(image, data) #Calling the function to embed the message
    cv2.imwrite(new_image, encoded_image)

    print("The stego image is: ") #Display the stego image
    stego_image = cv2.imread(new_image)
    cv2.imshow("Stego image", stego_image)
    cv2.waitKey()

#Main function
get_text()
