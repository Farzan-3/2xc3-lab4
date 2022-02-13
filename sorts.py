#Lab4.py function
def mergesort(L):
    
    if len(L) <= 1:
        return 
    mid = len(L)//2 
    left, middle = L[:mid], L[mid:]

    #Mergesort core
    mergesort(left)
    mergesort(middle)
    temp = merge(left, middle)

    #Copy the sorted list to L
    for i in range(len(temp)):
        L[i] = temp[i]

#Lab4.py function
def merge(left, middle):
    L = []
    i = j = 0

    while i < len(left) or j < len(middle):
        #Check it there's still elements to be merged from left and/or middle
        if i >= len(left):
            L.append(middle[j])
            j += 1
        elif j >= len(middle):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= middle[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(middle[j])
                j+=1
    return L

# Bottom up mergesort
def mergesort_bottom(L):
    window = 1
    high = len(L)
    while window <= high:
        for i in range(0, high, 2*window):
            merge_bottom(L, i, i + window - 1, min(i + 2*window - 1, high))
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

#mergesort_three
def mergesort_three(L):
    if len(L) <= 1:
        return 
    if len(L) == 2:
        if L[0] > L[1]:
            L[0], L[1] = L[1], L[0]
        return 
    mid = len(L)//3
    left, middle, right  = L[:mid], L[mid:mid*2], L[mid*2:]

    mergesort_three(left)
    mergesort_three(middle)
    mergesort_three(right ) 
    temp = merge_three(left, middle, right )

    for i in range(len(temp)):
        L[i] = temp[i]

#merge_three
def merge_three(left, middle, right ):
    L = []
    i = j = k = 0

    while i < len(left) or j < len(middle) or k < len(right ):
        #Check it there's still elements to be merged from left and/or middle
        if i >= len(left):
            if j >= len(middle):
                L.append(right [k])
                k +=1
            elif k >= len(right ) or middle[j] <= right [k]:
                L.append(middle[j])
                j += 1
            else: 
                L.append(right [k])
                k +=  1
        elif j >= len(middle):
            if i >= len(left):
                L.append(right [k])
                k += 1
            elif k >= len(right ) or left[i] <= right [k]:
                L.append(left[i])
                i += 1
            else: 
                L.append(right [k])
                k += 1
        elif k >= len(right ):
            if left[i] <= middle[j]:
                L.append(left[i])
                i += 1
            else: 
                L.append(middle[j])
                j += 1
        else:
            if left[i] <= middle[j] and left[i] <= right [k]:
                L.append(left[i])
                i += 1
            elif middle[j] <= left[i] and middle[j] <= right [k]:
                L.append(middle[j])
                j += 1
            else:
                L.append(right [k])
                k+=1
    return L