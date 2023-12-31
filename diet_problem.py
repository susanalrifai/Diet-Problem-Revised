# -*- coding: utf-8 -*-
"""Diet Problem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16KQEcsuAU1f6fnYbOHCYkC7fAhl9Ad45
"""

#!pip install pulp

#diet problem
# import pandas as pd
# import numpy as np

import pulp
lp = pulp.LpProblem("Diet_Problem_Revisted", pulp.LpMinimize)

#5 food items defined as variables, requirement to be positive, lowBound= 0

x1 = pulp.LpVariable (name= "Nonfat Greek Yogurt", lowBound=0)
x2 = pulp.LpVariable (name= "Tri colored Quinoa", lowBound= 0 )
x3 = pulp.LpVariable (name = "Spinach", lowBound= 0)
x4 = pulp.LpVariable (name = "Wild Caught Alaskan Salmon", lowBound = 0)
x5 = pulp.LpVariable (name = "Peanut Butter", lowBound = 0)

#Objective cost function to be minimized

lp += 0.71 * x1 + 0.34 * x2 + 0.57 * x3 + 3.74 * x4 + 0.22 * x5

#Constaints provided by FDA nutritional guidelines
lp += 50 * x1 + 0 * x2 + 65 * x3 + 85 * x4 + 140 * x5 <= 5000
lp += 100 * x1 + 170 * x2 + 25 * x3 + 150 * x4 + 190 * x5 >= 2000
lp += 17 * x1 + 6 * x2 + 2 * x3 + 25 * x4 + 7 * x5 >= 50
lp += 0 * x1 + 0 * x2 + 0 * x3 + 15.8 * x4 + 0 * x5 >= 20
lp += 210 * x1 + 21 * x2 + 80 * x3 + 10 * x4 + 17 * x5 >= 1300
lp += 0 * x1 + 2 * x2 + 2.3 * x3 + 0.5 * x4 + 0.5 * x5 >= 18
lp += 240 * x1 + 253 * x2 + 470 * x3 + 410 * x4 + 184 * x5 >=4700


# Solve the LP
solution = lp.solve()
print("Solution", solution)

#1 optimal, 2:not solved, 3: infeasible, 4:unbounded, 5:undefined

# Print Solution
for var in lp.variables():
  print(var, "=" , round(pulp.value(var), 2))

  print("OPT =", round(pulp.value(lp.objective), 2))

# Create and open a text file for writing
output_file_path = "diet_problem_output.txt"
with open(output_file_path, "w") as output_file:

    # Write the variable values to the file
    for var in lp.variables():
        output_file.write(f"{var} = {round(pulp.value(var), 2)}\n")

    # Write the objective value to the file
    output_file.write(f"OPT = {round(pulp.value(lp.objective), 2)}\n")

print(f"Results saved to {output_file_path}")

