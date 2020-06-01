def heapsort(arr):
    arr_len = len(arr)

    for i in range(arr_len - 1, -1, -1):
        heapify(arr, len(arr), i)
        arr[0], arr[i] = arr[i], arr[0]


def heapify(arr, n, i):
    for i in range(1, i + 1):
        data_index = i
        while data_index > 0:
            parent_index = (data_index - 1) // 2
            if arr[data_index] > arr[parent_index]:
                arr[data_index], arr[parent_index] = arr[parent_index], arr[data_index]
                data_index = parent_index
            else:
                break


def rearrange_digits(input_list):
    if len(input_list) == 0:
        return []
    heapsort(input_list)
    number_1_list = list()
    number_2_list = list()

    input_list_len = len(input_list)
    if input_list_len % 2 == 1:
        digit = input_list.pop()
        number_1_list.append(digit)
    input_list_len = len(input_list)
    for i in range(input_list_len, 0, -1):
        digit = input_list.pop()
        if i % 2 == 0:
            number_1_list.append(digit)
        else:
            number_2_list.append(digit)
    number_1_str = ''.join(str(n) for n in number_1_list)
    number_2_str = ''.join(str(n) for n in number_2_list)
    number_1 = int(number_1_str)
    number_2 = int(number_2_str)

    return [number_1, number_2]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Test case 1 - un-sorted array as input
print("Calling function with un-sorted array: [4, 6, 2, 5, 9, 8]")
test_case_1 = [[4, 6, 2, 5, 9, 8], [964, 852]]
# Should print pass as the output should be [964, 852]
test_function(test_case_1)

# Test case 2 - sorted array as input
test_case_2 = [[1, 2, 3, 4, 5], [542, 31]]
# Should print pass as the output should be [542, 31]
test_function(test_case_2)

# Test case 3 - empty array as input
test_case_3 = [[], []]
# Should print pass as the output should be []
test_function(test_case_3)