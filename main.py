import pandas as pd
from math import *
def dist(x1,x2,y1,y2):
	return sqrt(pow((x1-x2),2) + pow((y1-y2),2) )
#read CSV into dataframe
dfin = pd.read_csv("input.csv")
dfin['freq'] =0
columns = ["ID1","ID2","Distance"]
freqs = [110,111,112,113,114,115]
#Objective Function
def objective_func(df):
    out = 0
    for freq in freqs:
        if not df.isin([freq]).any(axis=None):
            out = out +1600 #bonus assigned to towers with unique freqs, arbitrarily chose a volue bigger than the biggest distance
        for index,row in df.iterrows():
            for index,col in df.iterrows():
                if row['freq'] == freq:
                    if col['freq'] == freq:
                        out = out + dist(row["Northing"],col["Northing"],row["Easting"],col["Easting"])
    return(out)

for index, row in dfin.iterrows():
    max = 0
    setfreq = 0
    for frequency in freqs:
        dftest = dfin #create a test dataframe to check options w.r.t objective function
        dftest.set_value(index,'freq',frequency)
        print(dfin)
        obj = objective_func(dftest)
        if obj >= max:
            print(obj)
            max = obj
            setfreq = frequency #this frequency will increase the objective function the most
    dfin.set_value(index,'freq',setfreq)


print(dfin)
