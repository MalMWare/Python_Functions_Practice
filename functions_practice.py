# A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.
def hello():
    print('greetings')

# A function named pack() that accepts three arguments, and returns a single list with the three arguments inside as list elements.
def pack(boop, beep, bop):
    return[boop, beep, bop]
    
# A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" 
# (the first element of the list), and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". 
# The function should not return anything.
def eat_lunch(food):
    if len(food) == 0:
        print('There is nothing in my lunchbox')
    else:
        for i in range(len(food)):
            if i == 0:
                print(f"First I eat {food[0]}")
            else:
                print(f"Next I eat {food[i]}")


#create a function to get the max number of any object
def max_number(m, a, x):
    return max(m, a, x)

#create a function called multi_list() to multiply all numbers in a list
def multi_list(*args):
    sum = 1
    for num in args:
        sum *= num
    return sum 

#Write a Python function called rev_string() to reverse a string.
def rev_string(str):
    return str[::-1]

# Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(n, u, m):
    return n in range(u, m + 2)

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
def pascal(n):
    num = ''
    prev_num = ''
    for e in range(n):
        if e == 0:
            prev_num = '1'
            num += f'{prev_num}\n'
        elif e == 1:
            prev_num = '1 1'
            num += f'{prev_num}\n'
        else:
            current_num = ''
            split = prev_num.split()
            for i, n in enumerate(split):
                if i != len(split) - 1:
                    number = int(n) + int(split[i+1])
                    current_num += f'{str(number)} '
            prev_num = f'1 {current_num}1'
            num += f'{prev_num}\n'
    return num

# Problem 1: Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.
# flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
#{'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}

def flatten_dict(d):
    result = dict()
    for i in d.keys():
        if type(d[i]) == dict:
            #value is dict so we must flatten it
            for k,v in d[i].items():
                new_key = i + "." + k #make new pair
                result[new_key] = v #add k:v pair
        else:
                #add the k:v pair to result dictionary
                result[i] = d[i]
    return result

#Problem 2: Write a function unflatten_dict to do reverse of flatten_dict.
#unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
#{'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}

def unflatten_dict(d):
    result = dict()
    for i in d.keys():
        if "." in i:
            #this should be nested
            new_key, sep, inner_key = i.partition(".")
        #create dictionary if not yet created
            if new_key not in result.keys():
                result[new_key] = dict()
        #add elements to inner dictionary
            result[new_key][inner_key] = d[i]
        else:
            #add the k:v pair to result dictionary
            result[i] = d[i]
    return result

#Problem 3: Write a function treemap to map a function over nested list.
#treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
#[1, 4, [9, 16, [25]]]
def treemap(func, lst):
    for i in range(len(lst)):
        if type(lst[i]) == list:
            lst[i] = treemap(func, lst[i])
        else:
            lst[i] = func(lst[i])
    return lst

#what to put in the terminal to show result(s) of function being used
hello()
print(pack(1,2,3))
print(pack('boop', 'beep', 'bop'))
eat_lunch([])
eat_lunch(['pizza', 'popcorn', 'icecream'])
print(max(1, 2, 3))
print(multi_list(2, 3, 4))
print(rev_string('cookies'))
print(num_within(3, 1, 3)) #true
print(num_within(10,2,5)) #false
print(pascal(6))
print(flatten_dict({'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}))
print(unflatten_dict({'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}))
print(treemap(lambda i: i*i, [1, 2, [3, 4, [5]]]))

