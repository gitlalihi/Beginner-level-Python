# To determine whether the number entered by the user is pefect or not
num1= int(input("Enter your number:"))

def perf_num(num1):
    total = 0
    for i in range(1,num1):
        if num1 % i== 0:
            total= total+i
    if total==num1:
        print("Yes, its a perfect number")
    else:
        print("No, its not a perfect number")  

perf_num(num1)              

