import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
#sort a list of book objects in ascending order based on their titles.
#input: a list of book objects, where each book object has a title attribute.
#output: the input list, book_list, sorted in-place by the titles of the books in ascending order.
def selection_sort_books(book_list: list):
    for i in range(len(book_list)):
        index = i
        for j in range(i + 1, len(book_list)):
            if book_list[j].title < book_list[index].title:
                index = j
        temp = book_list[i]
        book_list[i] = book_list[index]
        book_list[index] = temp
        

# Part 2
#swap the case of each character(lowercase letters to uppercase and uppercase letters to lowercase)
#input: string containing characters of different cases.
#output: a new string with the cases of all characters swapped(lowercase letters to uppercase and uppercase letters to lowercase)
def swap_case(input:str) -> str:
    result = []
    for i in input:
        if i.islower():
            result.append(i.upper())
        elif i.isupper():
            result.append(i.lower())
        else:
            result.append(i)
    return ''.join(result)


# Part 3
#replaces every occurrence of `old` character in `input_str` with `new` character.
#input: input_str, old:str, new:str
#output: str: The new string with `old` replaced by `new` characters.
def str_translate(input_str, old, new):
    result = []
    for i in input_str:
        if i == old:
            result.append(new)
        else:
            result.append(i)
    return ''.join(result)



# Part 4
#Count how many times each word appears in a string
#input: a string containing words separated by spaces
#output: a dictionary mapping each word to its count
def histogram(string):
    word_counts = {}
    words = string.split()
    for i in words:
        if i in word_counts:
            word_counts[i] += 1
        else:
            word_counts[i] = 1
    return word_counts
