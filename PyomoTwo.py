from pyomo.environ import *

m = ConcreteModel()

m.x = Var([1, 2, 3], domain=NonNegativeReals)

m.c1 = Constraint(expr=m.x[1] + m.x[2] + m.x[3] <= 1)
m.c2 = Constraint(expr=m.x[1] + 2 * m.x[2] >= 0.3)
m.OBJ = Objective(expr=m.x[3], sense=maximize)

solver = SolverFactory('ipopt')

solver.solve(m, tee=True)
