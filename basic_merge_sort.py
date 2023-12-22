import random
import time

# start_time = 0
# end_time = 0
# duration = 0


def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2

    left_array = []
    for i in range(mid):
        left_array.append(data[i])

    right_array = []
    for i in range(mid, len(data)):
        right_array.append(data[i])

    left = merge_sort(left_array)
    right = merge_sort(right_array)

    return merge(left, right)


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


# Example usage
last_number = 100
data = list(range(1, last_number + 1))
random.shuffle(data)
print(f"Unsorted data: {data}")
start_time = time.time()
sorted_data = merge_sort(data)
end_time = time.time()
duration = end_time - start_time
print(f"Sorted data: {sorted_data}")
print(f"Duration: {duration}")
