#!/usr/bin/python
# -*- coding:  utf-8 -*
"""
This module is used to learn linear regression algorithm
Authors: shiduo(shiduo@baidu.com)
Date:2016-6-12
"""
from numpy import *
import matplotlib.pyplot as plt
def loadDataSet(fileName):     
    numFeat = len(open(fileName).readline().split('\t')) - 1 
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat

def standRegres(xArr,yArr):
"""
    function:
        least square method
"""
    xMat = mat(xArr); yMat = mat(yArr).T
    xTx = xMat.T*xMat
    if linalg.det(xTx) == 0.0:
        print "This matrix cannot be inversed"
        return
    ws = xTx.I * (xMat.T*yMat)
    return ws
def make_plot(xArr,yArr,xCopy,yHat):
    xMat=mat(xArr)
    yMat=mat(yArr)
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.scatter(xMat[:,1].flatten().A[0],yMat.T[:,0].flatten().A[0])
    ax.plot(xCopy[:,1],yHat,color="red")
    plt.show()
def lwlr(testPoint,xArr,yArr,k=1.0):
"""
    function:
        Weighted least square method
"""
    xMat = mat(xArr); yMat = mat(yArr).T
    m = shape(xMat)[0]
    weights = mat(eye((m)))
    for j in range(m):                      #next 2 lines create weights matrix
        diffMat = testPoint - xMat[j,:]    #
        weights[j,j] = exp(diffMat*diffMat.T/(-2.0*k**2))
    xTx = xMat.T * (weights * xMat)
    if linalg.det(xTx) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = xTx.I * (xMat.T * (weights * yMat))
    return testPoint * ws

def lwlrTestPlot(xArr,yArr,k=1.0):  
    yHat = zeros(shape(yArr))       
    xCopy = mat(xArr)
    xCopy.sort(0)
    for i in range(shape(xArr)[0]):
        yHat[i] = lwlr(xCopy[i],xArr,yArr,k)
    return yHat,xCopy
def rssError(yArr,yHatArr): #yArr and yHatArr both need to be arrays
    return ((yArr-yHatArr)**2).sum()


if __name__ == '__main__':
    fileName="./test.txt"
    dataMat,labelMat=loadDataSet(fileName)
    ws=standRegres(dataMat,labelMat)
    xMat=mat(dataMat)
    xCopy=xMat.copy()
    xCopy.sort(0)
    yHat=xCopy*ws
    make_plot(dataMat,labelMat,xCopy,yHat)
    yHat,xCopy=lwlrTestPlot(dataMat,labelMat,k=0.01)
    make_plot(dataMat,labelMat,xCopy,yHat)
