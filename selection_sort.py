def selection_sort(original_array):
    array = original_array.copy()
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array = swap(array, i, min_index)
    return array


def swap(array, base_index, min_index):
    array[base_index], array[min_index] = array[min_index], array[base_index]
    return array
