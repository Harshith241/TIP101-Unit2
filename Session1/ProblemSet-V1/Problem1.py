'''Problem 1: Subsequence
Write a function is_subsequence() that takes in a list of integers lst and a list of integers sequence as parameters. Given these two lists, determine whether the sequence list is a subsequence of the lst list. A subsequence of a list is a set of numbers that aren't necessarily adjacent but are in the same relative order as they appear in the list. Return True if sequence is a subsequence, and False otherwise.

def is_subsequence(lst, sequence):
    pass
Example Usage:

lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))
Example Output: True'''

def is_subsequence(lst, sequence):
    j = 0
    for num in lst:
        if j == len(sequence):
            break
        if num == sequence[j]:
            j += 1
    return j == len(sequence)

print(is_subsequence([1,2,3,4], [1, 3]))