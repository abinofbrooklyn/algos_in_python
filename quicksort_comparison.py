#!/usr/bin/env

# Case I
# First element of the unsorted array is chosen as pivot element for sorting using Quick Sort


def countComparisonsWithFirst(array):
    """ Counts number of comparisons while using Quick Sort with first element of unsorted array as pivot """
    global count_pivot_first
    if len(array) == 1 or len(array) == 0:
        return array
    else:
        count_pivot_first += len(array)-1
        i = 0
        for j in range(len(array)-1):
            if array[j+1] < array[0]:
                array[j+1],array[i+1] = array[i+1], array[j+1]
                i += 1
        array[0],array[i] = array[i],array[0]
        first_part = countComparisonsWithFirst(array[:i])
        second_part = countComparisonsWithFirst(array[i+1:])
        first_part.append(array[i])
        return first_part + second_part

# Case II
# Last element of the unsorted array is chosen as pivot element for sorting using Quick Sort

def countComparisonsWithLast(array):
    """ Counts number of comparisons while using Quick Sort with last element of unsorted array as pivot """
    global count_pivot_last
    if len(array) == 1 or len(array) == 0:
        return array
    else:
        count_pivot_last += len(array)-1
        array[0],array[-1] = array[-1],array[0]
        i = 0
        for j in range(len(array)-1):
            if array[j+1] < array[0]:
                array[j+1],array[i+1] = array[i+1], array[j+1]
                i += 1
        array[0],array[i] = array[i],array[0]
        first_part = countComparisonsWithLast(array[:i])
        second_part = countComparisonsWithLast(array[i+1:])
        first_part.append(array[i])
        return first_part + second_part

# Case III
# Median-of-three method used to choose pivot element for sorting using Quick Sort

def middle_index(array):
    """ Returns the index of the middle element of an array """
    if len(array) % 2 == 0:
        middle_index = len(array)/2 - 1
    else:
        middle_index = len(array)/2
    return middle_index

def median_index(array,i,j,k):
    """ Returns the median index of three when passed an array and indices of any 3 elements of that array """
    if (array[i]-array[j])*(array[i]-array[k]) < 0:
        return i
    elif (array[j]-array[i])*(array[j]-array[k]) < 0:
        return j
    else:
        return k

def countComparisonsMedianOfThree(array):
    """ Counts number of comparisons while using Quick Sort with median-of-three element is chosen as pivot """
    global count_pivot_median
    if len(array) == 1 or len(array) == 0:
        return array
    else:
        count_pivot_median += len(array)-1
        k = median_index(array, 0, middle_index(array), -1)
        if k != 0: array[0], array[k] = array[k], array[0]
        i = 0
        for j in range(len(array)-1):
            if array[j+1] < array[0]:
                array[j+1],array[i+1] = array[i+1], array[j+1]
                i += 1
        array[0],array[i] = array[i],array[0]
        first_part = countComparisonsMedianOfThree(array[:i])
        second_part = countComparisonsMedianOfThree(array[i+1:])
        first_part.append(array[i])
        return first_part + second_part

#####################################################################
# initializing counts
count_pivot_first = 0; count_pivot_last = 0; count_pivot_median = 0

#####################################################################
# Cast I
# Read the contents of the file into a Python list
NUMLIST_FILENAME = "QuickSort.txt"
inFile = open(NUMLIST_FILENAME, 'r')

with inFile as f: numList = [int(integers.strip()) for integers in f.readlines()]
# call functions to count comparisons
countComparisonsWithFirst(numList)

#####################################################################
# Read the contents of the file into a Python list
NUMLIST_FILENAME = "QuickSort.txt"
inFile = open(NUMLIST_FILENAME, 'r')

with inFile as f: numList = [int(integers.strip()) for integers in f.readlines()]
# call functions to count comparisons
countComparisonsWithLast(numList)

#####################################################################
# Read the contents of the file into a Python list
NUMLIST_FILENAME = "QuickSort.txt"
inFile = open(NUMLIST_FILENAME, 'r')

with inFile as f: numList = [int(integers.strip()) for integers in f.readlines()]
# call functions to count comparisons
countComparisonsMedianOfThree(numList)
#####################################################################

print count_pivot_first, count_pivot_last, count_pivot_median
