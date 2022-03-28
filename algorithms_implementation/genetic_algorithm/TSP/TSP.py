import numpy as np

class Tsp_problem:

    def __init__(self, n_cities, dist_matrix):
        self.n_cities = n_cities
        self.dist_matrix = dist_matrix

    def create_random_instance(n):
        x = np.random.random(-5, 5, size = n)
        y = np.random.random(-5, 5, size = n)
        m = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                m[i,j] = np.sqrt((x[i] - x[j])**2+(y[i] - y[j])**2)

        return Tsp_problem(n,m)
    
    def objective_function(self, x):
        # x è la lista ordinata dei nodi visitati, eccetto l'ultimo vertice (che è anche il primo)
        # 1 2 0 4 5 3 1
        cost = 0
        for i in range(0, self.n_cities):
            c1 = x[i]
            c2 = x[i+1]
            cost = self.dist_matrix[c1, c2]
        
        # Costo per tornare al primo
        c1 = x[-1]
        c2 = x[0]
        cost+= self.dist_matrix[c1,c2]

        return cost
    
    def get_dim(self):
        return self.n_cities