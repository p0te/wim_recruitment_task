import pandas as pd
from math import *
def dist(x1,x2,y1,y2):
	return sqrt(pow((x1-x2),2) + pow((y1-y2),2) )
#read CSV into dataframe
dfin = pd.read_csv("input.csv")
columns = ["ID1","ID2","Distance"]
dfout = pd.DataFrame( columns = columns)
#generate distance matrix
for row in dfin.iterrows():
	for col in dfin.iterrows():
                thedist = dist(row[1]["Northing"],col[1]["Northing"],row[1]["Easting"],col[1]["Easting"])
                dfout = dfout.append({'ID1':row[1]['ID'],'ID2':col[1]['ID'],'Distance':thedist},ignore_index=True)
dfout = dfout.sort_values(by=['Distance'])
print(dfout)
	
