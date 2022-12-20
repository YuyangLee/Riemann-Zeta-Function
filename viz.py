import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from utils.funcs import zeta_np, zeta_int_np

sns.set()

plt.figure()
xx = np.linspace(0.5, 10, 1000)
yy = zeta_np(xx, 10000)

plt.plot(xx, yy)
plt.savefig("assets/zeta.pdf")

plt.figure()
xx = np.linspace(0, 25, 1000)
yy = zeta_int_np(3.5, xx)

plt.plot(xx, yy)
plt.savefig("assets/zeta_int.pdf")
