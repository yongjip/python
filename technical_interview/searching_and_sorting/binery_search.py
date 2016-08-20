# Search using while loop
def binary_search(input_array, value):
    middle = len(input_array)/2
    if middle == 0:
        if input_array[0] == value:
            return middle
        return -1
    found = False
    while middle > 0 and middle < len(input_array)-1 and found is False:
        if value == input_array[middle]:
            found = True
        elif value > input_array[middle]:
            if len(input_array[middle + 1:])/2 == 0:
                middle += 1
            else:
                middle = middle + len(input_array[middle + 1:])/2
        else:
            if len(input_array[:middle])/2 == 0:
                middle -= 1
            else:
                middle == len(input_array[:middle])/2
    if found is True:
        return middle
    else:
        return -1

def binary_search(input_array, value):

    first = 0
    last = len(input_array) - 1
    found = False

    while first <= last and found is False:
        midpoint = (first + last) / 2
        if value == input_array[midpoint]:
            found = True
        else:
            if value > input_array[midpoint]:
                first = midpoint + 1
            else:
                last = midpoint - 1

    if found is True:
        return midpoint
    return -1


# Search recursively
def binary_search(input_array, value, first=None, last=None):
    if first is None:
        first = 0
        last = len(input_array) - 1
    midpoint = (first + last) / 2
    if value == input_array[midpoint]:
        return midpoint
    elif first >= last:
        return -1
    else:
        if value < input_array[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
        return binary_search(input_array, value, first=first, last=last)


