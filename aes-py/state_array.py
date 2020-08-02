# trying for 128 bit key only
from const_aes import *

state_array = [[0 for x in range(4)] for x in range(4)]

def hexconversion(text):
    hex_code  = ""
    for i in text:
        hex_code = hex_code + hex(ord(i))[2:]
    
    return hex_code

def padd(text,key):
    present_len = len(text)   
    if(present_len>16):
        text = text[0:16]
    elif present_len<16:
        null_add = 16 - present_len
        text  = text + ( (null_add)*"0")

def text2matrix(text):
    matrix = []
    return text[0:]


def interact():
    text = input("Enter Text to encrypt : ")
    key = input("Enter Key : ")
    text = padd(text,key)
    
    
    print(text2matrix(hexconversion(text)))

if __name__ == "__main__":
    interact() 

        

    

