# -*- coding: utf-8 -*- 
"""
Created on Mon Sep  5 07:56:33 2022

@author: Chris Irizarry
"""

# Course: Introduction to Programming (INFO-233)
# Student Name: 

# Instructions: All of your work needs to be supported by code. For every
# problem, type your code in the appropriate location. This file can be directly
# executed by the Python interpreter, and therefore this file is what you will
# submit.

################################
# Problem 1: Lists
################################

# Build a list (called myList) that contains every year from 2015 to 2022. Write
# the code to verify whether index 1 is (or is not) a leap year. Also verify
# whether the last index of myList is a leap year.
# (Hint: leap years are evenly-divisible by 4)

# Your Code Here
#Variables
myList = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
a = myList[1]%4
b = myList[-1]%4
#If statements
if (a) < 1:
    print((myList[1], "is a leap year"))
if (b) > 0:
    print((myList[-1], "is not a leap year"))

    
########################
# Problem 2: Sets
########################

# Using the two sets below, divBy2 and divBy3, determine which values occur in
# both sets and assign that to a variable called common. Then confirm whether
# common is in fact a subset of both divBy2 and divBy3.

divBy2 = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30}
divBy3 = {0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30}

common = # Your Code Here
#Variables
divBy2 = {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30}
divBy3 = {0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
#Variables/methods used
a = (divBy2.union(divBy3))
common = (divBy2.intersection(divBy3))
b = (common.issubset(a))
#Prints if is true or false of a subset of both divBy2 and divBy3.
print(b)








## Complete your coding and submit a copy of this file saved as  FA2022-INFO233-01-Homework3-Your_Last_Name 