"""
Write a program that detects the ID number hidden in a text. 
We know that the format of the ID number is 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).
Input   : AABZA1111AEGTV5YH678MK4FM53B6
Output  : MK4FM53B6
Input   : AEGTV5VZ4PF94B6YH678
Output  : VZ4PF94B6
"""

import re
try:
    patern  =r"[a-zA-Z]{2}\d[a-zA-Z]{2}\d{2}[a-zA-Z]\d"
    string  =input("Enter a text: ")
    ddd     =re.search(patern,string).group()
    print("ID Number :", ddd)
except:
    print("ID number not found matching the criteria")
