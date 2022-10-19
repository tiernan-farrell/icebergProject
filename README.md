# icebergProject

This project was created by group 5 in CSE 5242.
The goal of this project is to create a web interface 
where a user can choose between a set of iceberg cubing 
algorithms and examine the difference in execution time for 
different sets of data. 

##  Initial Setup 

Before the web interface is built and real data sets are 
found/created, the algorithms will be implemented and tested
using python generated data in the form of a .txt file. 
The data will be pre-processed and the algorithms will be
implemented using the processed data.

- Data Generation: 
        `dataGenerator.py` generates 10000 tuples of data where each
        tuples contains 5 random integers from 0-9. using the command 
        ```
        python3 dataGenerator.py > data.txt
        ```
        pipes the ouptut from the data generator into a usable text file 

## Algorithms
- BUC (Bottom Up Computation)
- Top-Down Computation 
- APRIORI
- H-Cubing
- Star-Cubing
- Multiway