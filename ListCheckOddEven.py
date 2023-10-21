'''In a list of numbers entered by the user, check which among those numbers from the list
are odd and even and print them'''

num_list=[]

# defining 1 st  number range of the list num_list[]
x = int(input("Enter the first number:"))

# defining last number range of the list num_list[]
y = int(input("Enter the last number:"))

# using for loop list will be created b/w 1 st no and last no
for i in range( x , y):
    num_list.append(i) # lists the number b/w 1st and last no
print("The list is", num_list)   # prints the lists 
even_num_list=[]
odd_num_list=[]
for i in range(len(num_list)):# checks for odd and even 
    if(num_list[i] % 2 == 0):
        even_num_list.append(num_list[i])
    else:
        odd_num_list.append(num_list[i])
print("The even numbers from the list are",even_num_list)
print("The odd numbers from the list are",odd_num_list)

