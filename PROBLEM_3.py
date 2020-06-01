def joine(left, right):

    l_index = 0
    r_index = 0

    together = []
    while(l_index < len(left) and r_index < len(right)):
        if(left[l_index] < right[r_index]):
            together.append(right[r_index])
            r_index += 1
        else:
            together.append(left[l_index])
            l_index += 1

    together += left[l_index:]
    together += right[r_index:]

    return together


def sort(input_list):

    if(len(input_list) <= 1):
        return input_list

    mid = len(input_list)//2

    left = input_list[:mid]
    right = input_list[mid:]

    left = sort(left)
    right = sort(right)

    return joine(left, right)


def rearrange_digits(input_list):
    if(not(len(input_list))):
        return "Empty Input List"
    input_list = sort(input_list)
    order = 1
    counter = 1
    num1 = 0
    num2 = 0
    for i in reversed(range(len(input_list))):
        if(counter == 1):
            num1 += (order*input_list[i])
            counter = 2
        elif(counter == 2):
            num2 += (order*input_list[i])
            counter = 1
            order *= 10
    return [num1, num2]


print(rearrange_digits([3, 5, 1, 4, 2]))  # prints [531,42]
print(rearrange_digits([4]))  # prints [4,0]
print(rearrange_digits([]))  # prints Empty Input List
