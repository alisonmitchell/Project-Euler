from functools import reduce
import doctest
import timeit

"""
Problem 5: https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def solution_1(input_number: int = 21) -> int:
    """
    Find smallest multiple evenly divisible by all numbers from 1 to the input number

    :param input_number: integer

    :returns: integer

    >>> solution_1(10)
    2520
    >>> solution_1()
    232792560
    """

    def gcd(a: int, b: int) -> int:
        """
        Return greatest common divisor according to Euclid's Algorithm using iteration
        
        :param a: integer
        :param b: integer

        :returns: greatest common divisor
        """
        while b:
            a, b = b, a % b
        return a

    def lcm(a: int, b: int) -> int:
        """
        Return least common multiple

        :param a: integer
        :param b: integer

        :returns: least common multiple
        """
        return a * b // gcd(a, b)

    def iter_lcm(*args: range) -> int:
        """
        Return least common multiple of args using functools.reduce
        
        :param *args: pointer to a range call

        :returns: integer
        """   
        return reduce(lcm, args)

    return iter_lcm(*range(2, input_number))
    

def solution_2(input_number: int = 21) -> int:
    """
    Find smallest multiple evenly divisible by all numbers from 1 to the input number

    :param input_number: integer

    :returns: integer

    >>> solution_2(10)
    2520
    >>> solution_2()
    232792560
    """

    def gcd(a: int, b: int) -> int:
        """
        Return greatest common divisor according to Euclid's Algorithm using recursion
        
        :param a: integer
        :param b: integer

        :returns: greatest common divisor
        """
        if a == 0:
            return b
        else:
            return gcd(b % a, a)

    def lcm(a: int, b: int) -> int:
        """
        Return least common multiple

        :param a: integer
        :param b: integer

        :returns: least common multiple
        """
        return a * b // gcd(a, b)

    def iter_lcm(*args: range) -> int:
        """
        Return least common multiple of args using functools.reduce
        
        :param *args: pointer to a range call

        :returns: integer
        """
        return reduce(lcm, args)

    return iter_lcm(*range(2, input_number))

 
def solution_3(input_number: int = 21) -> int:
    """
    Find smallest multiple evenly divisible by all numbers from 1 to the input number

    :param input_number: integer

    :returns: integer

    >>> solution_3(10)
    2520
    >>> solution_3()
    232792560
    """

    def gcd(a: int, b: int) -> int:
        """
        Return greatest common divisor according to Euclid's Algorithm using recursion
        
        :param a: integer
        :param b: integer

        :returns: greatest common divisor
        """
        while b > 0:
            a, b = b, a % b
        return a

    def lcm(a: int, b: int) -> int:
        """
        Return least common multiple.

        :param a: integer
        :param b: integer

        :returns: least common multiple
        """ 
        return a // gcd(a, b) * b
    
    def iter_lcm(input_number: int) -> int:
        """
        Return least common multiple between 2 and 20.

        :param input_number: integer

        :returns: integer
        """
        # Iteratively compute the lcm of more than two numbers
        prod = 1     
        for n in range(2, input_number):
            prod = lcm(n, prod)
        return prod
    
    return iter_lcm(input_number)


def main() -> True:
    """ 
    Solve problems with different algorithms and measure computation time for each
    
    :returns: True
    """
    print('-- solution_1: ', solution_1())
    print('-- solution_2: ', solution_2())
    print('-- solution_3: ', solution_3())
    
    n_retry = 50
    for function_name in ['solution_1', 'solution_2', 'solution_3']:
        meas_time = timeit.timeit(function_name + '()',
                                  setup='from __main__ import ' + function_name,
                                  number=n_retry)
        average_time = 1000 * meas_time / n_retry
        print(f"Average time of {function_name}: {round(average_time, 5)}ms")
    return True

#-------------------------------------------------------------


if __name__ == "__main__":
    print("\n*** DOCTEST ***")
    failure_count, test_count = doctest.testmod(verbose=False)
    assert failure_count == 0, 'Test failure... bailing out'
    print(f'All {test_count} tests passed')
    main() 