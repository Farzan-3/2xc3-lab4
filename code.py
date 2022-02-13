import sorts
import random
import timeit
import math
import matplotlib.pyplot as plt

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L

def create_near_sorted_list(n, factor):
    l = create_random_list(n)
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

# Test if all the sorts work as intended
for i in range(1000):
    L1 = create_random_list(i)
    L2 = L1.copy()
    L3 = L1.copy()
    sorts.mergesort(L1)
    sorts.mergesort_three(L2)
    sorts.mergesort_bottom(L3)
    assert(L1 == L2 == L3)

# Bottom Up vs Normal Mergesort test
test(sorts.mergesort_bottom, "Bottom-Up Mergesort")
test(sorts.mergesort, "lab4 Mergesort")
plt.xlabel("size of list (n)")
plt.ylabel("time (t)")
plt.title("Performance of Mergesorts")
plt.legend(loc="upper left")
plt.show()

# Three array vs 2 test
test(sorts.mergesort_three, "Mergesort three")
test(sorts.mergesort, "lab4 Mergesort")
plt.xlabel("size of list (n)")
plt.ylabel("time (t)")
plt.title("Performance of Mergesorts")
plt.legend(loc="upper left")
plt.show()

# Worstcase test
test1(sorts.mergesort_three, "Mergesort three")
plt.xlabel("factor")
plt.ylabel("time (t)")
plt.title("Performance of Mergesorts")
plt.legend(loc="upper left")
plt.show()