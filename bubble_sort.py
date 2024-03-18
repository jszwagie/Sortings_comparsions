def bubble_sort(original_array):
    array = original_array.copy()
    for i in range(len(array)):
        is_sorted = True
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_sorted = False
        if is_sorted:
            break
    return array
