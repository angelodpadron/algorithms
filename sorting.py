from typing import List

# merge sort

def mergesort(array: List[int]) -> List[int]:

    # the list contains only one element, so it's already sorted
    if len(array) < 2:
        return array

	# split the main array in half
    left = array[: len(array) // 2]
    right = array[len(array) // 2 :]


    return merge(mergesort(left), mergesort(right))


def merge(left: List[int], right: List[int]) -> List[int]:

    sorted = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted.append(left[left_index])
            left_index += 1
        else:
            sorted.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        sorted.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        sorted.append(right[right_index])
        right_index += 1

    return sorted

# in place merge sort

def mergesort_v2(array: List[int]) -> None:

    if len(array) > 1:

        left = array[:len(array) // 2]
        right = array[len(array) // 2:]

        # sorting both halves with a recursive call (black magic fuckery right here)
        mergesort_v2(left)
        mergesort_v2(right)

        left_index = 0
        right_index = 0
        insertion_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                array[insertion_index] = left[left_index]
                left_index += 1
            else:
                array[insertion_index] = right[right_index]
                right_index += 1

            insertion_index += 1

        while left_index < len(left):
            array[insertion_index] = left[left_index]
            left_index += 1
            insertion_index += 1

        while right_index < len(right):
            array[insertion_index] = right[right_index]
            right_index += 1
            insertion_index += 1







