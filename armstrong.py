# To print out the armstrong numbers in a given range entered by the user
x= int(input("Enter your minimum range:"))
y= int(input("Enter your maximum range:"))
def armstrongNum():
    for i in range(x,y):
        sum = 0
        temp = i
        while temp > 0:
            digit = temp % 10
            sum = sum+  digit ** 3
            temp =temp// 10
    
        if i == sum:
            print('The armstrong Number in your range is: ',i)
            
armstrongNum()
