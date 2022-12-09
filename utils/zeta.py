import gmpy2
from tqdm import tqdm, trange
from gmpy2 import mpfr, mpq

def zeta(s, N, verbose=False):
    """
    Compute the Riemann zeta function at s, summation from n = 1 to n = N.
    """
    sum = mpq(0, 1)
    
    for n in trange(1, N+1):
    # n = 1
    # while n <= N:
        sum = sum + mpq(1, n**s)
        if verbose and (n % 50 == 0):
            tqdm.write(f"step {n}\t sum = { mpfr(sum).digits() }\n")
        # n += 1
            
    return sum
