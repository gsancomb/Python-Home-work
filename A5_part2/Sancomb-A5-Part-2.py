
# Griffin Sancomb
# CM25251

# Q6---------------
def is_prime(number):
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
             return False
    return True

is_prime(17)
# true
is_prime(16)
# false

primes = (x for x in range(2, 101) if(is_prime(x)))

print(primes)
# <generator object <genexpr> at 0x7fdbdde19200>

print(list(primes))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

#Q7--------------------
import math
# def factor_gen(n):
#     ''' generates the prime factors of the input number n '''
#     if (n <= 3):
#         raise Exception ("n should be a positive int greater than 3")
#     for x in range(2, n + 1):
#         if ((n % 1 == 0)):
#             factor = (x if (is_prime(x)))
#     return (factor)

def factor_gen(n):

    result = []
    if n <= 3:
        raise Exception("n should be a positive int greater than 3")

    while n % 2 == 0:
        (result.append(2))
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            (result.append(i))
            n = n / i

    if n > 2:
        (result.append(int(n)))

    yield result



factors_51 = factor_gen(51)
print(factors_51)
print(sorted(list(factors_51)))
# <generator object factor_gen at 0x7fdbde58e3c0>
# [3, 17]

factors_18000 = factor_gen(18000)
print(factors_18000)
print(sorted(list(factors_18000)))
# <generator object factor_gen at 0x7fdbde58ecf0>
# [2, 2, 2, 2, 3, 3, 5, 5, 5]

factors_16 = factor_gen(16)
print(factors_16)
print(sorted(list(factors_16)))
# <generator object factor_gen at 0x7fdbde60d040>
# [2, 2, 2, 2]

factors_625 = factor_gen(625)
print(factors_625)
print(sorted(list(factors_625)))
# <generator object factor_gen at 0x7fdbde60d3c0>
# [5, 5, 5, 5]

factors_753 = factor_gen(753)
print(factors_753)
print(sorted(list(factors_753)))
# <generator object factor_gen at 0x7fdbde60d740>
# [3, 251]

# #Q8--------------------
import random
A_high = 100
B_high = 89
C_high = 79
D_high = 69
F_high = 59

def random_gen(m, n):
    ''' generates m random integer numbers between 0 and n '''
    rand_list = []
    for i in range(0, m):
        rand_num = random.randint(0, n)
        print("Next random score is:", rand_num)
        rand_list.append( int(rand_num))
    yield rand_list


def converter_gen(scores):
    ''' converts the numeric scores to letter grades '''

    for x in scores:
        for i in range(len(x)):
            if x[i] > C_high:
                if x[i] > B_high:
                    yield('A')
                else:
                    yield('B')
            else:
                if x[i] > F_high:
                    if x[i] > D_high:
                        yield('C')
                    else:
                        yield('D')
                else:
                    yield('F')



random_grades = converter_gen(random_gen(3, 100))
print(random_grades)
print(list(random_grades))
# <generator object converter_gen at 0x7fdbde3d7f20>
# Next random score is: 77
# Next random score is: 98
# Next random score is: 11
# ['C', 'A', 'F']

random_grades = converter_gen(random_gen(5, 100))
print(random_grades)
print(list(random_grades))
# <generator object converter_gen at 0x7fdbdde19350>
# Next random score is: 80
# Next random score is: 58
# Next random score is: 35
# Next random score is: 83
# Next random score is: 94
# ['B', 'F', 'F', 'B', 'A']

