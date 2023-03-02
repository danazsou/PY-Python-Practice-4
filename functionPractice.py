"""
Write a Python function called max_num()to find the
maximum of three numbers
"""


def max_num(a, b, c):
    return max(a, b, c)


print(max_num(7, 13, 67))

"""
Write a Python function called mult_list()
 to multiply all the numbers in a list
"""


def mult_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result


my_list = [4, 3, 6, 7, 13]
result = mult_list(my_list)
print(result)


"""
Write a Python function called rev_string()
to reverse a string
"""


def rev_string(string):
    return string[::-1]


this_string = "It is finally sunny outside!"
reversed_string = rev_string(this_string)\

print(reversed_string)

"""
Write a Python function called num_within() to check whether a number falls in a given range.
The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False
"""


def num_within(num, start, end):
    if num >= start and num <= end:
        return True
    else:
        return False


my_num = 77
start_range = 25
end_range = 70
result = num_within(my_num, start_range, end_range)
print(result)

"""
Write a Python function called pascal() that prints out the first n rows of 
Pascal's triangle.

        The function accepts the number n, the number of rows to print

            Note : Pascal's triangle is an arithmetic and 
            geometric figure first imagined by Blaise Pascal. 
            Each number is the two numbers above it added together.
"""


def pascal(n):
    # Create an empty list to hold the rows of the triangle
    triangle = []

    # Loop over each row from 0 to n-1
    for i in range(n):
        # Create a new list to hold the current row
        row = []
        # Loop over each element in the row from 0 to i
        for j in range(i+1):
            # If we're at the first or last element in the row, set it to 1
            if j == 0 or j == i:
                row.append(1)
            # Otherwise, set it to the sum of the two elements above it
            else:
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # Add the completed row to the triangle list
        triangle.append(row)

    # Print out the triangle
    for row in triangle:
        print(row)
