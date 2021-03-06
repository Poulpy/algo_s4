#coding:utf-8

# ALGORITHMIQUE
# TP TRI TOPOLOGIQUE
# REPAIN Paul
# 2019

from graphes import *

def main():
    g0 = readGraph("dag0.txt")
    g0.pprint()
    toporder= g0.topological_ordering()
    print "TRI TOPOLOGIQUE NAIF :",toporder
    print "VERIFICATION :", g0.verify_topological_ordering(toporder)

    l1 = {'a':['b', 'c', 'e'], 'b':['e'], 'c':['b', 'e'], 'd':['b','e'], 'e':[]}
    g1 = Digraph(l1)
    g1.pprint()
    toporder= g1.topological_ordering()
    print "TRI TOPOLOGIQUE NAIF :",toporder
    print "VERIFICATION :", g1.verify_topological_ordering(toporder)

main()

