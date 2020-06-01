def rotated_array_search(input_list, number):
    if not isinstance(input_list, list):
        return -1

    if len(input_list) == 0:
        return -1

    l_index = 0
    r_index = len(input_list) - 1

    while r_index > l_index + 1:
        middle_index = (r_index + l_index) // 2

        middle_value = input_list[middle_index]

        if middle_value == number:
            return middle_index

        if input_list[l_index] < middle_value < input_list[r_index]:
            if number > middle_value:
                l_index = middle_index
            else:
                r_index = middle_index
        elif middle_value > input_list[l_index] and middle_value > input_list[r_index]:
            if input_list[l_index] <= number < middle_value:
                r_index = middle_index
            else:
                l_index = middle_index
        elif middle_value < input_list[l_index] and middle_value < input_list[r_index]:
            if middle_value < number <= input_list[r_index]:
                l_index = middle_index
            else:
                r_index = middle_index

    if input_list[l_index] == number:
        return l_index
    elif input_list[r_index] == number:
        return r_index
    else:
        return -1


def search_linear(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def testfunction(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if search_linear(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# Test case 1 - array with non-rotated values
print("Calling function with non-rotated array: [1, 2, 3, 4], target value = 3")
# Should print Pass as the index should be 2
testfunction([[1, 2, 3, 4], 3])

print("Calling function with rotated array: [6, 7, 8, 9, 10, 1, 2, 3, 4], target value = 1")
# Should print Pass as the index should be 5
testfunction([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])

# Test case 3 - non-list inut
print("Calling function with non-list input: 10, target value = 5")
# Should print Pass as the index should be -1
testfunction([[], 5])
