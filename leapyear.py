# To check whether the year entered by the user is a leap year or not
def CheckYear(y):
    if (y%4 == 0) and (y%100 != 0) or (y%400 == 0):
        print(y, ' is a leap year')
    else:
        print(y, ' is not a leap year')
        
def main():
    y = int(input('Enter the year: '))
    CheckYear(y)
    
main()