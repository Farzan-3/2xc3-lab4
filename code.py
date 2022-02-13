from venv import create
import sorts
import random
import timeit
import matplotlib.pyplot as plt

#Lab4.py function
def mergesort(L):
    
    if len(L) <= 1:
        return 
    mid = len(L)//2 
    left, right = L[:mid], L[mid:]

    #Mergesort core
    mergesort(left)
    mergesort(right)
    temp = merge(left, right)

    #Copy the sorted list to L
    for i in range(len(temp)):
        L[i] = temp[i]

#Lab4.py function
def merge(left, right):
    L = []
    i = j = 0

    while i < len(left) or j < len(right):
        #Check it there's still elements to be merged from left and/or right
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j+=1
    return L

#mergesort_three
def mergesort_three(L):
    if len(L) <= 1:
        return 
    if len(L) == 2:
        if L[0] > L[1]:
            L[0], L[1] = L[1], L[0]
        return 
    mid = len(L)//3
    left, right, middle = L[:mid], L[mid:mid*2], L[mid*2:]

    mergesort_three(left)
    mergesort_three(right)
    mergesort_three(middle) 
    temp = merge_three(left, right, middle)

    for i in range(len(temp)):
        L[i] = temp[i]

#merge_three
def merge_three(left, right, middle):
    L = []
    i = j = k = 0

    while i < len(left) or j < len(right) or k < len(middle):
        #Check it there's still elements to be merged from left and/or right
        if i >= len(left):
            if j >= len(right):
                L.append(middle[k])
                k +=1
            elif k >= len(middle) or right[j] <= middle[k]:
                L.append(right[j])
                j += 1
            else: 
                L.append(middle[k])
                k +=  1
        elif j >= len(right):
            if i >= len(left):
                L.append(middle[k])
            elif k >= len(middle) or left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else: 
                L.append(middle[k])
                k += 1
        elif k >= len(middle):
            if left[i] <= left[j]:
                L.append(left[i])
            else: 
                L.append(right[j])
                j += 1
        else:
            if left[i] <= right[j] and left[i] <= middle[k]:
                L.append(left[i])
                i += 1
            elif right[j] <= left[i] and right[j] <= middle[k]:
                L.append(right[j])
                j += 1
            else:
                L.append(middle[k])
                k+=1
    return L     

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L

bottomUpTs = []
lab4Ts = []
ns = [i for i in range(100)]
for i in range(100):
    L = create_random_list(i)
    temp = L
    start1 = timeit.default_timer()
    sorts.mergesort_bottom(L)
    end1 = timeit.default_timer()

    start2 = timeit.default_timer()
    mergesort(temp)
    end2 = timeit.default_timer()

    bottomUpTs.append(end1 - start1)
    lab4Ts.append(end2 - start2)

plt.plot(ns, bottomUpTs, '.', label="Bottom-Up Mergesort")
plt.plot(ns, lab4Ts, '.', label="lab4 Mergesort")
plt.xlabel("size of list (n)")
plt.ylabel("time (t)")
plt.title("Performance of Mergesorts")
plt.legend(loc="upper left")
plt.show()