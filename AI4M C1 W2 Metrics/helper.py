# Import packages and libraries necessary for helper to work
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import ipywidgets as widgets
from fractions import Fraction

# basic default set ups
df = pd.read_csv('covid19.csv')
sns.set_style('darkgrid')
hue_colors = {'Sick': 'red',
              "Healthy": 'blue'}

# Plots graph functions
def plot():
    plot = widgets.interactive(f, slope=(-10.0, 10.0, 0.05), yIntercept=(0, 180, 10), xIntercept=(-100, 100, 10), degree=(-2, 4, 1), continuous_update=False, orientation='vertical')
    output = plot.children[-1]
    output.layout.height = '300px'
    return plot

def f(slope, yIntercept, xIntercept, degree):
    plt.figure()
    xPlot = np.linspace(-1000, 1000, num=10000)
    yPlot = slope * ((xPlot + xIntercept) ** degree) + yIntercept
    sns.scatterplot(x='Time_outside(hours/week)',
                y='population_density(hundreds_of_people/square_mile)',
                data=df,
                hue='labels',
                palette = hue_colors)
    plt.plot(xPlot, yPlot)
    
    if slope < 0:
        plt.fill_between(xPlot, -20, yPlot, facecolor='blue', alpha=0.3)
        plt.fill_between(xPlot, yPlot, 100, facecolor='red', alpha=0.3)
    else:
        plt.fill_between(xPlot, -20, yPlot, facecolor='red', alpha=0.3)
        plt.fill_between(xPlot, yPlot, 100, facecolor='blue', alpha=0.3)
    
    plt.ylim(-20, 100)
    plt.xlim(-20, 100)
    plt.xlabel('Time_outside_(hours)')
    plt.ylabel('%_time_wearing_mask_outside')
    plt.title('Covid-19 Dataset Distribution')
    
def challenge1Check(TP, TN, FP, FN, answer1, answer2, answer3, answer4, name):
    if TP == answer1:
        print("True Positives: " + str(TP) + " is correct!")
    else:
        print("True Positives: " + str(TP) + " is incorrect!")
    if TN == answer2:
        print("True Negatives: " + str(TN) + " is correct!")
    else:
        print("True Negatives: " + str(TN) + " is incorrect!")
    if FP == answer3:
        print("False Positives: " + str(FP) + " is correct!")
    else:
        print("False Positives: " + str(FP) + " is incorrect!")
    if FN == answer4:
        print("False Negatives: " + str(FN) + " is correct!")
    else:
        print("False Negatives: " + str(FN) + " is incorrect!")
        
    if(TP == answer1 and TN == answer2 and FP == answer3 and FN == answer4):
        print()
        print("Congratulations on completing " + name + "!")
    
# Answers to 1st challenge
def example1(TP, TN, FP, FN):
    challenge1Check(TP, TN, FP, FN, 48, 46, 4, 2, "Example 1")

def challenge1_1(TP, TN, FP, FN):
    challenge1Check(TP, TN, FP, FN, 50, 35, 15, 0, "Challenge 1.1")

def challenge1_2(TP, TN, FP, FN):
    challenge1Check(TP, TN, FP, FN, 46, 45, 5, 4, "Challenge 1.2")

def challenge1_3(TP, TN, FP, FN):
    challenge1Check(TP, TN, FP, FN, 47, 27, 23, 3, "Challenge 1.3")

def challenge1_4(TP, TN, FP, FN):
    challenge1Check(TP, TN, FP, FN, 34, 44, 6, 16, "Challenge 1.4")
    
# Answers to second Challenge
def challenge2Check(TP, TN, FP, FN, Sensitivity, Specificity, PPV, NPV, answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, name):
    correct = 0
    if TP == answer1:
        correct+=1
        print("True Positives: " + str(TP) + " is correct!")
    else:
        print("True Positives: " + str(TP) + " is incorrect!")
    if TN == answer2:
        correct+=1
        print("True Negatives: " + str(TN) + " is correct!")
    else:
        print("True Negatives: " + str(TN) + " is incorrect!")
    if FP == answer3:
        correct+=1
        print("False Positives: " + str(FP) + " is correct!")
    else:
        print("False Positives: " + str(FP) + " is incorrect!")
    if FN == answer4:
        correct+=1
        print("False Negatives: " + str(FN) + " is correct!")
    else:
        print("False Negatives: " + str(FN) + " is incorrect!")
    print()
    if Sensitivity == answer5:
        correct+=1
        print("Sensitivity: " + str(Sensitivity) + " is correct!")
    else:
        print("Sensitivity: " + str(Sensitivity) + " is incorrect!")
    if Specificity == answer6:
        correct+=1
        print("Specificity: " + str(Specificity) + " is correct!")
    else:
        print("Specificity: " + str(Specificity) + " is incorrect!")
    if PPV == answer7:
        correct+=1
        print("PPV: " + str(PPV) + " is correct!")
    else:
        print("PPV: " + str(PPV) + " is incorrect!")
    if NPV == answer8:
        correct+=1
        print("NPV: " + str(NPV) + " is correct!")
    else:
        print("NPV: " + str(NPV) + " is incorrect!")
    if(correct == 8):
        print()
        print("Congratulations on completing " + name + "!")

def example2(TP, TN, FP, FN, Sensitivity, Specificity, PPV, NPV):
    challenge2Check(TP, TN, FP, FN, Sensitivity, Specificity, PPV, NPV, 33, 15, 0, 2, Fraction(33, 35), Fraction(15, 15), Fraction(33, 33), Fraction(15, 17), "Example 2")

def challenge2_1(TP, TN, FP, FN, Sensitivity, Specificity, PPV, NPV):
    challenge2Check(TP, TN, FP, FN, Sensitivity, Specificity, PPV, NPV, 55, 145, 30, 20, Fraction(55, 75), Fraction(145, 175), Fraction(55, 85), Fraction(145, 165), "Challenge 2.1")
        
def challenge2_2(TP, TN, FP, FN, Sensitivity, Specificity, PPV, NPV):
    challenge2Check(TP, TN, FP, FN, Sensitivity, Specificity, PPV, NPV, 300, 200, 50, 100, Fraction(300, 400), Fraction(200, 250), Fraction(300, 350), Fraction(200, 300), "Challenge 2.2")