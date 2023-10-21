# To print the maximum of the three numbers entered by the  user
import math

x= int(input("Enter your 1st number:"))
y= int(input("Enter your 2 number:"))
z= int(input("Enter your 3rd number:"))

def max_num(x,y,z):
    if x > y:
        print(x)
    elif y > z :
        print (y)
    elif z > max(x,y):
        print (z)
    print("The highest number is" , max(x,y,z))

max_num(x,y,z)
