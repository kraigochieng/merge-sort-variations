import random
import time


def top_down_merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    for k in range(i, len(left)):
        result.append(left[k])

    for k in range(j, len(right)):
        result.append(right[k])

    return result


def top_down_merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2

    left = []
    for i in range(mid):
        left.append(data[i])

    right = []
    for i in range(mid, len(data)):
        right.append(data[i])

    left = top_down_merge_sort(left)
    right = top_down_merge_sort(right)

    return top_down_merge(left, right)


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
sorted_array = top_down_merge_sort(array)
# End Timer
end_time = time.time()
# Calculate duration
duration = end_time - start_time
# Display sorted array
print(f"Sorted: {sorted_array}")
# Display duration
print(f"Duration: {duration}")
