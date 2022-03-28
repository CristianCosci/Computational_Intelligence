from permutation_genetic_algorithm import *
from TSP import *

p1 = [0,2,3,5,1,6,4]
p2 = [2,5,1,4,3,0,6]

j1 = 2
j2 = 4

print(Permutation_genetic_algorithm.ordered_crossover(p1, p2, j1 , j2))

print(Permutation_genetic_algorithm.ordered_crossover(p2, p1, j1 , j2))