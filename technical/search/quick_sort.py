"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

'''
def quicksort(array):
    return []

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
'''

def partition(array, first, last):
    pivot = array[first]

    left = first + 1
    right = last

    done = False

    while not done:
        while left <= right and array[left] <= pivot:
            left += 1

        while array[right] >= pivot and right >= left:
            right -= 1

        if right < left:
            done = True
        else:
            temp = array[left]
            array[left] = array[right]
            array[right] = temp

    temp = array[first]
    array[first] = array[right]
    array[right] = temp

    return right



def sortHelper(array, first, last):
    if first < last:
        split = partition(array, first, last)

        sortHelper(array, first, split - 1)
        sortHelper(array, split + 1, last)

def quickSort(array):
    end = len(array) - 1
    sortHelper(array, 0, end)

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
