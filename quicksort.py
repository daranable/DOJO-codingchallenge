def swap(low, high, arr):
    temp = arr[low]
    arr[low] = arr[high]
    arr[high] = temp

def partition(low, high, pivot, arr):
    #hoare partition
    while pivot < low:
        if arr[low] < arr[pivot]:
            low += 1
        elif arr[high] > arr[pivot]:
            high -= 1
        elif low != high and high > low:
            swap(low, high, arr)
            print arr
        # print low, high, pivot, ":",arr[low], arr[high], arr[pivot]
        # else:
        if low == high or high < low:
            if arr[high] < arr[pivot]:
                swap(high, pivot, arr)
                pivot = high
                return pivot
            elif high == pivot:
                return pivot
            else:
                high -= 1
                continue

def sort(low,high,arr):
    pivot = low
    low += 1
    part = partition(low, high, pivot, arr)
    low -= 1
    if abs(low - (part-1)) > 1:
        sort(low,part-1,arr)
    if abs(high - (part+1)) > 1:
        sort(part+1,high,arr)


def quicksort(arr):
    print "start", arr
    sort(0,len(arr)-1,arr)
    return arr

print quicksort([15,2,20,30,5,89,3,6,11,95])
print quicksort([32,15, 7, 13, 5, 3, 2])
print quicksort([155743,2,2,7,9,8,0])
print quicksort([4,0,6,2,5,1,7,3])
