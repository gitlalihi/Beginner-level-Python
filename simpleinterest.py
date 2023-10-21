p= int(input(" Enter your principal"))
r= float(input(" Enter your rate"))
t= float(input(" Enter your time"))
def simple_interest(p,r,t):
    print("The principal is", p)
    print("The rate is ", r)
    print("The time is ", t)
    si= (p*r*t)/100
    print("The simple interest is",si)

simple_interest(p,r,t)

