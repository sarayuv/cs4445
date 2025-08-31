




#------------ No New Package --------------
# NOTE: Please don't import any new package. You should be able to solve the problems using only the package(s) imported here.
import pandas as pd
from problem3 import compute_ratings
#---------------------------------------------------------


# ---------------------------------------------------------
'''
    Goal of Problem 4: Ranking NCAA teams using Elo ranking algorithm (30 points)
    In this problem, you will use the Elo rating algorithm to rank the NCAA teams, based upon a dataset of game results between the teams
.
    A list of all variables being used in this problem is provided at the end of this file. 
'''
# ---------------------------------------------------------

''' ---------Function: load_G (5 points)--------------------
    Goal: (Load Game Data) Load game results from a CSV file into a pandas dataframe. Each row contains two numbers, which represents the IDs of the winning team and losing team in the game in one game. 
	 For example, if  we have three game results in the file: 
	    Game 1: team 0 wins, team 1 loses 
	    Game 2: team 1 wins, team 2 loses 
	    Game 3: team 0 wins, team 2 loses 
	 The dataframe will be: 
	    win_ID  | lose_ID 
	  --------------------- 
	    0       |    1 
	    1       |    2 
	    0       |    2 
	  --------------------- . 
    ---- Inputs: --------
    * filename_G: (Type: str), the file name of game results G, a string. .
    ---- Outputs: --------
    * G: (Type: pd.DataFrame), a dataframe of all the game results, a pandas data frame of shape (m by 2), where each row of the matrix G[i] represents the result of the i-th game, and G[i] = (A,B) contains the IDs of the winning team (A) and losing team (B) in the game.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def load_G(filename_G:str='ncaa_games.csv')->pd.DataFrame:
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    
    #########################################
    return G

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_4.py::test_load_G
        (Mac /Linux): python3 -m pytest -v test_4.py::test_load_G
---------------------------------------------------------------'''



''' ---------Function: load_teams (5 points)--------------------
    Goal: (Load Team Names) Load the team names from a CSV file into a pandas dataframe. 
	 For example, if we have three teams in the file with names: 
	    Team 0: 'A' 
	    Team 1: 'B' 
	    Team 2: 'C' 
	 The dataframe will be: 
	    ID  | Name 
	  --------------- 
	    0   |   A 
	    1   |   B 
	    2   |   C 
	  --------------- . 
    ---- Inputs: --------
    * filename_teams: (Type: str), the file name of team names, a string. In this file, each row contains a name of a team, and the i-th row of the file contains the name of the i-th team (team ID = i). For example, the 0-th row contains the name of the team ID = 0 ("Liberty"), the 1-st row contains the name of the team ID=1 ("Randolph Col").
    ---- Outputs: --------
    * T: (Type: pd.DataFrame), a dataframe of all the team names in NCAA,  such as "Liberty", "Randolph Col","Valparaiso".
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def load_teams(filename_teams:str='ncaa_teams.csv')->pd.DataFrame:
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    
    #########################################
    return T

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_4.py::test_load_teams
        (Mac /Linux): python3 -m pytest -v test_4.py::test_load_teams
---------------------------------------------------------------'''



''' ---------Function: compute_elo (10 points)--------------------
    Goal: (compute Elo ratings) Now let's compute the elo ratings of all the NCCA teams in the dataset. Given dataframe (G) containing all the game result between the teams, compute a Elo ratings of all teams. 
	 For example, if we have three teams (n = 3) and after computing Elo ratings, the ratings (R) is: 
	 The dataframe will be: 
	    ID  | Elo 
	  --------------- 
	    0   | 300 
	    1   | 500 
	    2   | 400 
	  ---------------
. 
    ---- Inputs: --------
    * G: (Type: pd.DataFrame), a dataframe of all the game results, a pandas data frame of shape (m by 2), where each row of the matrix G[i] represents the result of the i-th game, and G[i] = (A,B) contains the IDs of the winning team (A) and losing team (B) in the game.
    * n: (Type: int), the total number of teams to rank, an integer scalar.
    * K: (Type: float), k-factor, a constant number which controls how maximum amount of change that can be applied on the rating of a team based upon the result of one game.
    ---- Outputs: --------
    * R: (Type: pd.DataFrame), a dataframe of the Elo ratings of all the n teams, where i-th row of R contains the ID and the Elo rating of the i-th team.
    ---- Hints: --------
    * You could use some function implemented in problem 3 to solve this problem. 
    * This problem can be solved using 2 line(s) of code. More lines are okay. ''' 

def compute_elo(G:pd.DataFrame, n:int, K:float=16.0)->pd.DataFrame:
    #########################################
    ## INSERT YOUR CODE HERE (10 points)
    
    #########################################
    return R

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_4.py::test_compute_elo
        (Mac /Linux): python3 -m pytest -v test_4.py::test_compute_elo
---------------------------------------------------------------'''



''' ---------Function: merge_team (5 points)--------------------
    Goal: If you have passed the previous test case, the result data frame should have been saved into a file, called 'ncaa_R.csv. Now the dataset only contains Elo ratings, but no team name is available. We have another CSV file 'ncaa_teams.csv', which contains the team names. It would be better if we can combine these two datasets into one data frame, so the new data frame contains both team names and Elo ratings. 
 (Merge the two dataframes) Given a data frame (T) of team names , and a data frame (R) of Elo ratings (loaded from 'ncaa_R.csv'), Combine the two data frames into one, according to the ID column. . 
    ---- Inputs: --------
    * T: (Type: pd.DataFrame), a dataframe of all the team names in NCAA,  such as "Liberty", "Randolph Col","Valparaiso".
    * R: (Type: pd.DataFrame), a dataframe of the Elo ratings of all the n teams, where i-th row of R contains the ID and the Elo rating of the i-th team.
    ---- Outputs: --------
    * X: (Type: pd.DataFrame), a dataframe of all the team names in NCAA merged with their Elo ratings.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def merge_team(T:pd.DataFrame, R:pd.DataFrame)->pd.DataFrame:
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    
    #########################################
    return X

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_4.py::test_merge_team
        (Mac /Linux): python3 -m pytest -v test_4.py::test_merge_team
---------------------------------------------------------------'''



''' ---------Function: rank_teams_Elo (5 points)--------------------
    Goal: If you have passed the previous test case, the result data frame should have been saved into a file, called 'ncaa_X.csv'.  Now let's rank all of these teams using the Elo ratings in descending order. 
(Rank Teams by Elo) Given a dataframe (X) of all the teams, rank all the teams based upon descending order of Elo ratings (Elo). 
 If you have solved this problem and passed the test case, the result data frame will be saved into a file, called 'ncaa_Elo.csv'. You could take a look at the ranking results of the teams. 
    ---- Inputs: --------
    * X: (Type: pd.DataFrame), a dataframe of all the team names in NCAA merged with their Elo ratings.
    ---- Outputs: --------
    * Y: (Type: pd.DataFrame), a dataframe of all the team names in NCAA sorted according to the descending order of their Elo ratings.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def rank_teams_Elo(X:pd.DataFrame)->pd.DataFrame:
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    
    #########################################
    return Y

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_4.py::test_rank_teams_Elo
        (Mac /Linux): python3 -m pytest -v test_4.py::test_rank_teams_Elo
---------------------------------------------------------------'''




'''---------- Static Type Checking (optional) ---------
Before running unit tests for this problem file, please consider using the static typing checker to check your code above. Using static typing can help catch type-related issues, which can save time and prevent bugs from reaching runtime. Static type checking examines function signatures and variable types to ensure they align as intended, reducing the likelihood of encountering unexpected type errors.
Please type the following command in your terminal to check types in this problem file:
        (Windows OS): py -m mypy --check-untyped-defs problem4.py
        (Mac /Linux): python3 -m mypy --check-untyped-defs problem4.py
Note: Type-checking is optional. It's only used for debuging. The errors in the type checking are NOT considered in the grading. So you coud ignore the type-checking errors. Only errors in the unit tests (in grading.py) are considered in the grading.
---------------------------------------------------'''
'''-------- TEST problem4.py file: (30 points) ----------
Please type the following command in your terminal to test the correctness of all the above functions in this file:
        (Windows OS): py -m pytest -v test_4.py
        (Mac /Linux): python3 -m pytest -v test_4.py
------------------------------------------------------'''

'''---------- TEST ALL problem files in this HW assignment (100 points) ---------
 This is the last problem file in this homework assignment. 
Please type the following command in your terminal to test the correctness of all the problem files:
        (Windows OS): py -m pytest -v
        (Mac /Linux): python3 -m pytest -v
---------------------------------------------------'''

'''-------- Automatic Grading of This HW Assignment -------
Please type the following command in your terminal to compute your score of this HW assignment:
        (Windows OS): py grading.py
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
* filename_G: (Type: str),  the file name of game results G, a string. . 
* filename_teams: (Type: str),  the file name of team names, a string. In this file, each row contains a name of a team, and the i-th row of the file contains the name of the i-th team (team ID = i). For example, the 0-th row contains the name of the team ID = 0 ("Liberty"), the 1-st row contains the name of the team ID=1 ("Randolph Col"). 
* G: (Type: pd.DataFrame),  a dataframe of all the game results, a pandas data frame of shape (m by 2), where each row of the matrix G[i] represents the result of the i-th game, and G[i] = (A,B) contains the IDs of the winning team (A) and losing team (B) in the game. 
* T: (Type: pd.DataFrame),  a dataframe of all the team names in NCAA,  such as "Liberty", "Randolph Col","Valparaiso". 
* R: (Type: pd.DataFrame),  a dataframe of the Elo ratings of all the n teams, where i-th row of R contains the ID and the Elo rating of the i-th team. 
* K: (Type: float),  k-factor, a constant number which controls how maximum amount of change that can be applied on the rating of a team based upon the result of one game. 
* n: (Type: int),  the total number of teams to rank, an integer scalar. 
* m: (Type: int),  the total number of games played, an integer scalar. 
* X: (Type: pd.DataFrame),  a dataframe of all the team names in NCAA merged with their Elo ratings. 
* Y: (Type: pd.DataFrame),  a dataframe of all the team names in NCAA sorted according to the descending order of their Elo ratings. 
--------------------------------------------'''



