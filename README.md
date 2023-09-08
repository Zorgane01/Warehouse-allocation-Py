# Warehouse Location-Allocation Optimization

## Overview

The Warehouse Location-Allocation Optimization project addresses the crucial logistics and supply chain challenge of determining optimal warehouse locations and efficiently allocating customer demand while minimizing transportation costs. This project employs linear programming techniques and the PuLP library in Python to find an optimized solution.

here you'll find the code written using Spyder, it contains an explanation for each step

i included a document explaining in depth the theory behind this problem and the steps we followed to solve it

### Key Components

- **Input Data**: The project takes input data from an Excel file, including distances between cities and manually defined demand data.

   ![Distance Data](images/dist.jpg)

   **Table 1: Demand by City**
   
   | City    | Demand   |
   | ------- | -------- |
   | City 1  | 10,000   |
   | City 2  | 20,000   |
   | City 3  | 33,000   |
   | City 4  | 9,000    |
   | City 5  | 60,000   |
   | City 6  | 2,500    |
   | City 7  | 35,000   |

- **Decision Variables**:

   - *Flows*: Binary variables representing the flow of goods from warehouses to cities.
   - *New Warehouses*: Binary variables indicating whether a warehouse is selected for operation.

- **Objective Function**: Minimize the total transportation distance by optimizing the allocation of warehouses to cities while satisfying demand.


