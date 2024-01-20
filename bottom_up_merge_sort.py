import random
import time


def bottom_up_merge(array, left, mid, right):
    temp = []
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if array[i] < array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1

    while i <= mid:
        temp.append(array[i])
        i += 1

    while j <= right:
        temp.append(array[j])
        j += 1

    for i in range(len(temp)):
        array[left + i] = temp[i]


def bottom_up_merge_sort(array):
    n = len(array)
    size = 1

    while size < n:
        left = 0
        while left < n - 1:
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            bottom_up_merge(array, left, mid, right)
            left += 2 * size

        size *= 2

    return array


# Input Size
input_size = 100
# Create random array
array = list(range(1, input_size + 1))
random.shuffle(array)
# Display random array
print(f"Unsorted: {array}")
# Start Timer
start_time = time.time()
# Sort array
sorted_array = bottom_up_merge_sort(array)
# End Timer
end_time = time.time()
# Calculate duration
duration = end_time - start_time
# Display sorted array
print(f"Sorted: {sorted_array}")
# Display duration
print(f"Duration: {duration}")
