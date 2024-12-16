import string
import random

def decode(str):
    if(len(str) >= 3):
        fchar = str[-4]
        str = str[3:-4]
        return fchar + str

    return str[::-1]

def encode(str):
    if(len(str) >= 3):
        s1 = ''.join(random.choices(string.ascii_letters, k=3))
        s2 = ''.join(random.choices(string.ascii_letters, k=3))
        str = str[1:] + str[0]
        return s1 + str + s2

    return str[::-1]

message = input("Please enter your message: ")
code_type = input("Please enter mechanism to be used: Encoding/Decoding: ")

words = message.split(" ")
# decode(message)

if code_type.lower() == "encoding":
    nwords = []
    for word in words:
        nwords.append(encode(word))

    print("Encoded message:", " ".join(nwords))
    
else:
    nwords = []
    for word in words:
        nwords.append(decode(word))

    print("Decoded message:", " ".join(nwords))

