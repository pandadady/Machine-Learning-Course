#!/usr/bin/python
# -*- coding:  utf-8 -*
"""
This module is used to ....
Authors: shiduo(shiduo@baidu.com)
Date:2016-6-8
"""
#coding=utf-8
from math import log
import time

def createDataSet():
    trainpath='test.txt'
    ff = open(trainpath,'r')
    i=0
    dataSet=[]
    for line in ff:
        i+=1
        tmpline=line.strip()
        if tmpline=="":
            continue
        tags=tmpline.split()
        if i==1:
            labels=tags
        else:
            dataSet.append(tags)
    ff.close()
    return dataSet, labels

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for feaVec in dataSet:
        currentLabel = feaVec[-1]
        if currentLabel not in labelCounts:
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt

def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet
    
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy -newEntropy
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature
            
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    return max(classCount)         
    
def createTree(dataSet, labels):
    
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) ==len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, 
                                        bestFeat, value),subLabels)
    return myTree
    
def main():
    data,label = createDataSet()
    t1 = time.clock()
    myTree = createTree(data,label)
    t2 = time.clock()
    print myTree
    print 'execute for ',t2-t1
if __name__=='__main__':
    main()
        
