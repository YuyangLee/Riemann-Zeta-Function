import math

import gmpy2
import numpy as np
from gmpy2 import mpfr, mpq
from tqdm import tqdm, trange


def zeta_np(s, N):
    sum = np.zeros_like(s)
    for n in trange(1, N+1):
        sum += 1 / n**s
    return sum

def zeta(s, N, verbose=False):
    """
    Compute the Riemann zeta function at s, summation from n = 1 to n = N.
    """
    sum = mpfr(0)
    # for n in trange(1, N+1):
    n = 1
    while n <= N:
        sum = sum + mpfr(1 / n**s)
        if verbose and (n % 50 == 0):
            tqdm.write(f"step {n}\t sum = { mpfr(sum).digits() }\n")
        n += 1
    return sum

def zeta_prime(s, N, verbose=False):
    """
    Compute the derivative of the Riemann zeta function at s, summation from n = 1 to n = N.
    """
    sum = mpfr(0)
    # for n in trange(1, N+1):
    n = 2
    while n <= N:
        sum = sum + mpfr(math.log(n) / (n**s))
        if verbose and (n % 50 == 0):
            tqdm.write(f"step {n}\t sum = { mpfr(sum).digits() }\n")
        n += 1
    return - sum

def zeta_int(x, t):
    return (t**(x-1)) / (gmpy2.exp(t) - 1 + mpq(1, int(1e20)))

def zeta_int_np(x, t):
    return np.power(t, x-1) / (np.exp(t) - 1 + 1e-14)
