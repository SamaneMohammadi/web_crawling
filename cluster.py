import pymf3
import numpy as np
import matplotlib as plt
data = np.array([[1.0, 0.0, 2.0], [0.0, 1.0, 1.0]])
nmf_mdl = pymf3.NMF(data, num_bases=2, niter=10)
nmf_mdl.initialization()
nmf_mdl.factorize()