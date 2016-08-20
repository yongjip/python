def quicksort(array):

    if len(array) > 1:
        pivot = array[-1]
        less = []
        equal = [pivot]
        greater = []
        for item in array[:-1]:
            if item < pivot:
                less.append(item)
            elif item == pivot:
                equal.append(item)
            else:
                greater.append(item)
        return quicksort(less) + equal + quicksort(greater)
    return array

def qsort(array):
    if len(array) < 1:
        return array
    else:
        return qsort([x for x in array[1:] if x<array[0]]) + [array[0]] + qsort([x for x in array[1:] if x>=array[0]])

def qsort(array):
    if len(array) < 1:
        return array
    else:
        return qsort([x for x in array[:-1] if x<=array[-1]]) + [array[-1]] + qsort([x for x in array[:-1] if x>array[-1]])
