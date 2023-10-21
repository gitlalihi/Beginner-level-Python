# To find the lcm of two numbers entered by  the users
num1= int(input(" Enter your 1st number:"))
num2= int(input("Enter your 2nd number:"))

def lcm(num1, num2):
    if num1 > num2:
        greater = num1
    else:
        greater = num2
    while(True):
        if((greater % num1 == 0) and (greater % num2 == 0)):
            lcm = greater
            break
        greater = greater + 1
    return lcm
print("LCM = ", lcm(num1,num2))



