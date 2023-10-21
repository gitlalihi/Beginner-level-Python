# to print the sum of squares of natural numbers

def sum_of_squares(num):
    sum=0
    for i in range(1,num+1):
        sum= sum + (i *i)
    return sum


num= int(input(" Enter your number"))

print(sum_of_squares(num))
