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

#Rewrite functions above as Lambda Functions
perimeter = lambda side_length: side_length * 4

alpha = "abcdefghijklmnopqrstuvwxyz"
my_lst = [alpha[i] for i in range(10)]

names = ["Alice", "Bob", "Charlie"]
my_dict = {n: n.upper() for n in names}

