import pandas as pd
from math import *
def dist(x1,x2,y1,y2):
	return sqrt(pow((x1-x2),2) + pow((y1-y2),2) )
#read CSV into dataframe
dfin = pd.read_csv("input.csv")
#generate distance matrix
for row in dfin.iterrows():
	for col in dfin.iterrows():
		print(dist(row[1]["Northing"],col[1]["Northing"],row[1]["Easting"],col[1]["Easting"]))
	
