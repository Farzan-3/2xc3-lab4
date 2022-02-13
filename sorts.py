def mergesort_bottom(L):
    window = 1
    high = len(L) - 1
    while window <= high:
        for i in range(0, high - 1, 2*window):
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