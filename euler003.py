import doctest
import timeit

"""
Problem 3: https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


# Trial division
def trial_division(n: int) -> list:
    """
    Generate a list of primes and iterate over it to find the largest prime 
    that is a factor of n

    :param n: integer greater than or equal to 2

    :returns: integer
    
    >>> trial_division(2*2*2*5*7)
    7
    """
    prime_factors = []                  # Prepare an empty list.

    while n % 2 == 0:                   # Check if n is even to remove multiples of 2.
        prime_factors.append(2)         # Append 2 to the list every time 
        n //= 2                         # Divide n by 2
    i = 3                               # The first possible factor.
    while i * i <= n:                   # Only check factors up to sqrt(n).
        if n % i == 0:                  # Check if remainder of n divided by i is 0.
            prime_factors.append(i)     # If so, it divides n. Add i to the list.
            n //= i                     # Divide that factor out of n.
        else:                           # If i is not a factor of n,
            i += 2                      # Add 2 to i and try again.
    if n != 1: prime_factors.append(n)  # Only an odd number is possible.
    
    return max(prime_factors)           # Return list of prime factors.


# Trial division 2
def trial_division2(n: int) -> int:
    """
    Return the largest prime factor of the input value 
    
    Iterate over every number from 2 up to n, and remove each factor from n. 
    Return the largest prime factor.

    :param n: integer greater than or equal to 2

    :returns: largest prime factor of n
    
    >>> trial_division2(2*2*2*3*3*5)
    5
    """
    i = 2                           # The first possible prime factor.
    
    while i * i < n:                # Only check factors up to sqrt(n).
        while n % i == 0:           # Check if remainder of n divided by i is 0.
            n //= i                 # If so, divide that factor out of n
        i += 1                      # If i is not a factor of n add one to i and repeat
    return n                        # Return largest prime 
    

def main() -> True:
    """ 
    Solve problems with different algorithms and measure computation time for each
    
    :return: True
    """
    
    n_retry = 5
    print('-- trial_division: ', trial_division(600851475143))
    print('-- trial_division2: ', trial_division2(600851475143))


    for function_name in ['trial_division', 'trial_division2']:
        meas_time = timeit.timeit(function_name + '(600851475143)',
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