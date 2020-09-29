import doctest
import timeit

"""
Problem 6: https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... 10**2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers 
and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def solution_1(input_number: int = 101) -> int:
    """
    Find solution using generator function

    :param input_number: integer

    :returns: integer
    
    >>> solution_1(11)
    2640
    """
    sequence = range(1, input_number)
    sum_of_squares = sum(i ** 2 for i in sequence) 
    square_of_sum = sum(sequence) ** 2

    return square_of_sum - sum_of_squares


def solution_2(input_number: int = 101) -> int:
    """
    Find solution using iteration and squaring by power of 2

    :param input_number: integer

    :returns: integer
    
    >>> solution_2(11)
    2640
    """
    sum_of_squares, sum_of_numbers = 0, 0

    for num in range(1, input_number):
        sum_of_squares += num ** 2
        sum_of_numbers += num

    return sum_of_numbers ** 2 - sum_of_squares
    

def solution_3(input_number: int = 101) -> int:
    """
    Find solution using iteration and squaring by multiplication

    :param input_number: integer

    :returns: integer
    
    >>> solution_3(11)
    2640
    """
    sum_of_squares, sum_of_numbers = 0, 0

    for num in range(1, input_number):
        sum_of_squares += (num * num)
        sum_of_numbers += num

    return (sum_of_numbers * sum_of_numbers) - sum_of_squares


def main() -> True:
    """ 
    Solve problems with different algorithms and measure computation time for each
    
    :returns: True
    """

    input_number = 101

    solutions = ['solution_' + str(i) for i in range(1, 4)]
    
    for solution in solutions:
        print(''.join(['-- ', solution, ' : ', 
                        str(eval(solution + '(' + str(input_number) + ')'))]))
    
    n_retry = 1000
    for function_name in solutions:
        meas_time = timeit.timeit(''.join([function_name,'(',str(input_number),')']),
                                  setup='from __main__ import ' + function_name,
                                  number=n_retry)
        average_time = 1e6 * meas_time / n_retry
        print(f"Average time of {function_name}: {round(average_time, 5)}us")
    return True

#-------------------------------------------------------------


if __name__ == "__main__":
    print("\n*** DOCTEST ***")
    failure_count, test_count = doctest.testmod(verbose=False)
    assert failure_count == 0, 'Test failure... bailing out'
    print(f'All {test_count} tests passed')
    main() 