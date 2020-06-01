def sqrt(number):
    try:
        int(number)
    except ValueError:
        return None

    if number < 0:
        return None

    if number == 0:
        return 0

    left_value = 1
    right_value = number

    while right_value > left_value + 1:
        mid_value = (left_value + right_value) // 2

        mid_value_square = mid_value * mid_value

        if mid_value_square > number:
            right_value = mid_value
        elif mid_value_square < number:
            left_value = mid_value
        else:
            return mid_value

    return left_value


# Test case 1 - normal case
print("Calling function with value 9")
# Should print pass as the square root is exactly 3
print ("Pass" if  (3 == sqrt(9)) else "Fail")

# Test case 2 - zero value
print("Calling function with value 0")
# Should print pass as the square root is 0
print ("Pass" if  (0 == sqrt(0)) else "Fail")

# Test case 3 - negative value
print("Calling function with negative value -10")
# Should print pass as the function should return None
print ("Pass" if  (None == sqrt(-10)) else "Fail")
