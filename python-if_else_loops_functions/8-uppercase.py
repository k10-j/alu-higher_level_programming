#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        # Check if character is lowercase
        if ord('a') <= ord(char) <= ord('z'):
            # Convert to uppercase by subtracting 32 from ASCII value
            char = chr(ord(char) - 32)
        result += char
    print("{}".format(result))
