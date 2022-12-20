import argparse
import math

import gmpy2
from gmpy2 import mpfr, mpq
from tqdm import tqdm, trange

from utils.funcs import zeta
from utils.time import timing
from utils.prec import set_dec_prec


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", type=int, default=4)
    parser.add_argument("--x_0", type=float, default=2.0)
    parser.add_argument("--y_0", type=float, default=2.0)
    parser.add_argument("--x", type=float, default=4.0)
    return parser.parse_args()

@timing
def diff_eq(x_0, y_0, N_divide, f):
    y = mpfr(y_0)
    for i in trange(N_divide):
        K_1 = f(y)
        K_2 = f(y + h * K_1)
        y += h * (K_1 + K_2) / 2
    return y

if __name__ == '__main__':
    args = get_args()
    
    x_0, y_0, x = args.x_0, args.y_0, args.x
    L = x - x_0
    
    # TODO: Precise extimation of hyper params
    N_divide, N_sum, D = 100, 1000, 10
    h = mpfr(L / N_divide)
    
    f = lambda x: zeta(x, N_sum)
    
    set_dec_prec(D)

    y, time = diff_eq(x_0, y_0, N_divide, f)    
    
    print(f"Target precision: {args.precision}")
    print(f"N_divide = {N_divide}, N_sum = {N_sum}, D = {D}")
    print(f"res = {y.digits()}")
    print(f"Time spent: {time} ms")
    