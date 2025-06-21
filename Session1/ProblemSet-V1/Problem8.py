'''Write a function index_to_value_map() that takes in a list lst and returns a dictionary that maps the index of each element in lst to its value.

def index_to_value_map(lst):
    pass
Example Input: lst = ["apple", "banana", "cherry"]

Example Output: {0: "apple", 1: "banana", 2: "cherry"}

'''

def index_to_value_map(lst):
    counter = 0
    dictionary = {}
    for item in lst:
        dictionary[counter] = lst[counter]
        counter += 1
    return dictionary
lst = ["apple", "banana", "cherry"]

print(index_to_value_map(lst))