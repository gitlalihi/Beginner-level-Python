# To capatilize the first charachter of every word  in a  string using string methods.

class capatilize:
    def str_cap(s1): #  a user defined method name
       string = input("Enter a sentence:")
       s1=string.title() # a built in string method
       print(s1)

class_cap = capatilize() # creating object of the above class capatilize and calling the class
class_cap.str_cap()# access the method str_cap with a (.) referencing with object of the above class
    
