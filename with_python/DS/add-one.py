"""
    You are given a non-negative number in the form of list elements. For example, the number 123 would be provided
     as arr = [1, 2, 3]. Add one to the number and return the output in the form of a new list.

    Example 1:

    input = [1, 2, 3]
    output = [1, 2, 4]

    Example 2:

    input = [9, 9, 9]
    output = [1, 0, 0, 0]
"""

def add_one(arr):
    borrow = 1

    for i in range(len(arr), 0, -1):
        digit = borrow + arr[i - 1]
        borrow = digit//10

        if borrow == 0:
            arr[i-1] = digit
            break
        else:
            arr[i-1] = digit % 10

    arr = [borrow] + arr

    position = 0
    if arr[position] == 0:
        position += 1
    print(arr[position:])
    return arr[position:]

'''
arr= [9,9,9]

solution = add_one(arr)

print('output: ', solution)
'''


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = add_one(arr)
    for index, element in enumerate(output):
        if element != solution[index]:
            print("Fail")
            return
    print("Pass")

# Test Case 1
arr = [0]
solution = [1]
test_case = [arr, solution]
test_function(test_case)

# Test Case 2
arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_function(test_case)

# Test Case 3
arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_function(test_case)
