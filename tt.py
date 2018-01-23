import numpy as np
import pandas as pd

fl = pd.read_csv('jazz.txt', header=None, sep='\t')

for ff in range(fl.shape[0]):
	for gg in range(fl.shape[0]):
		if ff < gg and fl[ff][gg]:
			print(ff, gg, fl[ff][gg], "Undirected")


