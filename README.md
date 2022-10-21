
# icebergProject

  

This project was created by group 5 in CSE 5242.

The goal of this project is to create a web interface

where a user can choose between a set of iceberg cubing

algorithms and examine the difference in execution time for

different sets of data.

  

## Initial Setup

  

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

  

# Algorithms

## BUC (Bottom Up Computation)

- Bottom up computation is a method in which the database is repeatedly sorted and partitioned and only values that meet the minimum support are kept. This starts at the "bottom" of the cube lattice and begins the sort only on the first attribute. Only the values for the first attribute that are above the min support level are partitioned. BUC then recursively calls itself reducing the input table to the partitioned table and increasing the starting dimension. BUC climbs up the lattice in this manner pruning out groups that don't meet minsup, then eventually comes back down to repeat on the next partition and so on. 

  

1. Sort database on attribute d=0

2. If an attribute value meets minsup, recursively call the buc algorithm with the dimension incremented and input table as only those tuples with the current value for current dimension.

3. If it does not meet minsup we prune it and dont add the counts to iceberg cube.

4. Recursion continues up the lattice and checks all combinations of attributes at each level to see if they are above minsup.

5. sort database on attribute d+1 and repeat until d=number of dimensions

  


<img width="458" alt="image" src="https://user-images.githubusercontent.com/63930496/197000331-6d14ecf9-54b7-4ba5-91b2-aadec6bb0bcd.png" width="800">
For this cube lattice, the processing tree of the buc algorithm looks like this:

<img width="458" alt="image" src="https://user-images.githubusercontent.com/63930496/197291959-e3b5ee17-c59c-49d8-abd0-84daad4979cd.png
" width="800">

Where the number next to the region in the lattice represents the order it is processed by BUC.

BUC climbs the lattice recursively then decends downward. Notice all of dimension A was processed before dimension B starts. 

  

## Top-Down Computation

## APRIORI

## H-Cubing

## Star-Cubing

## Multiway