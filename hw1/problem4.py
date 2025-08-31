




#------------ No New Package --------------
# NOTE: Please don't import any new package. You should be able to solve the problems using only the package(s) imported here.
import pandas as pd
#---------------------------------------------------------


# ---------------------------------------------------------
'''
    Goal of Problem 4: (Moneyball) Player Ranking for Oakland A's Baseball Team (OAK) in year 2002 (27 points)
    In this problem, you will rank baseball players for Oakland A's using different methods.
    A list of all variables being used in this problem is provided at the end of this file. 
'''
# ---------------------------------------------------------

''' ---------Function: compute_players_BA (4 points)--------------------
    Goal: (Compute Players' Batting Average) Given a dataframe (X6) of all the candidate players, compute the Batting Average (BA) of each player and insert a new column named 'BA' to store the data. 
    ---- Inputs: --------
    * X6: (Type: pd.DataFrame), a dataframe containing all the candidate players for evaluation in the year (2001), who have sufficient experience (at least min_AB) and affordable price tag (at most max_salary).
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_players_BA(X6:pd.DataFrame)->None:
    #########################################
    ## INSERT YOUR CODE HERE (4 points)
    X6['BA'] = X6['H'] / X6['AB']
    pass 
    #########################################
'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_4.py::test_compute_players_BA
        (Mac /Linux): python3 -m pytest -v test_4.py::test_compute_players_BA
---------------------------------------------------------------'''



''' ---------Function: rank_players_BA (3 points)--------------------
    Goal: If you have passed the previous test case, the result data frame should have been saved into a file, called 'moneyball_X7.csv'.  Now let's rank all of these players using the traditional metric: Batting Average. 
(Rank Players by BA) Given a dataframe (X7) of all the candidate players, rank all the players based upon descending order of Batting Average (BA). 
 If you have solved this problem and passed the test case, the result data frame will be saved into a file, called 'moneyball_R1.csv'. You could take a look at the ranking results of the players. 
    ---- Inputs: --------
    * X7: (Type: pd.DataFrame), a dataframe containing all the candidate players info, including Batting Average (BA).
    ---- Outputs: --------
    * R1: (Type: pd.DataFrame), a dataframe containing candidate players ranked by descending order of Batting Average (BA).
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def rank_players_BA(X7:pd.DataFrame)->pd.DataFrame:
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    R1 = X7.sort_values(by='BA', ascending=False).reset_index(drop=True)
    #########################################
    return R1

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_4.py::test_rank_players_BA
        (Mac /Linux): python3 -m pytest -v test_4.py::test_rank_players_BA
---------------------------------------------------------------'''



''' ---------Function: compute_players_OBP (4 points)--------------------
    Goal: (Compute Players' On-Base Percentage) Given a dataframe (X7) of all the candidate players, compute the (OBP) of each player and insert a new column named 'OBP' to store the data. 
    ---- Inputs: --------
    * X7: (Type: pd.DataFrame), a dataframe containing all the candidate players info, including Batting Average (BA).
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_players_OBP(X7:pd.DataFrame)->None:
    #########################################
    ## INSERT YOUR CODE HERE (4 points)
    X7['OBP'] = (X7['H'] + X7['BB'] + X7['HBP']) / (X7['AB'] + X7['BB'] + X7['HBP'] + X7['SF'])
    pass
    #########################################
'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_4.py::test_compute_players_OBP
        (Mac /Linux): python3 -m pytest -v test_4.py::test_compute_players_OBP
---------------------------------------------------------------'''



''' ---------Function: rank_players_OBP (3 points)--------------------
    Goal: If you have passed the previous test case, the result data frame should have been saved into a file, called 'moneyball_X8.csv'.  Now let's rank all of these players using the new metric: On-Base Percentage. 
(Rank Players by OBP) Given a dataframe (X8) of all the candidate players, rank all the players based upon descending order of On-Base Percentage (OBP). 
 If you have solved this problem and passed the test case, the result data frame will be saved into a file, called 'moneyball_R2.csv'. You could take a look at the ranking results of the players. 
    ---- Inputs: --------
    * X8: (Type: pd.DataFrame), a dataframe containing all the candidate players info, including Batting Average (BA) and On-Base Percentage (OBP).
    ---- Outputs: --------
    * R2: (Type: pd.DataFrame), a dataframe containing candidate players ranked by descending order of On-Base Percentage (OBP).
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def rank_players_OBP(X8:pd.DataFrame)->pd.DataFrame:
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    R2 = X8.sort_values(by='OBP', ascending=False).reset_index(drop=True)
    #########################################
    return R2

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_4.py::test_rank_players_OBP
        (Mac /Linux): python3 -m pytest -v test_4.py::test_rank_players_OBP
---------------------------------------------------------------'''



''' ---------Function: compute_players_1B (3 points)--------------------
    Goal: (Compute Players' 1B) Given a dataframe (X8) of all the candidate players, compute the number of singles (1B) of each player and insert a new column named '1B' to store the data. 
    ---- Inputs: --------
    * X8: (Type: pd.DataFrame), a dataframe containing all the candidate players info, including Batting Average (BA) and On-Base Percentage (OBP).
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_players_1B(X8:pd.DataFrame)->None:
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    X8['1B'] = X8['H'] - X8['2B'] - X8['3B'] - X8['HR']
    pass
    #########################################
'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_4.py::test_compute_players_1B
        (Mac /Linux): python3 -m pytest -v test_4.py::test_compute_players_1B
---------------------------------------------------------------'''



''' ---------Function: compute_players_TB (3 points)--------------------
    Goal: If you have passed the previous test case, the result data frame should have been saved into a file, called 'moneyball_X9.csv'.  Now let's compute the total number bases for each player. 
(Compute Players' TB) Given a dataframe (X9) of all the candidate players, compute the total number of bases (TB) of each player and insert a new column named 'TB' to store the data. 
    ---- Inputs: --------
    * X9: (Type: pd.DataFrame), a dataframe containing all the candidate players info, including Batting Average (BA), On-Base Percentage (OBP) and Singles (1B).
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_players_TB(X9:pd.DataFrame)->None:
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    X9['TB'] = (X9['1B'] * 1) + (X9['2B'] * 2) + (X9['3B'] * 3) + (X9['HR'] * 4)
    pass 
    #########################################
'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_4.py::test_compute_players_TB
        (Mac /Linux): python3 -m pytest -v test_4.py::test_compute_players_TB
---------------------------------------------------------------'''



''' ---------Function: compute_players_SLG (4 points)--------------------
    Goal: If you have passed the previous test case, the result data frame should have been saved into a file, called 'moneyball_X10.csv'.  Now let's compute the total number bases for each player. 
(Compute Players' SLG) Given a dataframe (X10) of all the candidate players, compute the slugging percentage (SLG) of each player and insert a new column named 'SLG' to store the data. 
    ---- Inputs: --------
    * X10: (Type: pd.DataFrame),  a dataframe containing all the candidate players info, including Batting Average (BA), On-Base Percentage (OBP) Singles (1B), and Total Bases (TB).
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_players_SLG(X10:pd.DataFrame)->None:
    #########################################
    ## INSERT YOUR CODE HERE (4 points)
    X10['SLG'] = X10['TB'] / X10['AB']
    pass 
    #########################################
'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_4.py::test_compute_players_SLG
        (Mac /Linux): python3 -m pytest -v test_4.py::test_compute_players_SLG
---------------------------------------------------------------'''



''' ---------Function: rank_players_SLG (3 points)--------------------
    Goal: If you have passed the previous test case, the result data frame should have been saved into a file, called 'moneyball_X11.csv'.  Now let's rank all of these players using the new metric: Slugging Percentage. 
(Rank Players by SLG) Given a dataframe (X11) of all the candidate players, rank all the players based upon descending order of Slugging Percentage (SLG). 
 If you have solved this problem and passed the test case, the result data frame will be saved into a file, called 'moneyball_R3.csv'. You could take a look at the ranking results of the players. 
    ---- Inputs: --------
    * X11: (Type: pd.DataFrame),  a dataframe containing all the candidate players info, including Batting Average (BA), On-Base Percentage (OBP) Singles (1B), Total Bases (TB) and Slugging Percentage (SLG).
    ---- Outputs: --------
    * R3: (Type: pd.DataFrame), a dataframe containing candidate players ranked by descending order of Slugging Percentage (SLG).
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def rank_players_SLG(X11:pd.DataFrame)->pd.DataFrame:
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    R3 = X11.sort_values(by='SLG', ascending=False).reset_index(drop=True)
    #########################################
    return R3

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_4.py::test_rank_players_SLG
        (Mac /Linux): python3 -m pytest -v test_4.py::test_rank_players_SLG
---------------------------------------------------------------'''




'''---------- Static Type Checking (optional) ---------
Before running unit tests for this problem file, please consider using the static typing checker to check your code above. Using static typing can help catch type-related issues, which can save time and prevent bugs from reaching runtime. Static type checking examines function signatures and variable types to ensure they align as intended, reducing the likelihood of encountering unexpected type errors.
Please type the following command in your terminal to check types in this problem file:
        (Windows OS): python -m mypy --check-untyped-defs problem4.py
        (Mac /Linux): python3 -m mypy --check-untyped-defs problem4.py
Note: Type-checking is optional. It's only used for debuging. The errors in the type checking are NOT considered in the grading. So you coud ignore the type-checking errors. Only errors in the unit tests (in grading.py) are considered in the grading.
---------------------------------------------------'''
'''-------- TEST problem4.py file: (27 points) ----------
Please type the following command in your terminal to test the correctness of all the above functions in this file:
        (Windows OS): python -m pytest -v test_4.py
        (Mac /Linux): python3 -m pytest -v test_4.py
------------------------------------------------------'''

'''---------- TEST ALL problem files in this HW assignment (100 points) ---------
 This is the last problem file in this homework assignment. 
Please type the following command in your terminal to test the correctness of all the problem files:
        (Windows OS): python -m pytest -v
        (Mac /Linux): python3 -m pytest -v
---------------------------------------------------'''

'''-------- Automatic Grading of This HW Assignment -------
Please type the following command in your terminal to compute your score of this HW assignment:
        (Windows OS): python grading.py
        (Mac /Linux): python3 grading.py
 The grading.py will run all the unit tests of this HW assignment and compute the scores you get. 
 For example, if your code for this HW can get 95 points, you will see this message at the end in the terminal
 ****************************
 ** Total Points: 95 / 100 ** (this is just an example, you need to run the grading.py to know your grade)
 ****************************

 NOTE: Due to the randomness of the test data and/or initialization of parameters, the results of the same unit test may vary in different runs. If your code could pass a test case with more than 80% probability, you won't lose points in that test case. If you lose points after the grading by the TA due to randomness of the testing, you could contact the TA to show that your code could pass that test case with more than 80% chance, and get the lost points back.

-------------------------------------------------
***   How to submit your work?  ***

After running the above grading script, a zip file named "submission.zip" will be created in the same folder of this homework assignment. Please upload this "submission.zip" file in canvas for your final submission. 
NOTE: Please only use the "submission.zip" generated by the grading script as your submision. Don't create a zip file yourself by including all the data files and folder structures in the zip. Because the TA will use an automatic script to grade all the submissions. The script requires all submissions to have a standard format and folder structure. If you create your own zip file, you may be using a different format or name in the submission, which may cause errors in the grading of your submission. Thanks a lot for your contribution to streamlining the grading of homework assignments.

 That's all! Great job! You did it!
----------------------------------------------------'''



'''---------List of All Variables ---------------
* X6: (Type: pd.DataFrame),  a dataframe containing all the candidate players for evaluation in the year (2001), who have sufficient experience (at least min_AB) and affordable price tag (at most max_salary). 
* X7: (Type: pd.DataFrame),  a dataframe containing all the candidate players info, including Batting Average (BA). 
* X8: (Type: pd.DataFrame),  a dataframe containing all the candidate players info, including Batting Average (BA) and On-Base Percentage (OBP). 
* X9: (Type: pd.DataFrame),  a dataframe containing all the candidate players info, including Batting Average (BA), On-Base Percentage (OBP) and Singles (1B). 
* X10: (Type: pd.DataFrame),   a dataframe containing all the candidate players info, including Batting Average (BA), On-Base Percentage (OBP) Singles (1B), and Total Bases (TB). 
* X11: (Type: pd.DataFrame),   a dataframe containing all the candidate players info, including Batting Average (BA), On-Base Percentage (OBP) Singles (1B), Total Bases (TB) and Slugging Percentage (SLG). 
* R1: (Type: pd.DataFrame),  a dataframe containing candidate players ranked by descending order of Batting Average (BA). 
* R2: (Type: pd.DataFrame),  a dataframe containing candidate players ranked by descending order of On-Base Percentage (OBP). 
* R3: (Type: pd.DataFrame),  a dataframe containing candidate players ranked by descending order of Slugging Percentage (SLG). 
--------------------------------------------'''



