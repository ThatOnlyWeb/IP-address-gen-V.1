import random 

numbers = '1', '2', '3', '4', '5', '6', '7', '8', '9', '0' 
def print_dot(): 
    print(".") 
def print_numbers(): 
    value = random.choice(numbers) 
    print(value) 
def print_all(): 
    for x in range(2): 
        print_numbers() 
def print_all2(): 
    for a in range(2): 
        print_numbers() 
def print_all3(): 
    for b in range(2): 
        print_numbers()
def print_all4(): 
    for c in range(3): 
        print_numbers()
print_all() 
print_dot() 
print_all2()
print_dot()
print_all3()
print_dot()
print_all4()
