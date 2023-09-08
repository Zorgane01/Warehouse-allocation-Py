# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8  2023

@author: ZORGANE Zakaria
"""
#step 1: importing the libraries we'll be working with

import pandas as pd
from pulp import *

#step 2: importing the excel file containing our data

data= pd.read_excel('warehouse_city.xlsx')
data= data.set_index('Warehouse')
demand= [10000, 20000, 33000, 9000, 60000, 2500, 35000] #since we don't have a file for the damand, we'll add it manually in a list

# List of warehouses and customers (cities)

warehouse = data.index
customers = data.columns

#step 3: Define keys for the decision variables and create a dictionary for distances

keys= [(w,c) for w in warehouse for c in customers]
distance_dict= { (w,c): data.loc[w,c] for w in warehouse for c in customers}

# we created a dictionary for customer(city) demands

demand_dict= dict(zip(customers, demand)) 

#step 4: Defining the decision variables

flows= LpVariable.dicts('flows', keys, cat= LpBinary)
new_w= LpVariable.dicts('new_w', warehouse, cat= LpBinary)

#step 5: Defining the objective function

model= LpProblem('warehouse_allocation', LpMinimize)

model+= lpSum([demand_dict[(c)]*flows[(w,c)]*distance_dict[(w,c)] for w in warehouse for c in customers])

#step 5: adding constraints
    """customer satisfaction constraint"""

for c in customers:
    model+= lpSum(flows[(w,c)] for w in warehouse) == 1

    """Number of warehouses constraint : 3 in our case"""

model+= lpSum(new_w[(w)] for w in warehouse)==3

    """warehouse assignement constraint"""

for w in warehouse:
    model+= new_w[(w)]>= flows[(w,'city 1')]
    model+= new_w[(w)]>= flows[(w,'city 2')]
    model+= new_w[(w)]>= flows[(w,'city 3')]
    model+= new_w[(w)]>= flows[(w,'city 4')]
    model+= new_w[(w)]>= flows[(w,'city 5')]
    model+= new_w[(w)]>= flows[(w,'city 6')]
    model+= new_w[(w)]>= flows[(w,'city 7')]

#step 6: solving the Optimization Model 

model.solve()

#step 7: check if an optimal solution was found and display its results

if LpStatus[model.status] == "Optimal":
    print("Optimal Solution Found")
    print("Objective Value (Total distance):", value(model.objective))

    # Display the selected warehouses
    selected_warehouses = [w for w in warehouse if new_w[(w)].varValue > 0]
    print("Selected Warehouses:", selected_warehouses)
    
    # Display the values of the flows
    for (w, c) in keys:
        if flows[(w, c)].varValue > 0:
            print(f"Flow from {w} to {c}: {flows[(w, c)].varValue}")
else:
    print("No Optimal Solution Found")
    
