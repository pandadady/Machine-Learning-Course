#!/usr/bin/python
# -*- coding:  utf-8 -*
import itertools
"""
This module is used to learn apriori algorithm
Authors: shiduo(shiduo@baidu.com)
Date:2016-7-5
"""
def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]
def createC1(dataSet):
    C1 = []
    maxlen=0
    for transaction in dataSet:
        transactionlen=len(transaction)
        if transactionlen>maxlen:
            maxlen=transactionlen
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
                
    C1.sort()
    return map(frozenset,C1),maxlen
def calc_support(dataSet,C1,minSupport=0.5):
    dscnt={}
    for item in C1:
        for i in range(len(dataSet)):
            if item.issubset(dataSet[i]):
                if not dscnt.has_key(item):
                    dscnt[item]=0
                dscnt[item]+=1
    total=len(dataSet)
    retList=[]
    supportData={}
    for key in dscnt:
        support=dscnt[key]*1.0/total
        if support >= minSupport:
            retList.insert(0,key)
        supportData[key] = support
    return retList,supportData
def frequent_set(dataSet,minSupport):
    C1,maxlen=createC1(dataSet)
    retList,supportData=calc_support(dataSet,C1,minSupport)
    C2=[list(x)[0] for x in retList]
    L=[retList]
    for i in range(2,maxlen+1):
        iterilist=list(itertools.combinations(C2,i))
        iterilist=map(frozenset,iterilist)
        iterretList,itersupportData=calc_support(dataSet,iterilist,minSupport)
        supportData.update(itersupportData)
        L.append(iterretList)
    return L,supportData
def generateRules(L, supportData, minConf=0.7):  #supportData is a dict coming from scanD
    bigRuleList = []
    for i in range(1, len(L)):#only get the sets with two or more items
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            C2=[list(x)[0] for x in H1]
            maxlen=len(C2)
            for i in range(1,maxlen):
                iterilist=list(itertools.combinations(C2,i))
                iterilist=map(frozenset,iterilist)
                for item in iterilist:
                    conf=supportData[freqSet]/supportData[item]
                    if conf > minConf:
                        print item,"--->",freqSet,"conf:",conf
if __name__ == '__main__':
#     print list(itertools.permutations(plist,2))
#     print list(itertools.combinations(plist,2))
    L,supportData=frequent_set(loadDataSet(),minSupport=0.5)
    print supportData
    generateRules(L, supportData, minConf=0.7)
