import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as rand
import seaborn as sns
from ipywidgets import *
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

value1 = 0
value2 = 0

def setValue1(value1):
    value1 = value1
    
def setValue2(value2):
    value2 = value2
    
def getValue1():
    return value1

def getValue2():
    return value2

def getTrainX(trainX):
    helperTrainX = trainX
    return helperTrainX

def inputData(value1, value2, breast_cancer):
    setValue1(value1)
    setValue2(value2)
    breast_cancer = datasets.load_breast_cancer()
    # just focusing on selected two dimensions 
    X = breast_cancer.data[:, [getValue1() - 1, getValue2() - 1]]
    Y = breast_cancer.target_names
    binClasses = breast_cancer.target
    return X, Y, binClasses

def showChallengeEx():
    exampleYScore = [5.32689544,  6.60995336,  -3.82163158, -0.64246504,  2.79210812]
    desiredArrayNums = [1, 1, 0, 0, 1]
    desiredArrayLabels = ['benign', 'benign', 'malignant', 'malignant', 'benign']
    print("Sample oiginal scores: " + str(exampleYScore))
    print("Desired classifications (binary) : " + str(desiredArrayNums))
    print("Desired classifications (labels) : " + str(desiredArrayLabels))
    return exampleYScore
    
def checkAnswerEx(threshold, exampleYScore):
    challenge1Nums = []
    challenge1Labels = []
    for num in exampleYScore:
        if num < threshold:
            challenge1Nums.append(0)
            challenge1Labels.append('malignant')
        else:
            challenge1Nums.append(1)
            challenge1Labels.append('benign')
            
    print("Threshold: " + str(threshold))
    print("Resulting classifications (binary) : ")
    print(challenge1Nums)
    print("Resulting classifications (labels) : ")
    print(challenge1Labels)
    print()
    if threshold <= -0.64246504  or threshold > 2.79210812:
        print("Incorrect, please try again")
    else:
        print("Congradulations on passing Example")
        
def showChallenge1_1():
    challenge1_1Score = [15.282729,  4.5895023,  0.0192348, -0.15332346,  1.1119684, -7.52491384, -0.0001879]
    desiredArrayNums = [1, 1, 1, 0, 1, 0, 1]
    desiredArrayLabels = ['benign', 'benign', 'benign', 'malignant', 'benign', 'malignant', 'benign']
    print("Sample oiginal scores: " + str(challenge1_1Score))
    print("Desired classifications (binary) : " + str(desiredArrayNums))
    print("Desired classifications (labels) : " + str(desiredArrayLabels))
    return challenge1_1Score
    
def checkAnswer1_1(threshold, challenge1_1Score):
    challenge1Nums = []
    challenge1Labels = []
    for num in challenge1_1Score:
        if num < threshold:
            challenge1Nums.append(0)
            challenge1Labels.append('malignant')
        else:
            challenge1Nums.append(1)
            challenge1Labels.append('benign')
            
    print("Threshold: " + str(threshold))
    print("Resulting classifications (binary) : ")
    print(challenge1Nums)
    print("Resulting classifications (labels) : ")
    print(challenge1Labels)
    print()
    if threshold <= -0.15332346  or threshold > -0.00001879:
        print("Incorrect, please try again")
    else:
        print("Congradulations on passing Challenge 1.1")
        
def showChallenge1_2():
    challenge1_2Score = [0.128975, 0.11111892,  -0.22474992, 2.18903579,  0.9875043, 1.542689, 6.16830486, 0.4478944, 0.55555555, -0.78923445]
    desiredArrayNums = [1, 0, 0, 1, 1, 1, 1, 1, 1, 0]
    desiredArrayLabels = ['benign', 'malignant', 'malignant', 'benign', 'benign', 'benign', 'benign', 'benign', 'benign', 'malignant']
    print("Sample oiginal scores: " + str(challenge1_2Score))
    print("Desired classifications (binary) : " + str(desiredArrayNums))
    print("Desired classifications (labels) : " + str(desiredArrayLabels))
    return challenge1_2Score
    
def checkAnswer1_2(threshold, challenge1_2Score):
    challenge1Nums = []
    challenge1Labels = []
    for num in challenge1_2Score:
        if num < threshold:
            challenge1Nums.append(0)
            challenge1Labels.append('malignant')
        else:
            challenge1Nums.append(1)
            challenge1Labels.append('benign')
            
    print("Threshold: " + str(threshold))
    print("Resulting classifications (binary) : ")
    print(challenge1Nums)
    print("Resulting classifications (labels) : ")
    print(challenge1Labels)
    print()
    if threshold <= -0.22474992  or threshold > 0.11111892:
        print("Incorrect, please try again")
    else:
        print("Congradulations on passing Challenge 1.2")
        
def showChallenge1_3():
    challenge1_3Score = [0.05, -0.1576825,  0.12, -1.7895432, -2.01413958, -1.9999578, -6.16830486, -1.9478944]
    desiredArrayNums = [1, 1, 1, 1, 0, 0, 0, 0]
    desiredArrayLabels = ['benign', 'benign', 'benign', 'benign', 'malignant', 'malignant', 'malignant', 'malignant']
    print("Sample oiginal scores: " + str(challenge1_3Score))
    print("Desired classifications (binary) : " + str(desiredArrayNums))
    print("Desired classifications (labels) : " + str(desiredArrayLabels))
    return challenge1_3Score
    
def checkAnswer1_3(threshold, challenge1_3Score):
    challenge1Nums = []
    challenge1Labels = []
    for num in challenge1_3Score:
        if num < threshold:
            challenge1Nums.append(0)
            challenge1Labels.append('malignant')
        else:
            challenge1Nums.append(1)
            challenge1Labels.append('benign')
            
    print("Threshold: " + str(threshold))
    print("Resulting classifications (binary) : ")
    print(challenge1Nums)
    print("Resulting classifications (labels) : ")
    print(challenge1Labels)
    print()
    if threshold <= -1.9478944  or threshold > -1.7895432:
        print("Incorrect, please try again")
    else:
        print("Congradulations on passing Challenge 1.3")

#def f(slope, yIntercept, xIntercept, degree, trainX):
    #trainX = getTrainX(trainX)
    #cushionX = (sum(trainX[getValue1()]) / trainX[getValue1()].size)
    #cushionY = (sum(trainX[getValue2()]) / trainX[getValue2()].size)
    #maxY = max(trainX[getValue2()])
    #maxX = max(trainX[getValue1()])
    #minY = min(trainX[getValue2()])
    #minX = min(trainX[getValue1()])
    
    #plt.figure()
    #xPlot = np.linspace(minX - cushionX, maxX + cushionX)
    #yPlot = slope * ((xPlot + xIntercept) ** degree) + yIntercept

    #sns.scatterplot(x="feature1",
                    #y="feature2",
                    #data=df,
                    #hue=trainY,
                    #palette=hue_colors)
    #if slope < 0:
        #plt.fill_between(xPlot, -20, yPlot, facecolor='blue', alpha=0.3)
        #plt.fill_between(xPlot, yPlot, 100, facecolor='red', alpha=0.3)
    #else:
        #plt.fill_between(xPlot, -20, yPlot, facecolor='red', alpha=0.3)
        #plt.fill_between(xPlot, yPlot, 100, facecolor='blue', alpha=0.3)
        
    #plt.plot(xPlot, yPlot)
    #plt.ylim(minY - cushionY, maxY + cushionY)
    #plt.xlim(minX - cushionX, maxX + cushionX)        