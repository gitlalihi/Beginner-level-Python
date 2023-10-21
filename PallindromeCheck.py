'''Defining a function and checking the string from the 1st n index to the last n index of 
a string '''

string=str(input("Enter a string"))
def check_pallindrome(string):
    for i in range (int(len(string)/2)):
        if string[i] != string[len(string)-i-1]:
           print("the string is not a pallindrome")
    else:
         print(" the string is a pallindrome ")
    

check_pallindrome(string)

