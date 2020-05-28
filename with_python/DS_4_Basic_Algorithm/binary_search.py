
def binary_search_recursive(arr, x, left, right):
    print("left : {} , right : {}".format(left, right))

    if left > right:
        return False

    mid = left + ((right - left) // 2)
    print("   mid = ", mid)

    if arr[mid] == x:
        return True
    elif x < arr[mid]:
        return binary_search_recursive(arr, x, left, mid-1)
    else:
        return binary_search_recursive(arr, x, mid+1, right)

    return False


numbers = [1, 3, 4, 5, 13, 20, 25, 40, 42, 44, 53]
length = len(numbers)

result = binary_search_recursive(numbers, 42, 0, length)
print(result)

