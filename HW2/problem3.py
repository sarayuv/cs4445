




#------------ No New Package --------------
# NOTE: Please don't import any new package. You should be able to solve the problems using only the package(s) imported here.
import pandas as pd
#---------------------------------------------------------


# ---------------------------------------------------------
'''
    Goal of Problem 3: Elo ranking algorithm (25 points)
    In this problem, you will implement the Elo rating algorithm to rank players based upon match results (win/lose). Assuming all the players' performance are random following a Logistic distribution with a scale of 400
.
    A list of all variables being used in this problem is provided at the end of this file. 
'''
# ---------------------------------------------------------

''' ---------Function: compute_EA (5 points)--------------------
    Goal: Given the current ratings of player A and player B, compute the expected probability of player A (with rating RA) to win in a game against player B (with rating RB). 
    ---- Inputs: --------
    * RA: (Type: float), the rating of player A (the average performance of the player), a float scalar value.
    * RB: (Type: float), .
    ---- Outputs: --------
    * EA: (Type: float), the expected probability of player A wins when competing with player B in a game, a float scalar value between 0 and 1.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_EA(RA:float, RB:float)->float:
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    EA = 1 / (1 + 10 ** ((RB - RA) / 400))
    #########################################
    return EA

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_3.py::test_compute_EA
        (Mac /Linux): python3 -m pytest -v test_3.py::test_compute_EA
---------------------------------------------------------------'''



''' ---------Function: compute_EB (5 points)--------------------
    Goal: Given the expected probability of player A (with rating RA) to win in a game against a player B (with rating RB). 
    ---- Inputs: --------
    * EA: (Type: float), the expected probability of player A wins when competing with player B in a game, a float scalar value between 0 and 1.
    ---- Outputs: --------
    * EB: (Type: float), the expected probability of player B wins when competing with player A in a game, a float scalar value between 0 and 1.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_EB(EA:float)->float:
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    EB = 1 - EA
    #########################################
    return EB

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_3.py::test_compute_EB
        (Mac /Linux): python3 -m pytest -v test_3.py::test_compute_EB
---------------------------------------------------------------'''



''' ---------Function: update_RA (5 points)--------------------
    Goal: Given the result of one game between player A and player B, the current ratings of both players, compute the new rating of player A. 
    ---- Inputs: --------
    * RA: (Type: float), the rating of player A (the average performance of the player), a float scalar value.
    * SA: (Type: int), the result of one game where player A is competing with player B, a scalar value. If player A wins in this game, SA = 1; if player A loses, SA =0.
    * EA: (Type: float), the expected probability of player A wins when competing with player B in a game, a float scalar value between 0 and 1.
    * K: (Type: float), k-factor, a constant number which controls the maximum amount of change that can be applied on the rating of a player based upon the result of one game.
    ---- Outputs: --------
    * RA: (Type: float), the rating of player A (the average performance of the player), a float scalar value.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def update_RA(RA:float, SA:int, EA:float, K:float=16.0)->float:
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    RA = RA + K * (SA - EA)
    #########################################
    return RA

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_3.py::test_update_RA
        (Mac /Linux): python3 -m pytest -v test_3.py::test_update_RA
---------------------------------------------------------------'''



''' ---------Function: update_RB (5 points)--------------------
    Goal: Given the result of one game between player A and player B, the current ratings of both players, compute the new rating of player B. 
    ---- Inputs: --------
    * RB: (Type: float), .
    * SB: (Type: int), the result of one game where player B is competing with player A, a scalar value. If player B wins in this game, SB = 1; if player B loses, SB =0.
    * EB: (Type: float), the expected probability of player B wins when competing with player A in a game, a float scalar value between 0 and 1.
    * K: (Type: float), k-factor, a constant number which controls the maximum amount of change that can be applied on the rating of a player based upon the result of one game.
    ---- Outputs: --------
    * RB: (Type: float), .
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def update_RB(RB:float, SB:int, EB:float, K:float=16.0)->float:
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    RB = RB + K * (SB - EB)
    #########################################
    return RB

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_3.py::test_update_RB
        (Mac /Linux): python3 -m pytest -v test_3.py::test_update_RB
---------------------------------------------------------------'''



''' ---------Function: compute_ratings (5 points)--------------------
    Goal: Given the result of one game between player A and player B, the current ratings of both players, compute the new ratings of players A and B. 
    ---- Inputs: --------
    * G: (Type: pd.DataFrame), a dataframe of all the game results, a pandas data frame of shape (m by 2), where each row of the matrix G[i] represents the result of the i-th game, and G[i] = (A,B) contains the IDs of the winning team (A) and losing team (B) in the game.
    * n: (Type: int), the total number of players to rank, an integer scalar.
    * K: (Type: float), k-factor, a constant number which controls the maximum amount of change that can be applied on the rating of a player based upon the result of one game.
    ---- Outputs: --------
    * R: (Type: list[float]), the ratings of all the n players, a list of length n, where R[i] represents the current rating of the i-th player.
    ---- Hints: --------
    * Step 1 extract current rating of the winning player (A) of the game from the list R. 
    * Step 2 extract current rating of the losing player (B) of the game from the list R. 
    * Step 3 compute the expected winning probability of player A in the game. 
    * Step 4 compute the expected winning probability of player B in the game. 
    * Step 5 update player A's rating based upon the game result and write it back to the list R. 
    * Step 6 update player B's rating based upon the game result and write it back to the list R. 
    * This problem can be solved using 5 line(s) of code. More lines are okay. ''' 

def compute_ratings(G:pd.DataFrame, n:int, K:float=16.0)->list[float]:
    R = [400.]*n # initialize the ratings of all players with 400
    for index, row in G.iterrows(): # for each game, update the ratings based upon the result of the game
        A,B = row["win_ID"], row["lose_ID"] # # extract the player IDs as A and B
        SA,SB = 1,0 # the game result: Player A wins, Player B loses
        #########################################
        ## INSERT YOUR CODE HERE (5 points)
        RA = R[A]
        RB = R[B]
        EA = compute_EA(RA, RB)
        EB = compute_EB(EA)
        R[A] = update_RA(RA, SA, EA, K)
        R[B] = update_RB(RB, SB, EB, K)
        #########################################
    return R

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_3.py::test_compute_ratings
        (Mac /Linux): python3 -m pytest -v test_3.py::test_compute_ratings
---------------------------------------------------------------'''




'''---------- Static Type Checking (optional) ---------
Before running unit tests for this problem file, please consider using the static typing checker to check your code above. Using static typing can help catch type-related issues, which can save time and prevent bugs from reaching runtime. Static type checking examines function signatures and variable types to ensure they align as intended, reducing the likelihood of encountering unexpected type errors.
Please type the following command in your terminal to check types in this problem file:
        (Windows OS): py -m mypy --check-untyped-defs problem3.py
        (Mac /Linux): python3 -m mypy --check-untyped-defs problem3.py
Note: Type-checking is optional. It's only used for debuging. The errors in the type checking are NOT considered in the grading. So you coud ignore the type-checking errors. Only errors in the unit tests (in grading.py) are considered in the grading.
---------------------------------------------------'''
'''-------- TEST problem3.py file: (25 points) ----------
Please type the following command in your terminal to test the correctness of all the above functions in this file:
        (Windows OS): py -m pytest -v test_3.py
        (Mac /Linux): python3 -m pytest -v test_3.py
------------------------------------------------------'''





'''---------List of All Variables ---------------
* RA: (Type: float),  the rating of player A (the average performance of the player), a float scalar value. 
* RB: (Type: float),  . 
* EA: (Type: float),  the expected probability of player A wins when competing with player B in a game, a float scalar value between 0 and 1. 
* EB: (Type: float),  the expected probability of player B wins when competing with player A in a game, a float scalar value between 0 and 1. 
* SA: (Type: int),  the result of one game where player A is competing with player B, a scalar value. If player A wins in this game, SA = 1; if player A loses, SA =0. 
* SB: (Type: int),  the result of one game where player B is competing with player A, a scalar value. If player B wins in this game, SB = 1; if player B loses, SB =0. 
* K: (Type: float),  k-factor, a constant number which controls the maximum amount of change that can be applied on the rating of a player based upon the result of one game. 
* n: (Type: int),  the total number of players to rank, an integer scalar. 
* m: (Type: int),  the total number of games played, an integer scalar. 
* R: (Type: list[float]),  the ratings of all the n players, a list of length n, where R[i] represents the current rating of the i-th player. 
* G: (Type: pd.DataFrame),  a dataframe of all the game results, a pandas data frame of shape (m by 2), where each row of the matrix G[i] represents the result of the i-th game, and G[i] = (A,B) contains the IDs of the winning team (A) and losing team (B) in the game. 
--------------------------------------------'''



