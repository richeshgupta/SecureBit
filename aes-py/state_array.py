# trying for 128 bit key only
from const_aes import *
import numpy as np

state_array = [[0 for x in range(4)] for x in range(4)]

def hexconversion(text):
    hex_code  = []
    temp=[]
    print("text : ",text)
    for i in range(len(text)):
       
        temp.append([hex(ord(text[i]))[2:]])
        temp[i] = int(temp[i][0])
        print(temp)

    return temp

def padd(text,key):
    present_len = len(text)   
    if(present_len>16):
        text = text[0:16]
    elif present_len<16:
        null_add = 16 - present_len
        text  = text + ( (null_add)*"0")
    return text


def text2matrix(cipher_array):
    return "TO be done"
    


def interact():
    text = input("Enter Text to encrypt : ")
    key = input("Enter Key : ")
    text = padd(text,key)
    cipher_array = hexconversion(text)
    cypher_matrix = text2matrix(cipher_array)
    # print(matrix)

if __name__ == "__main__":
    interact() 

        

    

