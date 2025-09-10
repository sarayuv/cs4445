from problem1 import *
import sys
import math
import importlib.metadata 
import pandas as pd
'''
    Unit test 1:
    This file includes unit tests for problem1.py.
'''

#-------------------------------------------------------------------------
def test_python_environment():
    ''' ----------- Problem 1 (15 points in total)---------------------'''
    assert sys.version_info[0]==3 # require python 3.11 or above 
    assert sys.version_info[1]>=11
    installed_pkg = {pkg.name.lower() for pkg in importlib.metadata.distributions()}
    assert len(set(['pytest', 'mypy', 'numpy', 'flask', 'pandas', 'pandas-stubs']) - installed_pkg) ==0 # Check if any required package is missing. If missing, please follow the instructions at the begining of problem1.py to install the packages

#---------------------------------------------------
def test_load_webpages():
    ''' (5 points) load_webpages'''
    X = load_webpages("data_thanksgiving.csv") 
    assert type(X) == pd.DataFrame
    assert X.shape == (8, 4)
    assert X.iloc[3].ID== 3 
    assert X.iloc[0].URL == "0.html" 
    assert X.iloc[1].Title == "The Bob Chef" 
    assert X.iloc[-1].Description == "I learnt this recipe from Derek" 
#---------------------------------------------------
def test_count_word_frequency():
    ''' (5 points) count_word_frequency'''
    X = load_webpages("data_thanksgiving.csv") 
    X = count_word_frequency(X,"thanksgiving")
    assert X.shape == (8, 5)
    assert X.iloc[0].Count== 1 
    assert X.iloc[1].Count== 1 
    assert X.iloc[2].Count== 1 
    assert X.iloc[5].Count== 16 
    assert X.iloc[6].Count== 3 
    assert X.iloc[7].Count== 0 
    # Now lets save the result into a CSV file, for further analysis
    X.to_csv("data_X1.csv", index=False)
#---------------------------------------------------
def test_rank_word_frequency():
    ''' (5 points) rank_word_frequency'''
    X1 = pd.read_csv('data_X1.csv')
    R = rank_word_frequency(X1)
    assert R.iloc[0].ID == 5
    assert R.iloc[0].Count == 16
    assert R.iloc[1].ID == 6
    assert R.iloc[1].Count == 3
    # Now lets save the result into a CSV file, for your review
    R.to_csv("data_R1.csv", index=False)

