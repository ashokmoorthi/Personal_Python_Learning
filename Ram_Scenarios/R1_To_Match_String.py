''' Ram scenario One:
1) Get input from user (String alone)
2) Check the characters in the string and see if you can form the word "idirect"
3) If yes print iDirect
4) Else print Not a valid Input
5) Later update it to get both inputs from user
6) Print the reuslts'''

import sys
input_text_string = input('Please Enter the String: ')
print('Your input String:', input_text_string)
Tobecomaprestring = input('Please Enter the sub string to check part of the String: ')

for character in Tobecomaprestring:
    if Tobecomaprestring.count(character) > input_text_string.count(character):
        print ("Is Not a Valid String")
        sys.exit()

print (Tobecomaprestring + " is sub string of the first string provided: " +input_text_string)