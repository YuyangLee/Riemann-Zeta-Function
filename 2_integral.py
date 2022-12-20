import argparse
import math

import gmpy2
from gmpy2 import mpfr, mpq
from tqdm import tqdm, trange

from utils.zeta import zeta, zeta_int
from utils.prec import set_dec_prec
from utils.time import timing

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", type=int, default=4)
    parser.add_argument("--x", type=float, default=3.5)
    parser.add_argument("--N_subdivide", type=float, default=3.5)
    return parser.parse_args()

def get_C(sub, sup):
    # TODO: Computation
    assert(sup == 1 or sup == 2)
    if sup == 1:
        return [mpq(1, 2), mpq(1, 2)][int(sub)]
    elif sup == 2:
        return [mpq(1, 6), mpq(4, 6), mpq(1, 6)][int(sub)]

@timing
def integral(f, N_divide, N_subdivide, X_max):
    
    l = mpfr(X_max / N_divide)
    h = l / N_subdivide
    
    I = mpfr(0)
    for n in trange(N_divide):
        sub_integral = mpfr(0)
        for i in range(N_subdivide + 1):
            sub_integral += get_C(i, N_subdivide) * zeta_int(x, l * n + h * i)
        I += l * sub_integral
        
    return I
    
if __name__ == '__main__':
    args = get_args()
    
    x = args.x
    N_subdivide = args.N_subdivide
    
    N_divide = 1000
    
    X_max = 4 * math.pow(10**(2 * args.precision) / 9, 1 / 3)
    D = args.precision + math.ceil(math.log10(2 * N_divide))

    set_dec_prec(D)
    
    I, time = integral(zeta_int, N_divide, N_subdivide, X_max)
    
    print(f"Target precision: {args.precision}")
    print(f"N_divide = {N_divide}, N_subdivide = {N_subdivide}, X_max = {X_max}, D = {D}")
    print(f"integral = {I.digits()}")
    print(f"Time spent: {time} ms")
    