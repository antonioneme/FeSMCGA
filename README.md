FeSMCGA
=======

Feature selection by maximization of a clustering coefficient guided by genetic algorithms

This program implements a feature selection algorithm.
Developed by Antonio Neme as part of his postdoctoral stay at 
Aittokallio's Group.
FIMM. Finland

How to run the program:

python FeSMCGA.py dats.dat K ps epochs pm dats.LAB output_1.fs dats.vars output_1.1K alfa D

where

dats.dat: is a text file, delimited by spaces. Each row is a vector and each column is an attribute. The last column
is the class of the vector, in an integer format. (see the file example.dat)

K is the maximum dimension of the subspace to be found (the maximum number of selected features)

ps is the population size (number of solutions)

epochs is the numbe rof generations (epochs) the genetic algorithm will run

pm is the probability of mutation

dats.LAB is a label for each of the objects

output_1.fs is the file containing the selected attributes.

dats.vars is the description of the attributes in the original space (one line per variable)

output_1.1K is the C value (clustering coefficient) for each attribute measured independently

alfa is the parameter to weight the C clustering coefficient

D is the kind of diameter to be considered.


python FeSMCGA.py example1.dat 3 50 100 0.05 example1.LAB example1_1.fs example1.vars example_1.1K 0.5 1
