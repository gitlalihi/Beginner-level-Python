#To check whether the numbers entered by the user are co-prime or not

def co_prime (num1, num2):
    hcf = 1
    for i in range(1, num1+1):
        if  (num1 %i==0) and (num2%i==0):
            hcf = i
    return hcf == 1

def main():
    num1 = int(input("Enter your 1st number:"))
    num2 = int(input("Enter your 2nd Number:"))
    if co_prime(num1, num2):
        print('%d and %d are CO-PRIME Number' %(num1, num2))
    else:
        print('%d and %d are NOT CO-PRIME Number' %(num1, num2))

main()

