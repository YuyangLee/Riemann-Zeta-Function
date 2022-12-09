import argparse
import math

import gmpy2
from gmpy2 import mpfr, mpq
from tqdm import tqdm, trange

from utils.zeta import zeta, zeta_prime


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", type=int, default=4)
    parser.add_argument("--a", type=float, default=1.5)
    return parser.parse_args()
    
if __name__ == '__main__':
    args = get_args()
    
    # TODO: Computation
    N_sum, N_iter = 10000, 100
    D = args.precision + math.ceil(math.log(N_sum))
    D = math.ceil(math.log2(10**D))
    gmpy2.get_context().precision = D
    
    a = args.a
    
    x = mpq(1 / a)
    for i in trange(N_iter):
        z = zeta(x, N_sum)
        z_p = zeta_prime(x, N_sum)
        x = x - (z - a) / z_p
    
    print(f"x_hat = {x.digits()}")
    