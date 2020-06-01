def sort_012(input_list):
    index = 0
    next_0 = 0
    next_2 = len(input_list) - 1

    while index <= next_2:
        if input_list[index] == 0:
            input_list[index] = input_list[next_0] # Makes sure we don't accidentially overwrite a value
            input_list[next_0] = 0
            next_0 += 1
            index += 1
        elif input_list[index] == 2:
            input_list[index] = input_list[next_2] # Makes sure we don't accidentially overwrite a value
            input_list[next_2] = 2
            next_2 -= 1
        else:
            index += 1

    return input_list

def function_test(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

function_test([])

function_test([0])
function_test([1])
function_test([2])

function_test([0, 0])
function_test([0, 1])
function_test([2, 1])

function_test([0, 1, 2])
function_test([1, 2, 0])
function_test([2, 1, 0])

function_test([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
function_test([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
function_test([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Test case 3 - array with only a single element
# Should print [0]
print("Calling function with sorted array: [0]")
# Should print Pass as the result array should be the same array
function_test([0])
