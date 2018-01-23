# coding:utf-8 zxD
import math
import time
from igraph import *
import numpy as np
import pandas as pd

fl = pd.read_csv('jazz.txt', header=None, sep='\t')
edge_lst = []
weight_lst = []

for i in range(fl.shape[0]):
	for j in range(fl.shape[1]):
		if i < j and fl[i][j] != 0:
			edge_lst.append((i, j))
			weight_lst.append(fl[i][j])
g = Graph()
vn = fl.shape[0]
g.add_vertices(vn)
g.add_edges(edge_lst)
g.es['weight'] = weight_lst
for num in range(vn):
	g.vs[num]['name'] = num

ql = [0 for i in range(fl.shape[0])]
# print ql
# layout = g.gomory_hu_tree()
# clu = g.community_leading_eigenvector(weights=weight_lst)
# clu = g.community_infomap()
# clu = g.community_label_propagation(weights=weight_lst)
# clu = g.community_multilevel(weights=weight_lst)
# start = time.clock()
# clu = g.community_walktrap().as_clustering()
clu = g.community_fastgreedy().as_clustering()
# clu = g.community_edge_betweenness(weights=weight_lst).as_clustering()
# clu = g.community_optimal_modularity().as_cover()
# clu = g.community_spinglass().as_cover()
# finish = time.clock()

for q in range(len(clu.sizes())):
	for qq in clu[q]:
		ql[qq] = q
		# print ql[qq]

print ql
# 计算模块度值
print max(ql)
print g.modularity(ql)
# print finish-start
# plot(g)
