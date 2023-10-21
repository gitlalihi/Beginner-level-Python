# to print reverse number enter by user using while loop

num= int(input("Enter your number:"))

def reverse_order(num):
    count= num
    while True:
      print(count)
      count = count- 1
      if count == 0:
        break
      else:
        pass 

reverse_order(num)        