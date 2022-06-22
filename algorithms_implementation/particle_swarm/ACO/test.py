from ACO import *
import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
print (os.getcwd())

pr = Tsp_problem.read_file("algorithms_implementation/particle_swarm/ACO/berlin52.tsp")

a = ACO_for_TSP(pr)

print(a.alpha)

a.run(500, 121)


