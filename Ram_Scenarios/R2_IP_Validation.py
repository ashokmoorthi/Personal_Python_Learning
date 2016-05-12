''' Ram scenario Two:
1) Get input from User
2) Validate if it is valid numeric inputs
3) Validate if it is proper IP
2) If Valid IP then what is the class it belogs to
'''

import re

print ("This script will validate the given input is valid IP or Not and will tell the class it belogs to as well it is valid IP")
ip_input = input("Please enter the IP address to validate and know Valid or Not and the the Class it belogs to if valid: \n ")

print(ip_input)
for ip_oct in ip_input.split("."):
    #print (ip_oct)
    if ip_oct.isnumeric()== True:
        if int(ip_oct)>-1 and int(ip_oct)<256 :
            print (ip_oct)
        #print (ip_oct)
    else:
        res = ("Given input is not a numeric input for Valid IP " +ip_oct)
        print (res)













'''if type(eval(ip_oct)) == int:
        print ("Numeric")
    else:
        print ("Not a numeric input for Valid IP")'''





#get_input_ip = re.compile(r'\d\d\d.\d\d\d.\d\d\d.\d\d\d')
'''try:
    val = int(get_input_ip)
except ValueError:
    print("That's not an int!")'''

'''if get_input_ip.isdigit():
    print("Valid")
else:
    print("Not Valid")

if get_input_ip.isnumeric():
    print("Valid Numbers")
else:
    print("NOt Valid Numbers")'''