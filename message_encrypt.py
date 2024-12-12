import string
import random

def decode(str):
    fchar = str[-4]
    str = str[3:-4]
    return fchar + str

def encode(str):
    s1 = ''.join(random.choices(string.ascii_letters, k=3))
    s2 = ''.join(random.choices(string.ascii_letters, k=3))
    str = str[1:] + str[0]
    return s1 + str + s2

message = input("Please enter your message: ")
code_type = input("Please enter mechanism to be used: Encoding/Decoding: ")

# decode(message)

if code_type.lower() == "encoding":
    str = encode(message)
    print("Encoded message:", str)
    str = decode(str)
    print("Decoded message:", str)
else:
    str = decode(message)
    print("Decoded message:", str)