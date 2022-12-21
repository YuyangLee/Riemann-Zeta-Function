import argparse
import math

import gmpy2
from gmpy2 import mpfr, mpq
from tqdm import tqdm, trange

from utils.funcs import zeta, gamma_int
from utils.prec import set_dec_prec
from utils.time import timing

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", type=int, default=4)
    parser.add_argument("--x", type=float, default=3.5)
    parser.add_argument("--N_subdivide", type=int, default=1)
    return parser.parse_args()

def get_C(sub, sup):
    # TODO: Computation
    assert(sup == 1 or sup == 2)
    if sup == 1:
        return [mpq(1, 2), mpq(1, 2)][int(sub)]
    elif sup == 2:
        return [mpq(1, 6), mpq(4, 6), mpq(1, 6)][int(sub)]

@timing
def zeta_gamma(x, N_sum, N_divide, N_subdivide, X_max):
    zeta_x = zeta(x, N_sum, verbose=False)
    f = lambda z: gamma_int(x, z)
    gamma_x = integral(f, N_divide, N_subdivide, X_max)
    
    return zeta_x * gamma_x

def integral(f, N_divide, N_subdivide, X_max):
    l = mpfr(X_max / N_divide)
    h = l / N_subdivide
    
    I = mpfr(0)
    for n in trange(N_divide):
        sub_integral = mpfr(0)
        for i in range(N_subdivide + 1):
            sub_integral += get_C(i, N_subdivide) * f(l * n + h * i)
        I += l * sub_integral
        
    return I

if __name__ == '__main__':
    args = get_args()
    
    x = args.x
    N_subdivide = args.N_subdivide
    
    X_max = math.log(15 * 10**args.precision / 2, 2)
    N_sum = math.ceil(math.pow(12 * 10**args.precision / 5, 2 / 5))
    N_divide = math.ceil(math.sqrt(X_max**3 * 10**args.precision / 2))
    D = args.precision + math.ceil(math.log10(max(6 * N_sum, 3 * N_divide)))
    
    X_max = 4 * math.pow(10**(2 * args.precision) / 9, 1 / 3)
    D = args.precision + math.ceil(math.log10(2 * N_divide))

    set_dec_prec(D)
    
    I, time = zeta_gamma(x, N_sum, N_divide, N_subdivide, X_max)
    
    print(f"Target precision: {args.precision}")
    print(f"N_sum = {N_sum}, N_divide = {N_divide}, N_subdivide = {N_subdivide}, X_max = {X_max}, D = {D}")
    print(f"integral = {('{0:.' + str(args.precision) + 'f}').format(I)}")
    print(f"Time spent: {time} ms")
    