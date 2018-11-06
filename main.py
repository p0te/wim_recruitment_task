import pandas as pd
from math import *
def dist(x1,x2,y1,y2):
	return sqrt(pow((x1-x2),2) + pow((y1-y2),2) )
#read CSV into dataframe
dfin = pd.read_csv("input.csv")
dfin['freq'] =0
print(dfin)
columns = ["ID1","ID2","Distance"]
dfout = pd.DataFrame( columns = columns)
freqs = [110,111,112,113,114,115]

def objective_func(df):
    out = 0
    for freq in freqs:
        if not df.isin([freq]).any(axis=None):
            out = out +1600
        for row in df.iterrows():
            for col in df.iterrows():
                if row[1]['freq'] == freq:
                    if col[1]['freq'] == freq:
                        out = out + dist(row[1]["Northing"],col[1]["Northing"],row[1]["Easting"],col[1]["Easting"])
    return(out)

#print("object:" + str(objective_func()))
for index, row in dfin.iterrows():
    max = 0
    setfreq = 0
    for freq in freqs:
        dftest = dfin 
        dftest.set_value(index,'freq',setfreq)
        obj = objective_func(dftest)
        if obj >= max:
            print(obj)
            max = obj
            setfreq = freq
    dfin.set_value(index,'freq',setfreq)


print(dfin)
