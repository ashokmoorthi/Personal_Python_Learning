input_text_string = input('Please Enter the String: ')
print('Your input String:', input_text_string)
#print(len(input_text_string))

keyword = 'idirect'

i=input_text_string.count("i")
#print (i)

d=input_text_string.count("d")
#print (d)

r=input_text_string.count("r")
#print (r)

e=input_text_string.count("e")
#print (e)

c=input_text_string.count("c")
#print (c)

t=input_text_string.count("t")
#print (t)

if i==2 and d==1 and r==1 and e==1 and c==1 and t==1:
    print("idirect")
else:
    print ("Is Not a Valid String")

