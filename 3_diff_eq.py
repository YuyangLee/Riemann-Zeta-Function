import argparse
import math

import gmpy2
from gmpy2 import mpfr, mpq
from tqdm import tqdm, trange

from utils.zeta import zeta


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", type=int, default=4)
    parser.add_argument("--x_0", type=float, default=2.0)
    parser.add_argument("--y_0", type=float, default=2.0)
    parser.add_argument("--x", type=float, default=4.0)
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    
    x_0, y_0, x = args.x_0, args.y_0, args.x
    L = x - x_0
    
    # TODO: Computation
    N_divide, N_sum, D = 1000, 1000, 32
    h = mpfr(L / N_divide)
    
    f = lambda x: zeta(x, N_sum)
    
    gmpy2.get_context().precision = D
    
    y = mpfr(y_0)
    for i in trange(N_divide):
        # K_1 = f(x_0 + h * i)
        # K_2 = f(x_0 + h * i + h / 2)
        # y += h * (K_1 + K_2) / 2
        
        K_1 = f(x_0 + h * i)
        K_2 = f(x_0 + h * i + K_1 * h / 2)
        K_3 = f(x_0 + h * i + K_2 * h / 2)
        K_4 = f(x_0 + h * i + K_3 * h    )
        y += h * (K_1 + 2 * K_2 + 2 * K_3 + K_4) / 6
    
    print(f"integral = {float(y)}")
    print(f"integral = {y.digits()}")
    