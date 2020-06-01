def sort_012(input_list):
    top_of_zero_idx = 0                     
    one_idx = 0                             
    bottom_of_2_idx = len(input_list) - 1   
    while one_idx <= bottom_of_2_idx:
        if input_list[one_idx] == 0:
            input_list[one_idx], input_list[top_of_zero_idx] = input_list[top_of_zero_idx], input_list[one_idx]
            top_of_zero_idx += 1
            one_idx += 1
        elif input_list[one_idx] == 1:
            one_idx += 1
        elif input_list[one_idx] == 2:
            input_list[one_idx], input_list[bottom_of_2_idx] = input_list[bottom_of_2_idx], input_list[one_idx]
            bottom_of_2_idx -= 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# Test case 1 - unsorted array
print("Calling function with un-sorted array: [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]")
# Should print [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# Should print Pass as the result array should be a correctly sorted array
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])

# Test case 2 - sorted array
# Should print [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
print("Calling function with sorted array: [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]")
# Should print Pass as the result array should be the same sorted array
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Test case 3 - array with only a single element
# Should print [0]
print("Calling function with sorted array: [0]")
# Should print Pass as the result array should be the same array
test_function([0])