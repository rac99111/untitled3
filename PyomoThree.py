from pylab import *

import shutil
import sys
import os.path

from pyomo.environ import *

model = ConcreteModel()

# declare decision variables
model.x = Var(domain=NonNegativeReals)

# declare objective
model.profit = Objective(
    expr=40*model.x,
    sense=maximize)

# declare constraints
model.demand = Constraint(expr=model.x <= 40)
model.laborA = Constraint(expr=model.x <= 80)
model.laborB = Constraint(expr=2*model.x <= 100)

# solve
SolverFactory('glpk').solve(model).write()