import gmpy2
import math

def set_dec_prec(D):
    D = math.ceil(math.log2(10**D))
    gmpy2.get_context().precision = D
    
def float_str(base, exp, digits):
    # TODO: Fix
    res = float(base) * math.pow(10, -exp)
    res = round(res, digits)
    return eval(f"{res:.{digits}f}")
