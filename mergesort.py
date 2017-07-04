import math
def merge_compare(lista, listb):
    a = merge_compare(lista[:len(lista)/2], lista[len(lista)/2:]) if len(lista) > 1 else lista
    b = merge_compare(listb[:len(listb)/2], listb[len(listb)/2:]) if len(listb) > 1 else listb
    out = []
    pointera = 0
    pointerb = 0
    while pointera < len(a) or pointerb < len(b):
        if pointera < len(a) and pointerb == len(b):
            out += a[pointera:]
            pointera = len(a)
        elif pointerb < len(b) and pointera == len(a):
            out += b[pointerb:]
            pointerb = len(b)
        elif a[pointera] <= b[pointerb]:
            out.append(a[pointera])
            pointera += 1
        elif b[pointerb] < a[pointera]:
            out.append(b[pointerb])
            pointerb += 1
    return out

def mergesort(collection):
    return merge_compare(collection[:len(collection)/2], collection[len(collection)/2:])

print mergesort([32,15, 7, 13, 5, 3, 2])
print mergesort([155743,2,2,7,9,8,0])
print mergesort([4,0,6,2,5,1,7,3])
