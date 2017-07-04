import math
def merge_compare(lista, listb):
    a = merge_compare(lista[:len(lista)/2], lista[len(lista)/2:]) if len(lista) > 1 else lista
    b = merge_compare(listb[:len(listb)/2], listb[len(listb)/2:]) if len(listb) > 1 else listb
    out = []
    while len(a) or len(b):
        if a and not b:
            out += a
            a = []
        elif b and not a:
            out += b
            b = []
        elif a[0] <= b[0]:
            out.append(a[0])
            del a[0]
        elif b[0] < a[0]:
            out.append(b[0])
            del b[0]
    return out

def mergesort(collection):
    return merge_compare(collection[:len(collection)/2], collection[len(collection)/2:])

print mergesort([32,15, 7, 13, 5, 3, 2])
print mergesort([155743,2,2,7,9,8,0])
print mergesort([4,0,6,2,5,1,7,3])
