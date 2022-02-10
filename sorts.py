import random
from venv import create

def mergesort_bottom(L):
    window = 2
    for _ in range(len(L) - 2):
        for j in range(0, len(L), window):
            merge_bottom(L, j, int(j + (window)/2), j + window)
        window *= 2
    return
def merge_bottom(L, start, mid, end):
    temp = []
    left = L[start:mid]
    right = L[mid:end]
    while(len(left) + len(right) > 0):
        if len(left) == 0:
            minimum = min(right)
        elif len(right) == 0:
            minimum = min(left)
        else:
            minimum = min(min(left), min(right))

        temp.append(minimum)
        if minimum in left:
            left.remove(minimum)
            continue
        right.remove(minimum)
    
    L[start:end] = temp

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L