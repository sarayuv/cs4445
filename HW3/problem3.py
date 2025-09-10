




#------------ No New Package --------------
# NOTE: Please don't import any new package. You should be able to solve the problems using only the package(s) imported here.
import numpy as np
import pandas as pd
#---------------------------------------------------------


# ---------------------------------------------------------
'''
    Goal of Problem 3: Ranking webpages using counts of in-links (15 points)
    In this problem, you will implement the ranking algorithm for webpages using the counts of in-links. 
 ------------------------------------ 
      Search Engine (Version 2) 
 ------------------------------------ 
 The earliest version of Google search is simply counting the number of in-links (the hyperlinks from other webpages to this webpage) .
    A list of all variables being used in this problem is provided at the end of this file. 
'''
# ---------------------------------------------------------

''' ---------Function: count_in_links (5 points)--------------------
    Goal: Given an adjacency matrix A of a webpage hyperlink network, compute the counts of in-links for each webpage in the network. 
    ---- Inputs: --------
    * A: (Type: np.ndarray), the adjacency matrix indicating the hyperlinks between webpages, a numpy matrix of shape (n X n). A[i][j] =1, if there is a hyperlink from webpage j to webpage i; A[j][i]=0, if there is no hyperlink from webpage j to webpage i.
    ---- Outputs: --------
    * c: (Type: np.ndarray), the number of in-links for each webpage, a numpy vector of length n, where c[i] is the number of in-links pointing to webpage i.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def count_in_links(A:np.ndarray)->np.ndarray:
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    c = np.sum(A, axis=1)
    #########################################
    return c

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_3.py::test_count_in_links
        (Mac /Linux): python3 -m pytest -v test_3.py::test_count_in_links
---------------------------------------------------------------'''



''' ---------Function: add_column_inlinks (5 points)--------------------
    Goal: Given the counts of in-links of each webpage and the dataframe storing all the webpages (X1), insert a new column (named 'Inlinks') to the dataframe X1 to store the number of inlinks for each webpage. 
    ---- Inputs: --------
    * X1: (Type: pd.DataFrame),  a dataframe of all the webpages containing the column of word frequency, where each row represents a webpage.
    * c: (Type: np.ndarray), the number of in-links for each webpage, a numpy vector of length n, where c[i] is the number of in-links pointing to webpage i.
    ---- Outputs: --------
    * X1: (Type: pd.DataFrame),  a dataframe of all the webpages containing the column of word frequency, where each row represents a webpage.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def add_column_inlinks(X1:pd.DataFrame, c:np.ndarray)->pd.DataFrame:
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    X1['Inlinks'] = c
    #########################################
    return X1

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_3.py::test_add_column_inlinks
        (Mac /Linux): python3 -m pytest -v test_3.py::test_add_column_inlinks
---------------------------------------------------------------'''

''' 
    If you have passed the above test, the result data should have been saved into a file, named "data_X2.csv", you could take a look at this file for the result.
    
'''


''' ---------Function: rank_inlinks (5 points)--------------------
    Goal: (Rank Webpages by Word Frequency) Given a dataframe (X2) of all the webpages, rank all the webpages by descending order of # inlinks ('InLinks'). 
    ---- Inputs: --------
    * X2: (Type: pd.DataFrame),  a dataframe of all the webpages containing the columns of word frequency and number of inlinks, where each row represents a webpage.
    ---- Outputs: --------
    * R2: (Type: pd.DataFrame),  a dataframe of all the webpages, where the webpages are sorted according to descending order of the number of in-links .
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def rank_inlinks(X2:pd.DataFrame)->pd.DataFrame:
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    R2 = X2.sort_values(by='Inlinks', ascending=False)
    #########################################
    return R2

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_3.py::test_rank_inlinks
        (Mac /Linux): python3 -m pytest -v test_3.py::test_rank_inlinks
---------------------------------------------------------------'''

''' 
    If you have passed the above test, the result data should have saved into a file, named "data_R2.csv". You could take a look at this file for the ranking result.
    
'''

'''---------- Demo -----------------
Please type the following command in your terminal to test the search engine that you have built:
        (Windows OS): py demo2.py
        (Mac /Linux): python3 demo2.py
The website will be hosted in your computer and you could copy the testing URL shown in the terminal to a web browser to use the website. Once it is done, you could terminate the web server by pressing Ctrl+C in the terminal.
-------------------------------------'''



'''---------- Static Type Checking (optional) ---------
Before running unit tests for this problem file, please consider using the static typing checker to check your code above. Using static typing can help catch type-related issues, which can save time and prevent bugs from reaching runtime. Static type checking examines function signatures and variable types to ensure they align as intended, reducing the likelihood of encountering unexpected type errors.
Please type the following command in your terminal to check types in this problem file:
        (Windows OS): py -m mypy --check-untyped-defs problem3.py
        (Mac /Linux): python3 -m mypy --check-untyped-defs problem3.py
Note: Type-checking is optional. It's only used for debuging. The errors in the type checking are NOT considered in the grading. So you coud ignore the type-checking errors. Only errors in the unit tests (in grading.py) are considered in the grading.
---------------------------------------------------'''
'''-------- TEST problem3.py file: (15 points) ----------
Please type the following command in your terminal to test the correctness of all the above functions in this file:
        (Windows OS): py -m pytest -v test_3.py
        (Mac /Linux): python3 -m pytest -v test_3.py
------------------------------------------------------'''





'''---------List of All Variables ---------------
* A: (Type: np.ndarray),  the adjacency matrix indicating the hyperlinks between webpages, a numpy matrix of shape (n X n). A[i][j] =1, if there is a hyperlink from webpage j to webpage i; A[j][i]=0, if there is no hyperlink from webpage j to webpage i. 
* c: (Type: np.ndarray),  the number of in-links for each webpage, a numpy vector of length n, where c[i] is the number of in-links pointing to webpage i. 
* X1: (Type: pd.DataFrame),   a dataframe of all the webpages containing the column of word frequency, where each row represents a webpage. 
* X2: (Type: pd.DataFrame),   a dataframe of all the webpages containing the columns of word frequency and number of inlinks, where each row represents a webpage. 
* R2: (Type: pd.DataFrame),   a dataframe of all the webpages, where the webpages are sorted according to descending order of the number of in-links . 
* n: (Type: int),  the number of all webpages in the network, an integer scalar. 
--------------------------------------------'''



