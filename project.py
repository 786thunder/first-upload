""" def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 *  num2

    elif operator == "/":
        return num1 / num2

    else:
        return "invalid operator"

print(calculate(9, "-", 4)) 

def apply_discount(price, discount):
    discount_amount = price * (discount / 100)
    final_price = price - discount_amount
    return final_price

item_price = 200
discount_percent = 40
final_price = apply_discount(item_price, discount_percent)
print(final_price)

def extract_integers(original_list):
    integers_list = []
    for element in original_list:
        if type(element) == int:
            integers_list.append(element)
    return integers_list


def filter_integers(lst):
    #initialize an empty list to store integers
    integers = []
    #iterate over elements in the given list
    for element in lst:
        #check if the element is an integer
        if isinstance(element, int):
            #if it is an integer, append it to the list of integers
            integers.append(element)
    #return the list of integers
    return integers

original_list = [1, "hello", 2, "world", 3]
integers_list = filter_integers(original_list)
print(integers_list)

def filter_integers(lst):
    return [i for i in lst if isinstance(i, int)]"""

def decimal_to_binary(decimal):
    # Initialize an empty list to store the binary digits
    binary = []
    # Repeat until the decimal number is zero
    while decimal > 0:
        # Append the remainder of the decimal number divided by 2
        binary.append(decimal % 2)
        # Update the decimal number to be the quotient of the division
        decimal = decimal // 2
    # Reverse the list of binary digits
    binary = binary[::-1]
    # Convert the list of binary digits to a string
    binary_str = ''.join(str(x) for x in binary)
    # Return the binary string
    return binary_str

decimal_num = 1066
binary_num = decimal_to_binary(decimal_num)
print(binary_num)
