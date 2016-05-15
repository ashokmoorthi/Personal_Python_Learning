''' Ram scenario Four:
1) Get two numeric inputs
2) Give the value 0 for Denominator
3) Handle the error
4) Next step handle the other errors (Like if we give string instead of numeric)
5) Then how to handle general issues (Like unknown issue and handle them)
'''
import sys
#while True:
try:
    n = input("Numerator:")
    d = input("Denominator:")
    print (int(n) / int(d))
#        break
#    except ZeroDivisionError:
#        print ("Division by Zero error")
#        break
#    except ValueError:
#        print ("Only Numeric Values please")
#        break
except:
    print ("Unexpected error:", sys.exc_info()[0])
#        break