
def single_factors(number):
    '''
    Returns the product of the prime divisors of "number"
    (using each prime divisor only once).

    You can assume that "number" is an integer at least equal to 2.

    >>> single_factors(2)
    2
    >>> single_factors(4096)                 # 4096 == 2**12
    2
    >>> single_factors(85)                   # 85 == 5 * 17
    85
    >>> single_factors(10440125)             # 10440125 == 5**3 * 17**4
    85
    >>> single_factors(154)                  # 154 == 2 * 7 * 11
    154
    >>> single_factors(52399401037149926144) # 52399401037149926144 == 2**8 * 7**2 * 11**15
    154
    '''
    def factor(num):
        if num ==1:
            return []
        else:
            for i in range(2,num+1):
                n,d = divmod(num,i)
                if d ==0:
                    return [i]+factor(n)
    L = factor(number)
    dict = set(L)
   


    
    sum_1 = 1
    for i in dict:
        sum_1*=i





    return sum_1
    # REPLACE THE PREVIOUS LINE WITH YOUR CODE


if __name__ == '__main__':
    import doctest
    doctest.testmod()

