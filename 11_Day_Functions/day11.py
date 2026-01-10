import cmath
import keyword

def add_two_numbers(a,b):
    return (a+b)
print (add_two_numbers(2,3))

def area (r):
    return (3.14 * r*r)

print (area (3))

def add_all_nums(*params):
    sum = 0
    for i in params:
        sum +=i
    return (sum)
print (add_all_nums (1,2,3))

def convert_celsius_to_fahrenheit (c):
    return (c*(9/5)+32)
print (convert_celsius_to_fahrenheit (5))

def check_season(m):
    if m == "September" or m == "October" or m == "November":
        return ("Autumn")
    elif m == "December" or m == "January" or m == "February":
        return ("Winter")
    elif m == "March" or m == "April" or m == "May":
        return ("Spring")
    elif m == "June" or m == "July" or m == "August":
        return ("Summer")
    else:
        return ("enter a valid month")
print (check_season("June"))

def calculate_slope (m,x,c):
    return (m*x + c)
print (calculate_slope(1,2,3))

def solve_quadratic_eqn(a, b, c):
    if a == 0:
        raise ValueError("Coefficient 'a' must not be zero.")

    discriminant = b**2 - 4*a*c
    sqrt_disc = cmath.sqrt(discriminant)

    x1 = (-b + sqrt_disc) / (2 * a)
    x2 = (-b - sqrt_disc) / (2 * a)

    return {x1, x2}

print(solve_quadratic_eqn(1, -3, 2)) 

def print_list (*params):
    for i in params:
        print (i)
print_list(1,2,3,4)

def reverse_list (lst):
    i = len (lst)
    rev = []
    while i >0:
        rev.append(lst[i-1])
        i-=1
    return (rev)
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

def capitalize_list_items (lst):
    cap = []
    for i in lst:
        cap.append(i.capitalize())
    return cap
print (capitalize_list_items (['a','b','cd']))

def add_item (lst, item):
    return (lst.append(item))
print (add_item(['Potato', 'Tomato', 'Mango', 'Milk'],"Meat"))

def remove_item (lst, item):
    return (lst.remove(item))
print (remove_item (['Potato', 'Tomato', 'Mango', 'Milk'], 'Mango'))

def sum_of_numbers (num):
    sum = 0
    for i in range (num):
        sum +=i
    return (sum)
print(sum_of_numbers(100))

def sum_of_odds (num):
    sum_odd = 0
    for i in range (num):
        if i % 2 !=0:
            sum_odd +=i
    return (sum_odd)
print (sum_of_odds(5))

def sum_of_even(num):
    sum_even = 0
    for i in range (num):
        if i % 2 == 0:
            sum_even +=i
    return (sum_even)
print (sum_of_even(5))
    
def evens_and_odds (num):
    count_odd = 0
    count_even = 0
    for i in range (num):
        if i % 2 == 0:
            count_even +=1
        else:
            count_odd +=1
    return (count_odd,count_even) 
print (evens_and_odds(100))

def is_empty(param):
    if  param == None:
        return ("empty")
    else:
        return ("not empty")
print (is_empty(1))

def is_prime(num):
    if num <= 1:
        return ("not prime")
    if num <=3:
        return ("prime")
    if num %2 == 0 or num % 3 == 0:
        return ("not prime")
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i+2) == 0:
            return ("not prime")
        i+=6
    return ("prime")
print (is_prime(23))

def is_unique(lst):
    st = set (lst)
    if len(lst) == len (st):
        return ("unique")
    else:
        return ("not unique")
print (is_unique([1,2,3,3,4,54,6]))

def is_same_dataType (lst):
    if len(lst) == 1:
        return ("same")
    i = 1
    while i < len(lst):
        if type(lst[i-1]) != type(lst[i]):
            return ("not same")
        else:
            i+=1
            continue
    return ("same")
print (is_same_dataType([1,2,3,'c']))
print (is_same_dataType([1,2,3]))

def is_valid_variable(name):
    return name.isidentifier() and not keyword.iskeyword(name)
print(is_valid_variable("my_var"))   
print(is_valid_variable("1var"))     
print(is_valid_variable("class"))    
    
        
        
          
        
