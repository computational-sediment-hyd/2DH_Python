import numpy as np
from numba import jit

def z0(fn,gxn,gyn,nx,ny):

#     fn = np.zeros([nx+2, ny+2])
#     gxn = np.zeros([nx+2, ny+2])
#     gyn = np.zeros([nx+2, ny+2])

    fn[:,:] = float(0) 
    gxn[:,:] = float(0)
    gyn[:,:] = float(0)
    
    return fn, gxn, gyn
