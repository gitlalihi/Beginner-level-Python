# To check the maximum length of a string within a string using for loop
s1= str(input ("Enter your sentence:")) 
x= s1.split(' ')
print(x)
print(len(x))

def check_max_string():
   max_len = -1
   for a in x:
      if len(a)> max_len:
         max_len= len(a)
         response =a
         print(response)     

check_max_string()