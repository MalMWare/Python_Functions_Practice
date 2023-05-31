# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_arr(array):
  arr = []
  for num in array:
    if type(num) == int:
      arr.append(num)
    else:
      for order in num:
        arr.append(order)
  return sorted(arr)

print(flatten_arr([4, 2, 88, 45, [1, 300], [40, 28]]))

'''
How does this solution ensure data immutability?

The data is immutable because when data is put in the function it doesn't override the new data. The data is static and the function ensures that the data will not be deleted. WHen called a new log will be formed. 


Is this solution a pure function? Why or why not?

This is a pure function because when given the same input it results in the same output every time. There is no change in originl value, a new log is given. 


Is this solution a higher order function? Why or why not?

This is a higher order function because it needs an array to call another function that outputs a new log of data


Would it have been easier to solve this problem using a different programming style?

Using this style  makes it easier to keep prior data and not lose it where as with more mutable functions I could lose previour data. 


Why in particular is functional programming a helpful paradigm when solving this problem?
It is easier to debug.
'''