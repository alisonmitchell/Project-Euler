import doctest
import timeit

"""
Problem 1: https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

# iteration
def sum_of_multiples_iteration(max_value: int =1000) -> int:
    """
    Find the sum of all multiples between 1 and max_value that are divisible by 3 or 5.

    :param max_value: Integer greater than 1
 
    :returns: Integer

    >>> sum_of_multiples_iteration(5)
    3
    >>> [sum_of_multiples_iteration(i+1) for i in [3,5,6]] 
    [3, 8, 14]
    >>> try:
    ...     sum_of_multiples_iteration(max_value=1)
    ... except AssertionError as err:
    ...     print(f'Error found:{err}')
    Error found:The argument must be greater than 1
    """
    assert max_value > 1, "The argument must be greater than 1"

    total_sum = 0
    for i in range(1, max_value):
        if (i % 3 == 0 or i % 5 == 0):
            total_sum += i
    return total_sum

print(sum_of_multiples_iteration(max_value=1000))


# lambda function
def sum_of_multiples_lambda(max_value: int = 1000) -> int:
    """
    Find the sum of all the multiples of 3 or 5 below 1000.

    :param max_value: Integer greater than 1
 
    :returns: Integer.

    >>> sum_of_multiples_lambda(5)
    3
    >>> [sum_of_multiples_lambda(i+1) for i in [3,5,6]] 
    [3, 8, 14]
    >>> try:
    ...     sum_of_multiples_lambda(max_value=1)
    ... except AssertionError as err:
    ...     print(f'Error found:{err}')
    Error found:The argument must be greater than 1
    """
    assert max_value > 1, "The argument must be greater than 1"

    return sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(max_value))) 

print(sum_of_multiples_lambda(max_value=1000))


# list comprehension
def sum_of_multiples_list(max_value: int = 1000) -> int:
    """
    Find the sum of all the multiples below 1000 that are divisible by either 3 or 5.
    
    :param max_value: Integer greater than 1
 
    :returns: Integer.

    >>> sum_of_multiples_list(5)
    3
    >>> [sum_of_multiples_list(i+1) for i in [3,5,6]] 
    [3, 8, 14]
    >>> try:
    ...     sum_of_multiples_list(max_value=1)
    ... except AssertionError as err:
    ...     print(f'Error found:{err}')
    Error found:The argument must be greater than 1
    """
    assert max_value > 1, "The argument must be greater than 1"

    return sum([i for i in range(max_value) if i % 3 == 0 or i % 5 == 0])

print(sum_of_multiples_list(max_value=1000))


# generator expression
def sum_of_multiples_gen(max_value: int = 1000) -> int:
    """
    Find the sum of all the multiples below 1000 that are divisible by either 3 or 5.

    :param max_value: Integer greater than 1
 
    :returns: Integer.

    >>> sum_of_multiples_gen(5)
    3
    >>> [sum_of_multiples_gen(i+1) for i in [3,5,6]] 
    [3, 8, 14]
    >>> try:
    ...     sum_of_multiples_gen(max_value=1)
    ... except AssertionError as err:
    ...     print(f'Error found:{err}')
    Error found:The argument must be greater than 1
    """
    assert max_value > 1, "The argument must be greater than 1"

    return sum(i for i in range(max_value) if i % 3 == 0 or i % 5 == 0) 

print(sum_of_multiples_gen(max_value=1000))


# convert list to set
def sum_of_multiples_use_set(max_value: int = 1000) -> int:
    """
    Find the sum of all the multiples of 3 or 5 below 1000.
    
    :param max_value: Integer greater than 1
 
    :returns: Integer.

    >>> sum_of_multiples_use_set(5)
    3
    >>> [sum_of_multiples_use_set(i+1) for i in [3,5,6]] 
    [3, 8, 14]
    >>> try:
    ...     sum_of_multiples_use_set(max_value=1)
    ... except AssertionError as err:
    ...     print(f'Error found:{err}')
    Error found:The argument must be greater than 1
    """
    assert max_value > 1, "The argument must be greater than 1"

    return sum(set(list(range(3, max_value, 3)) + list(range(5, max_value, 5))))
    
print(sum_of_multiples_use_set(max_value=1000))


# range unpacking into a set
def sum_of_multiples_unpack(max_value=1000):
    """
    Find the sum of all the multiples of 3 or 5 below 1000.

    :param max_value: Integer greater than 1
 
    :returns: Integer.  

    >>> sum_of_multiples_unpack(5)
    3
    >>> [sum_of_multiples_unpack(i+1) for i in [3,5,6]] 
    [3, 8, 14]
    >>> try:
    ...     sum_of_multiples_unpack(max_value=1)
    ... except AssertionError as err:
    ...     print(f'Error found:{err}')
    Error found:The argument must be greater than 1
    """
    assert max_value > 1, "The argument must be greater than 1"

    return sum({*range(3, max_value, 3)} | {*range(5, max_value, 5)}) 

print(sum_of_multiples_unpack(max_value=1000))


def time_function(function_name: str, n_retry:int = 10) -> True:
    """
    Timing function
    
    :param function_name: Name of function to be timed
    :param n_retry: Number of times the function is run to improve the average
    :return: True
    """
    meas_time = timeit.timeit(function_name + "()",
                              setup="from __main__ import " + function_name,
                              number = n_retry)
    average_time = 1000 * meas_time / n_retry
    print(f"Average time of {function_name}: {average_time}ms")
    return True


def main():
    print(f"\n*** Time solution ***")
    n_retry = 1000
    time_function("sum_of_multiples_iteration", n_retry)
    time_function("sum_of_multiples_lambda", n_retry)
    time_function("sum_of_multiples_list", n_retry)
    time_function("sum_of_multiples_gen", n_retry)
    time_function("sum_of_multiples_use_set", n_retry)
    time_function("sum_of_multiples_unpack", n_retry)
    

#-------------------------------------------------------------


if __name__ == "__main__":
    print("\n*** DOCTEST ***")
    failure_count, test_count = doctest.testmod(verbose=False)
    assert failure_count == 0, 'Test failure... bailing out'
    print(f'All {test_count} tests passed')
    main() 