import argparse
import math

import gmpy2
from gmpy2 import mpfr, mpq
from tqdm import tqdm, trange

from utils.zeta import zeta, zeta_prime
from utils.prec import set_dec_prec
from utils.time import timing

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", type=int, default=4)
    parser.add_argument("--a", type=float, default=1.5)
    parser.add_argument("--x_0", type=float, default=2.5)
    return parser.parse_args()
    
@timing
def root_newton(a, x_0, N_iter, N_sum):
    x = mpfr(x_0)
    for i in trange(N_iter):
        z = zeta(x, N_sum)
        z_p = zeta_prime(x, N_sum)
        x = x - (z - a) / z_p
        
    return x
    
if __name__ == '__main__':
    args = get_args()
    
    N_iter = math.ceil(math.log2(math.log(1/4**args.precision, 1.99/2.)))
    N_sum = 4 * N_iter * 10**args.precision
    
    # A better estimation:
    # N_iter, N_sum = 16, 8000
    
    D = args.precision + math.ceil(math.log10((4 * N_sum**2 + 3 * N_sum) / 3))
    set_dec_prec(D)
    
    a, x_0 = args.a, args.x_0
    
    x, time = root_newton(a, x_0, N_iter, N_sum)
    
    print(f"Target precision: {args.precision}")
    print(f"N_iter = {N_iter}, N_sum = {N_sum}, D = {D}")
    print(f"x_hat = {x.digits()}")
    print(f"Time spent: {time} ms")
    