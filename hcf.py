# To find the highest common factors of two numbers entered by user
num1 = int(input("Enter your 1st number:"))
num2 = int(input("Enter your 2nd Number:"))

def get_hcf(num1, num2):
    hcf= 1
    for i in range(1,min(num1,num2)):
        if((num1 % i== 0) and (num2 % i == 0)):
            hcf= i
    print( " HCF of",num1,"and", num2, "is", hcf)

get_hcf(num1, num2)
            

