# Basic pproach
## Data input/output
The first step was to get the table from the word document into a format that python can read. For this test, the data was typed into a .csv file. If need be, a script can be written that converts the input data from the original format into a CSV.
## Using Pandas
I used the Pandas library to manipulate the data. It scales well to bigger data-sets and I have some experience using it.
## Getting something that works
The first step was to import the data and getting a way to output the assignments. After doing this, I spent some time to make some rules for assignment (like setting up a distance matrix and assigning the furthest two towers some frequencies and working from there), but after talking to some other engineers and doing some research, I decided to go with a more formal approach, namely defining an objective function and maximizing its output using some algorihm
# Objective Function
The objective function adds the distance between any 2 towers with the same frequencies, and assigns a bonus to any towers with unique frequencies. The function is typed out in latex and rendered in PDF. It's in the repo
# Greedy Algorithm
The greedy algorithm is the was chosen because it's the simplest to implement. It involves no iteration. It simply uses the objective function to test the options when assigning each frequency, and assigning the frequency that would increase the output of the objective function the most
