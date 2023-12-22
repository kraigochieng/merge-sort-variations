import random
import time


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append remaining elements from left and right, if any
    for k in range(i, len(left)):
        result.append(left[k])

    for k in range(j, len(right)):
        result.append(right[k])

    return result


def basic_merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left_array = []
    for i in range(mid):
        left_array.append(array[i])

    right_array = []
    for i in range(mid, len(array)):
        right_array.append(array[i])

    left = basic_merge_sort(left_array)
    right = basic_merge_sort(right_array)

    return merge(left, right)


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
sorted_array = basic_merge_sort(array)
# End Timer
end_time = time.time()
# Calculate duration
duration = end_time - start_time
# Display sorted array
print(f"Sorted: {sorted_array}")
# Display duration
print(f"Duration: {duration}")
