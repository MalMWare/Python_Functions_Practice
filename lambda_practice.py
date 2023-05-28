def perimeter(side_length):
    return 4 * side_length


my_lst = []
alpha = "abcdefghijklmnopqrstuvwxyz"

for i in range(10):
    my_lst.append(alpha[i])


my_dict = dict()
names = ["Alice", "Bob", "Charlie"]
for i in names:
    my_dict[i] = i.upper()


# Problem 1: Write a lambda function to sort a list of tuples in ascending order according to the number in the second position of each tuple.

grades = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Problem 2: Write a lambda function to cube every element of a list
#Original list: [3,6,9,2]

cubed = lambda x: [i**3 for i in x]
print(cubed([3,6,9,2])) 

#Problem 3: Write a lambda function to determine whether a number is even or odd (the function should return True or False), and then use the function and a list comprehension to create a new list of booleans, where even numbers are True and odd numbers are False.



# Problem 4: Use a list comprehension to create a list of the numbers from 1 to 100 (including 100).
#Rewrite functions above as Lambda Functions

# Problem 5: Use a dictionary comprehension to count the length of each word in a sentence.
perimeter = lambda side_length: side_length * 4

alpha = "abcdefghijklmnopqrstuvwxyz"
my_lst = [alpha[i] for i in range(10)]

names = ["Alice", "Bob", "Charlie"]
my_dict = {n: n.upper() for n in names}

