def binary_search_recursive(arr, x, left, right):
    if left > right:
        return False

    mid = left + ((right - left) // 2)
    # mid = (left + right) // 2

    if arr[mid] == x:
        return True
    elif x < arr[mid]:
        return binary_search_recursive(arr, x, left, mid - 1)
    else:
        return binary_search_recursive(arr, x, mid + 1, right)

    return False


def binary_search_iterative(array, x):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if x == array[mid]:
            return True

        elif x < array[mid]:
            right = mid - 1

        else:
            left = mid + 1

    return -1

""" 
# Recursive
numbers = [1, 3, 4, 5, 13, 20, 25, 40, 42, 44, 53]
length = len(numbers)

result = binary_search_recursive(numbers, 42, 0, length)
print(result)
"""

# Iterative
numbers = [1, 3, 4, 5, 13, 20, 25, 40, 42, 44, 53]

result = binary_search_iterative(numbers, 42)
print(result)