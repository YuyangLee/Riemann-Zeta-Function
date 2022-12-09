import argparse
import math

import gmpy2
from gmpy2 import mpfr, mpq
from tqdm import tqdm, trange

from utils.zeta import zeta, zeta_int


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", type=int, default=4)
    parser.add_argument("--x", type=float, default=3.5)
    return parser.parse_args()

def get_C(sub, sup):
    # TODO: Computation
    assert(sup == 2)
    return [mpq(1, 6), mpq(4, 6), mpq(1, 6)][int(sub)]
    
if __name__ == '__main__':
    args = get_args()
    
    x = args.x
    
    # TODO: Computation
    N_divide, N_subdivide, X_max, D = 100000, 2, 100.0, 32
    l = mpfr(X_max / N_divide)
    h = l / N_subdivide
    gmpy2.get_context().precision = D
    
    integral = mpfr(0)
    
    for n in trange(N_divide):
        sub_integral = mpfr(0)
        for i in range(N_subdivide + 1):
            sub_integral += get_C(i, N_subdivide) * zeta_int(x, l * n + h * i)
        integral += l * sub_integral
    
    print(f"integral = {float(integral)}")
    print(f"integral = {integral.digits()}")
    