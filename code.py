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