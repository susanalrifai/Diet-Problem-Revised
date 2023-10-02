# Diet-Problem-Revised
This python script solves the diet problem using linear programming methods with the puLP library. The diet problem revised atempts to find the optimal combination of five food items to meet the specific nutrional requirements set by the FDA while simaltaneously minimizing the cost.

# Installation
puLP library needs to be installed in order to run this program. It can be installed with pip:
!pip install pulp

# Usage
Open the script in preferred python environment
Run the script 
This script will produce optimal values for the food items chosen and the minimzed cost. It will also save the output results to a text file named 'diet_problem-output.txt' which can be altered based on preference

# Variables
There are 5 variables within this script
(x1) Nonfat Greek Yogurt
(x2) Tri Colored Quinoa
(x3) Spinach
(x4) Wild Caught Alaskan Salmon
(x5) Peanut Butter

# Objective Function
The objective is to minimize the cost: 
0.71 * x1 + 0.34 * x2 + 0.57 * x3 + 3.74 * x4 + 0.22 * x5

The objective function utilizes the cost per serving size of each food item in order to minimize the cost

# Constraints
The script consists of constraints that are based on FDA suggestions of nutrional guidelines to meet a healhty diet 
There are 7 nutritional constraints which are for: 
sodium <= 5000 mg
energy or calories >= 2000 kcal
protein >= 50 g
vitamin D >= 20 mcg
calcium >= 1300 mg
iron >= 18 mg
potassium >= 4700 mg

# Output 
The script prints the optimal values for each variable to minimize the cost. The results are also saved as a txt file



