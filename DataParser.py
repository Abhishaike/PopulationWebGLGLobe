import pandas as pd
import numpy as np
import csv


FullData = pd.read_csv('/Users/abhishaikemahajan/Documents/Project/PopData.csv', skiprows=1)


FullData = FullData.ix[:,4:]

lat = FullData.ix[:,0]
lon = FullData.ix[:,1]
Data1950 = FullData.ix[:,2]/36400
Data1955 = FullData.ix[:,3]/36400
Data1960 = FullData.ix[:,4]/36400
Data1965 = FullData.ix[:,5]/36400
Data1970 = FullData.ix[:,6]/36400
Data1975 = FullData.ix[:,7]/36400
Data1980 = FullData.ix[:,8]/36400
Data1985 = FullData.ix[:,9]/36400
Data1990 = FullData.ix[:,10]/36400
Data1995 = FullData.ix[:,11]/36400
Data2000 = FullData.ix[:,12]/36400
Data2005 = FullData.ix[:,13]/36400
Data2010 = FullData.ix[:,14]/36400
Data2015 = FullData.ix[:,15]/36400
Data2020 = FullData.ix[:,16]/36400
Data2025 = FullData.ix[:,17]/36400
Data2050 = FullData.ix[:,18]/36400


f = open('NewData2.json', 'w')
print >>f, "var data = ["
print >>f, "["

for Date in Data1950, Data1955, Data1960, Data1965, Data1970, Data1975, Data1980, Data1985, Data1990, Data1995, Data2000, Data2005, Data2010, Data2015, Data2020, Data2025, Data2050:
	print >> f, "[",'"',Date.name, '"', ",", "["
	if (Date.name == 'Data2050'):
		for CountNumber in range(0, 590):
			if (CountNumber == 589):
				print >> f,lat[CountNumber],",",lon[CountNumber],",",Data2050[CountNumber], "]",
				print >> f, '\n'
				print >> f, "]"
			else:
				print >> f, lat[CountNumber],",",lon[CountNumber],",",Data2050[CountNumber],",",
	else:
		for CountNumber in range(0, 590):
			if (CountNumber == 589):
				print >> f, lat[CountNumber],",",lon[CountNumber],",",Date[CountNumber], "]"
				print >> f, '\n'
				print >> f, "],"
			else:
				print >> f, lat[CountNumber],",",lon[CountNumber],",",Date[CountNumber],",",
f.close()
print >> f, "];"



