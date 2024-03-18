from random import randint


def modifying_quick_sort(array, left, right):
    if left < right:
        base_right = right
        base_left = left
        pivot_index = randint(left, right)
        pivot = array[pivot_index]
        while left < right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        modifying_quick_sort(array, base_left, right)
        modifying_quick_sort(array, left, base_right)


def quick_sort(original_array):
    array = original_array.copy()
    left = 0
    right = len(array) - 1
    modifying_quick_sort(array, left, right)
    return array
