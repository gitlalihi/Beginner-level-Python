import math

p= int(input(" Enter your principal"))
r= float(input(" Enter your rate"))
t= int(input(" Enter your time"))
def compund_interest(p,r,t):
    print("The principal is", p)
    print("The rate is ", r)
    print("The time is ", t)
    Amount = p * (pow((1 + r / 100), t))
    CI = Amount - p
    print("Compound interest is", CI)
 
compund_interest(p,r,t)
