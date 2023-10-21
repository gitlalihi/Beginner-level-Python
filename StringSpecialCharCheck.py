'''Using the if -elif-else expression to check whether the string  contains a 
 special charachter  or not'''
import re 

s1= input("Enter a phrase:")

if ( bool (re.match ("^[a-zA-Z0-9] *$",s1)) == True):
        print(" string does not have a special  charchter")
else:
        print("string has  a special chrachter")

       