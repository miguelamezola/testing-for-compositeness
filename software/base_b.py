#!/usr/bin/python3

"""Base b representations and operations."""

from utils import are_integers

def convert(num, base):
    """Base b represenation of any integer.

    Args:

    Returns:

    Raises:

    """

    # num and base should both be integers
    if not are_integers(num, base):
        raise Exception('num and base must be integers')   

    # contains digits in new base 
    representation = []

    # for each digit in the origin base
    while num > 0:
        # compute remainder
        remainder = num % base
        # add remainder to base b represenation
        representation = [remainder] + representation
        # compute new value for num
        num = num // base

    return representation

def revert(num, base):
    """Returns base 10 representation of base b number.

    Args:

    Returns:

    Raises:

    """

    sum = 0

    for index, digit in enumerate(num):
        sum += digit * base ** (len(num) - index - 1)

    return sum


def add(m, n, base):
    """Addition in base b.

    Args:

    Returns:

    Raises:

    """
    # make use x greater than or equal to y
    if len(n) >= len(m):
        x, y = n.copy(), m.copy()
    else:
        x, y = m.copy(), n.copy()

    # store digits of sum here
    sum = []

    # carry starts as empty sum
    carry = 0

    # for each digit in x
    while len(x) > 0:
        # remove next digit from x and y
        x_digit = x.pop()
        if len(y) > 0:
            y_digit = y.pop()
        else:
            y_digit = 0

        # add x and y digits, together with carry value
        sum = [(x_digit + y_digit + carry) % base] + sum
        carry = (x_digit + y_digit + carry) // base

    # add any leftover carry values
    if carry > 0:
        sum = [carry] + sum

    return sum

def multiply(m, n, base):
    """Long multiplication in base b.

    Args:
        m: A base b represenation of an integer.
        n: A base b represenation of an integer.
        base: An intger greater than or equal to 2.

    Returns:

    Raises:

    """

    # base should an integer greater than or equal to 2
    if not are_integers(base):
        raise Exception('base must be integers')   
    if not base >= 2:
        raise Exception('base must be greater than or equal to 2')

    # Long multiplication requires the top number x to be greater than or equal
    # to the bottom number y.
    #
    # For example,
    #
    #   100 <- x
    # x  23 <- y
    #  ----
    #   300 <- partial product
    # +2000 <- partial product
    #  ----
    #  2300
    if len(n) >= len(m):
        x, y = n.copy(), m.copy()
    else:
        x, y = m.copy(), n.copy()


    partial_prods = [] # collection of partial products (see example above)
    zeros = 0

    # for each digit in the bottom number y
    while len(y) > 0:

        partial_product = [] # partial product
        carry = 0

        # Append appropriate number of zeros to right-most positions in product.
        # No zeros will be appended to first partial product, 1 zero will be
        # appended to second partial product, 2 zeros to the third partial 
        # product, and so forth.
        for index in range(zeros):
            partial_product.append(0)

        y_digit = y.pop() # get the right-most digit in the bottom number y 

        # Multiply the current y digit by each digit in the top number from 
        # right to left.
        for x_digit in reversed(x):
            product = y_digit * x_digit + carry
            partial_product = [product % base] + partial_product
            carry = product // base

        # final carry
        if carry > 0:
            # partial_product = [carry] + partial_product
            partial_product = [carry % base] + partial_product
            partial_product = [carry // base] + partial_product

        partial_prods.append(partial_product)

        zeros = zeros + 1

    # Add all the partial products together.
    sum = partial_prods.pop()
    while len(partial_prods) > 0:
        sum = add(sum, partial_prods.pop(), base)

    return sum
    
__author__ = "Miguel Amezola"
__copyright__ = "Copyright 2017, Miguel Amezola"
__credits__ = []

__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Miguel Amezola"
__email__ = "math@miguelamezola.com"
__status__ = "Development"
