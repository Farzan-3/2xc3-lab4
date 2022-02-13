import sorts
import random
import timeit
import math
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
                k += 1
            elif k >= len(middle) or left[i] <= middle[k]:
                L.append(left[i])
                i += 1
            else: 
                L.append(middle[k])
                k += 1
        elif k >= len(middle):
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
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

def create_near_sorted_list(n, factor):
    l= create_random_list(n)
    l.sort()
    for _ in range(math.ceil(n * factor)):
        index1 = random.randint(0, n - 1)
        index2 = random.randint(0, n - 1)
        l[index1], l[index2] = l[index2], l[index1]
    return l

def test(function, name):
    ns = [i for i in range(1, 1001)]
    ts = []

    for i in range(1000):
        L = create_random_list(i)
        start = timeit.default_timer()
        function(L)
        end = timeit.default_timer()
        ts.append(end - start)
    plt.plot(ns, ts, '.', label=name)
    ts.clear() 

def test1(function, name):
    ns = [i/1000 for i in range(500)]
    ts = []

    for i in range(500):
        L = create_near_sorted_list(1000,i/1000)
        start = timeit.default_timer()
        function(L)
        end = timeit.default_timer()
        ts.append(end - start)
    plt.plot(ns, ts, '.', label=name)
    ts.clear() 

test(sorts.mergesort_bottom, "Bottom-Up Mergesort")
test(mergesort, "lab4 Mergesort")
plt.xlabel("size of list (n)")
plt.ylabel("time (t)")
plt.title("Performance of Mergesorts")
plt.legend(loc="upper left")
plt.show()

test(mergesort_three, "Mergesort three")
test(mergesort, "lab4 Mergesort")
plt.xlabel("size of list (n)")
plt.ylabel("time (t)")
plt.title("Performance of Mergesorts")
plt.legend(loc="upper left")
plt.show()

test1(mergesort_three, "Mergesort three")
plt.xlabel("factor")
plt.ylabel("time (t)")
plt.title("Performance of Mergesorts")
plt.legend(loc="upper left")
plt.show()