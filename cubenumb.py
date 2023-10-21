#Python Program for cube sum of first n natural numbers
def sum_of_cubes(num):
    sum=0
    for i in range(1,num+1):
        sum= sum + (i *i* i)
    return sum


num= int(input(" Enter your number"))

print(sum_of_cubes(num))