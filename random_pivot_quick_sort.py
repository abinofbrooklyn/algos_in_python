import random

def quick_sort(arr,start,stop):
    if start < stop:
        pivotIndex = randompivot(arr,start,stop)
        quick_sort(arr,start,pivotIndex)
        quick_sort(arr,pivotIndex+1,stop)

def randompivot(arr,start,stop):
    rand_pivot = random.randrange(start,stop)
    arr[start], arr[rand_pivot] = arr[rand_pivot], arr[start]
    return partition(arr,start,stop)

def partition(arr,start,stop):
    pivot = start
    i = start - 1
    j = stop + 1
    while True:
        while True:
            i = i + 1
            if arr[i] >= arr[pivot]:
                break
        while True:
            j = j - 1
            if arr[j] <= arr[pivot]:
                break
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


ints = open('IntegerArray.txt','r')
ints_list = list(map(int,ints.read().split('\n')[:-1]))
ints.close()

quick_sort(ints_list,0,len(ints_list)-1)
print(ints_list)
