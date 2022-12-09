import argparse
import math

import gmpy2
from gmpy2 import mpfr, mpq

from utils.zeta import zeta


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", type=int, default=20)
    parser.add_argument("--zeta2", action='store_true')
    return parser.parse_args()
    
if __name__ == '__main__':
    args = get_args()
    
    
    if args.zeta2:
        s = 2
        N = math.ceil(2 * (10**args.precision))
        D = args.precision + math.ceil(math.log(N))
    else:
        s = 8
        N = math.ceil(math.pow(2, 1./7.) * math.pow(10, args.precision / 7))
        D = args.precision + 1
    
    D = math.floor(math.log2(10**D))
    gmpy2.get_context().precision = D
    sum = zeta(s, N, verbose=True)
    sum = mpfr(sum)
    
    pi = gmpy2.root(sum * 9450, 8)
    
    print(f"pi = {pi.digits()}")
    