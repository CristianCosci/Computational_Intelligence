import numpy as np
from NPP import *

# local search algorithm for a binary problem
# FIRST IMPROVEMENT
def local_search(prob, init_sol=None, verbose= False):
    n = prob.get_dim()
    if init_sol is None:
        x = np.random.randint(0, 1+1, n)
    else:
        x = init_sol.copy()
    
    improved = True
    fx = prob.objective_function(x)
    if verbose:
        print('Initial value {}'.format(fx))
    while improved:
        best_f = fx
        ordering = list(range(0,n))
        np.random.shuffle(ordering)
        for i in ordering:
            x[i] = 1-x[i]
            fy = prob.objective_function(x)
            if fy < best_f:
                y = x.copy()
                best_f = fy
                x[i] = 1-x[i]
                break
        
            x[i] = 1-x[i]
        if best_f < fx:
            fx = best_f
            x = y
            improved = True
            if verbose:
                print("New value {}".format(fx))
        else:
            improved = False
    return x, fx 
