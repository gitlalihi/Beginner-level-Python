# to print fibonacci series of a number using for loop 
num=int(input(" Enter your fibonacci number series :"))
def fibonacci(num):
    x=0
    y=1
    sum= 0
    for count in range(1,num+1):
        count = count+1
        x = y
        y= sum
        sum= x+ y
        print(sum)

fibonacci(num)

    