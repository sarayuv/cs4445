
'''------------Turn on Word Wrap Setting in Your Editor--------------
    NOTE: For better readability of the instructions, 
          please turn on the 'Word Wrap' setting in your editor. 
    HOW: For example, in the VS Code editor, click "Settings" in the menu, 
         then type "word wrap" in the search box of the settings, 
    choose "on" in the drop-down menu.
    TEST: If you can read this long sentence without scrolling your screen from left to right, it means that your editor's word wrap setting is on and you are good to go. 
------------------------------------------------------------------'''


''' ------------ How to start? Set up Python and install packages --------
    If you are having troubles setting up your python environment, you could try the following steps to install a clean python environment.

    Step 1: Download the latest python installer from https://www.python.org/

    Step 2: Install the python environment by running the downloaded installer. During the installation, you may want to allow the program to set the path in your computer so that this python is your default python environment, which makes it easier for you to use. In windows, you may also want to allow longer path length during the setup process to avoid problems with long path strings of your folder. 

    Step 3: Open a terminal in your computer, and change the directory to the folder of this homework assignment using "cd <PATH>", here replace "<PATH>" with the path of this assignment on your computer. 

    Step 4: In the terminal, check the prompt.    If you can find a "(base)" at the beginning of your terminal prompt, you may have a conda installed in your computer. Please use the following command to disable the conda environment: 
        conda config --set auto_activate_base false
        conda deactivate

    Step 5: Update the Pip (python package manager) in the terminal. 
    Please type the following command in your terminal to update pip:
        (Windows OS): py -m pip install --upgrade pip
        (Mac /Linux): python3 -m pip install --upgrade pip

    Step 6: Install all the packages in a batch. 
    Please type the following command in your terminal to install all the required packages:
        (Windows OS): py -m pip install -r requirements.txt
        (Mac /Linux): python3 -m pip install -r requirements.txt
    
    Now your python environment is all set. 
     ------------------------------------------------'''


''' ------------Test Your Python Environment --------------
    After installing python and packages in your computer, you may want to test if your python environment meets the requirements. If your python version is incorrect or you didn't install a required package successfully, you may not be able to solve this homework assignment correctly.   
    Please type the following command in your terminal to test your python environment:
        (Windows OS): py -m pytest -v test_1.py::test_python_environment
        (Mac /Linux): python3 -m pytest -v test_1.py::test_python_environment
     ------------------------------------------------'''

#------------ No New Package --------------
# NOTE: Please don't import any new package. You should be able to solve the problems using only the package(s) imported here.
import re
import pandas as pd
#---------------------------------------------------------

#--------------------------
def Terms_and_Conditions():
    ''' 
      By submitting this homework or changing this function, you agree with the following terms:
       (1) Not sharing your code/solution with any student before and after the homework due. For example, sending your code segment to another student, putting your solution online or lending your laptop (if your laptop contains your solution or your Dropbox automatically copied your solution from your desktop computer to your laptop) to another student to work on this homework will violate this term.
       (2) Not using anyone's code in this homework and building your own solution. For example, using some code segments from another student or online resources due to any reason (like too busy recently) will violate this term. Changing other's code as your solution (such as changing the variable names) will also violate this term.
       (3) When discussing with any other students about this homework, only discuss high-level ideas or use pseudo-code. Don't discuss about the solution at the code level. For example, two students discuss about the solution of a function (which needs 5 lines of code to solve) and they then work on the solution "independently", however the code of the two solutions are exactly the same, or only with minor differences (variable names are different). In this case, the two students violate this term.
      All violations of (1),(2) or (3) will be handled in accordance with the WPI Academic Honesty Policy.  For more details, please visit: https://www.wpi.edu/about/policies/academic-integrity/dishonesty
      Note: We may use the Stanford Moss system to check your code for code similarity. https://theory.stanford.edu/~aiken/moss/
      Historical Data: In one year, we ended up finding 25% of the students in that class violating one of the above terms and we handled ALL of these violations according to the WPI Academic Honesty Policy. 
    '''
    #*******************************************
    # CHANGE HERE: if you have read and agree with the term above, change "False" to "True".
    Read_and_Agree = False
    #*******************************************
    return Read_and_Agree
#--------------------------

# ---------------------------------------------------------
'''
    Goal of Problem 1: Ranking Webpages using Counts of Keywords (15 points)
    In this problem, we will implement a webpage ranking algorithm: We will use the frequency of keywords in the webpages to determine the ranking. We will use this method on a small dataset of 8 webpages and create a demo to show the result of the search engine. 
 ------------------------------------------------------ 
      Search Engine (Version 1): Rank by Word Frequency 
 ------------------------------------------------------ 
 In this version of the search engine, the webpages with the most occurrence of the searched keyword will appear on the top of the result.
    A list of all variables being used in this problem is provided at the end of this file. 
'''
# ---------------------------------------------------------

''' ---------Function: load_webpages (5 points)--------------------
    Goal: (Load Webpage Data) Given a file name of a CSV file containing all the webpages, load the CSV file into a pandas dataframe. Each row contains information from a webpage. The data frame has 4 columns: ID, URL, Title and Description. 
    ---- Inputs: --------
    * filename: (Type: str), a string, indicating the path and name of a CSV file, which contains the webpage data.
    ---- Outputs: --------
    * X: (Type: pd.DataFrame), a dataframe of all the webpages, where each row represents a webpage.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def load_webpages(filename:str)->pd.DataFrame:
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    
    #########################################
    return X

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_1.py::test_load_webpages
        (Mac /Linux): python3 -m pytest -v test_1.py::test_load_webpages
---------------------------------------------------------------'''



''' ---------Function: count_word_frequency (5 points)--------------------
    Goal: (Count Word Frequency) Given the dataframe X, compute the frequency of the keywords in each webpage's 'Description' and add a column (called 'Count') to the dataframe X to store the frequencies of the searched keyword. 
	 For example, if the searched keyword is 'thanksgiving', and we have the following webpages: 
	 Webpage 0: Thanksgiving is coming 
	 Webpage 1: This is my thanksgiving recipe for my thanksgiving dinner 
	 Webpage 2: Hello world 
	 Then the result dataframe X should be as follows: 
	    ID  | URL | ...| Count 
	  ----------------------- 
	    0   | ... | ...| 1 
	    1   | ... | ...| 2 
	    2   | ... | ...| 0 
	  ----------------------- 
	 Note, the keyword matching is not case-sensitive. So we assume that all words in the webpages should be converted to lower cases before being matched with the keyword. For example, in webpage 0, the 'Thanksgiving' should be first converted to lower cases 'thanksgiving', then it will match with the keyword 'thanksgiving' and being counted. 
    ---- Inputs: --------
    * X: (Type: pd.DataFrame), a dataframe of all the webpages, where each row represents a webpage.
    * keyword: (Type: str), the searched keyword, a string, here we assume the string contains only one word that is being searched.
    ---- Outputs: --------
    * X: (Type: pd.DataFrame), a dataframe of all the webpages, where each row represents a webpage.
    ---- Hints: --------
    * In a pandas Series x (which is a column of a dataframe X), you could find various functions for x.str to process string values, for example if a function is named f(), you could call the function by x.str.f(). 
    * To ignore the cases in word count, you could use a flag value in the "re" package as the parameter for the above f() function. Here "re" is designed for regular expression. 
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def count_word_frequency(X:pd.DataFrame, keyword:str)->pd.DataFrame:
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    
    #########################################
    return X

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_1.py::test_count_word_frequency
        (Mac /Linux): python3 -m pytest -v test_1.py::test_count_word_frequency
---------------------------------------------------------------'''

''' 
    If you have passed the above test, the result data should have been saved into a file, named "data_X1.csv". You could take a look at this file for the result.
    
'''


''' ---------Function: rank_word_frequency (5 points)--------------------
    Goal: (Rank Webpages by Word Frequency) Given the dataframe (X1), rank all the webpages by descending order of Keyword frequency (Count). 
    ---- Inputs: --------
    * X1: (Type: pd.DataFrame), a dataframe of all the webpages containing the column of word frequency, where each row represents a webpage.
    ---- Outputs: --------
    * R1: (Type: pd.DataFrame), a dataframe of all the webpages, where the webpages are sorted according to descending order of word frequency.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def rank_word_frequency(X1:pd.DataFrame)->pd.DataFrame:
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    
    #########################################
    return R1

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_1.py::test_rank_word_frequency
        (Mac /Linux): python3 -m pytest -v test_1.py::test_rank_word_frequency
---------------------------------------------------------------'''

''' 
    If you have passed the above test, the result data should have been saved into a file, named "data_R1.csv". You could take a look at this file for the ranking result.
    
'''

'''---------- Demo -----------------
Please type the following command in your terminal to test the search engine that you have built:
        (Windows OS): py demo1.py
        (Mac /Linux): python3 demo1.py
The website will be hosted in your computer and you could copy the testing URL shown in the terminal to a web browser to use the website. Once it is done, you could terminate the web server by pressing Ctrl+C in the terminal.
-------------------------------------'''



'''---------- Static Type Checking (optional) ---------
Before running unit tests for this problem file, please consider using the static typing checker to check your code above. Using static typing can help catch type-related issues, which can save time and prevent bugs from reaching runtime. Static type checking examines function signatures and variable types to ensure they align as intended, reducing the likelihood of encountering unexpected type errors.
Please type the following command in your terminal to check types in this problem file:
        (Windows OS): py -m mypy --check-untyped-defs problem1.py
        (Mac /Linux): python3 -m mypy --check-untyped-defs problem1.py
Note: Type-checking is optional. It's only used for debuging. The errors in the type checking are NOT considered in the grading. So you coud ignore the type-checking errors. Only errors in the unit tests (in grading.py) are considered in the grading.
---------------------------------------------------'''
'''-------- TEST problem1.py file: (15 points) ----------
Please type the following command in your terminal to test the correctness of all the above functions in this file:
        (Windows OS): py -m pytest -v test_1.py
        (Mac /Linux): python3 -m pytest -v test_1.py
------------------------------------------------------'''





'''---------List of All Variables ---------------
* filename: (Type: str),  a string, indicating the path and name of a CSV file, which contains the webpage data. 
* X: (Type: pd.DataFrame),  a dataframe of all the webpages, where each row represents a webpage. 
* keyword: (Type: str),  the searched keyword, a string, here we assume the string contains only one word that is being searched. 
* X1: (Type: pd.DataFrame),  a dataframe of all the webpages containing the column of word frequency, where each row represents a webpage. 
* R1: (Type: pd.DataFrame),  a dataframe of all the webpages, where the webpages are sorted according to descending order of word frequency. 
--------------------------------------------'''



