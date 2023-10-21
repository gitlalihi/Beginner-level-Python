''' Assigning the variable to a integer number and checking the number is even or odd with using 
 the input()  functions'''

x= int (input(" Enter a number:"))
def odd_even(x):
    if  x % 2 == 0:
        print(x ,"is an even number")
    else:
        print(x ,"is an odd number")

odd_even(x)