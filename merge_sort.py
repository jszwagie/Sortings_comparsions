def merge_sort(array):
    result = []
    if len(array) <= 1:
        return array
    midpoint = len(array) // 2
    left = array[0:midpoint]
    right = array[midpoint:]
    left = merge_sort(left)
    right = merge_sort(right)
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
