




#------------ No New Package --------------
# NOTE: Please don't import any new package. You should be able to solve the problems using only the package(s) imported here.
import pandas as pd
#---------------------------------------------------------


# ---------------------------------------------------------
'''
    Goal of Problem 2: Getting familiar with pandas package (27 points)
     In this problem, we will get familiar with the Pandas python package.  Pandas is the library for tabular data analysis in Python.  It provides fast, flexible, and expressive data structures designed to make working with tabular and multidimensional data both easy and intuitive.  You could read the tutorials for Pandas: 
	 https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/ 
	 https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html .
    A list of all variables being used in this problem is provided at the end of this file. 
'''
# ---------------------------------------------------------

''' ---------Function: dataframe (3 points)--------------------
    Goal: Create the following data frame with 2 columns (height and width) and 3 rows/records using Pandas: 
	|'height'| 'width' | 
	|--------|---------| 
	|    1   |    4    | 
	|    2   |    5    | 
	|    3   |    6    |. 
    ---- Outputs: --------
    * X: (Type: pd.DataFrame), a pandas dataframe.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def dataframe()->pd.DataFrame:
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    X = pd.DataFrame(
        {'height': [1, 2, 3], 
         'width': [4, 5, 6]}
         )
    #########################################
    return X

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_2.py::test_dataframe
        (Mac /Linux): python3 -m pytest -v test_2.py::test_dataframe
---------------------------------------------------------------'''



''' ---------Function: load_csv (3 points)--------------------
    Goal: Load a data frame from CSV file. The CSV file contains a header line (the first row), indicating the names of all the columns. 
    ---- Inputs: --------
    * filename: (Type: str), the file name of a CSV file, a string.
    ---- Outputs: --------
    * X: (Type: pd.DataFrame), a pandas dataframe.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def load_csv(filename:str)->pd.DataFrame:
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    X = pd.read_csv(filename)
    #########################################
    return X

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_2.py::test_load_csv
        (Mac /Linux): python3 -m pytest -v test_2.py::test_load_csv
---------------------------------------------------------------'''



''' ---------Function: save_csv (3 points)--------------------
    Goal: Save a data frame (X) into a CSV file (filename). Note the CSV file should NOT contain the index column. 
    ---- Inputs: --------
    * X: (Type: pd.DataFrame), a pandas dataframe.
    * filename: (Type: str), the file name of a CSV file, a string.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def save_csv(X:pd.DataFrame, filename:str)->None:
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    X.to_csv(filename, index=False)
    #########################################
'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_2.py::test_save_csv
        (Mac /Linux): python3 -m pytest -v test_2.py::test_save_csv
---------------------------------------------------------------'''



''' ---------Function: filter_height (3 points)--------------------
    Goal: filter all the data records in a dataframe with height (column) greater or equals to a threshold value. For example, suppose we have the following dataframe as the input: 
	|'height'| 'width' | 
	|--------|---------| 
	|    0   |    4    | 
	|    1   |    5    | 
	|    2   |    6    | 
	|    3   |    7    | 
 If the threshold is 2, then all the rows with height greater or equal to 2 will be returned. The result will be another data frame: 
	|'height'| 'width' | 
	|--------|---------| 
	|    2   |    6    | 
	|    3   |    7    |. 
    ---- Inputs: --------
    * X: (Type: pd.DataFrame), a pandas dataframe.
    * t: (Type: int), an integer scalar, the threshold of the height.
    ---- Outputs: --------
    * Xt: (Type: pd.DataFrame),  the result dataframe, containing only the records with heights greater or equals to the threshold t.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def filter_height(X:pd.DataFrame, t:int)->pd.DataFrame:
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    Xt = X[X['height'] >= t]
    #########################################
    return Xt

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_2.py::test_filter_height
        (Mac /Linux): python3 -m pytest -v test_2.py::test_filter_height
---------------------------------------------------------------'''



''' ---------Function: group_sum (3 points)--------------------
    Goal: Group the data records in a dataframe according to a column (k). Then sum all the values within each group. Suppose we have the following data frame X: 
	| 'ID'   | 'count' | 
	|--------|---------| 
	|    1   |    4    | 
	|    1   |    5    | 
	|    2   |    6    | 
	|    2   |    7    | 
 We have duplicated values in ID column. Now we want to sum the 'count' values within each group of data records with the same ID's. So that the records with ID=1, should have a sum of 'count' = 4+5 = 9 and the records with ID=2, should have a sum of 'count' = 6+7 = 13 The output should be: 
	| 'ID'   | 'count' | 
	|--------|---------| 
	|    1   |    9    | 
	|    2   |    13   |. 
    ---- Inputs: --------
    * X: (Type: pd.DataFrame), a pandas dataframe.
    * k: (Type: str), a string indicating the name of a column in a data frame.
    ---- Outputs: --------
    * Y: (Type: pd.DataFrame), a pandas dataframe.
    ---- Hints: --------
    * you could use the groupby() function of pandas and solve this problem using two lines of code. 
    * To convert an index into a column, you could use reset_index() method in a pandas dataframe. 
    * This problem can be solved using 2 line(s) of code. More lines are okay. ''' 

def group_sum(X:pd.DataFrame, k:str)->pd.DataFrame:
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    Y = X.groupby(k)['count'].sum().reset_index()
    #########################################
    return Y

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_2.py::test_group_sum
        (Mac /Linux): python3 -m pytest -v test_2.py::test_group_sum
---------------------------------------------------------------'''



''' ---------Function: merge (3 points)--------------------
    Goal: Merge two data frames on a column (k) into one joint data frame. Suppose we have the following data frame X: 
	| 'ID'   | 'count' | 
	|--------|---------| 
	|    1   |    9    | 
	|    2   |    13   |

  and we have another data frame  Y: 
	| 'ID'   | 'name'  | 
	|--------|---------| 
	|    1   | 'Alex'  | 
	|    2   | 'Bob'   | 
	|    3   | 'Tom'   | 
 Merge the two tables with k='ID'. The output should be: 
	| 'ID'   | 'count' |  'name'  | 
	|--------|---------| ---------| 
	|    1   |    9    |   'Alex' | 
	|    2   |    13   |   'Bob'  | 
 In database, there are different ways of joining two tables: 'inner join', 'left join', 'right join', 'outer join'. Here we using 'inner join' of the two tables to get the result table (dataframe). 
 In cases when the two tables have columns with identical names, suffixes '_x', '_y' should be added in the column names of the result table. For examples, suppose we have a data frame X: 
	| 'ID'   | 'name'  | 
	|--------|---------| 
	|    1   | 'Smith' | 
	|    2   | 'Wilson'|

  and we have another data frame  Y: 
	| 'ID'   | 'name'  | 
	|--------|---------| 
	|    1   | 'Alex'  | 
	|    2   | 'Bob'   | 
	|    3   | 'Tom'   | 
 Now in both data frames, we have a column called 'name'. After merging the two tables with k='ID'. The output should be: 
	| 'ID'   | 'name_x'|  'name_y'| 
	|--------|---------| ---------| 
	|    1   | 'Smith' |   'Alex' | 
	|    2   | 'Wilson'|   'Bob'  | . 
    ---- Inputs: --------
    * X: (Type: pd.DataFrame), a pandas dataframe.
    * Y: (Type: pd.DataFrame), a pandas dataframe.
    * k: (Type: str), a string indicating the name of a column in a data frame.
    ---- Outputs: --------
    * J: (Type: pd.DataFrame), the result pandas dataframe after joining two dataframes.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def merge(X:pd.DataFrame, Y:pd.DataFrame, k:str)->pd.DataFrame:
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    J = pd.merge(X, Y, on=k, how='inner')
    #########################################
    return J

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_2.py::test_merge
        (Mac /Linux): python3 -m pytest -v test_2.py::test_merge
---------------------------------------------------------------'''



''' ---------Function: sort_values (3 points)--------------------
    Goal: Given a dataframe X and a column (k), sort data records in descending order of the values in the column (k) . Suppose we have the following data frame X: 
	|'height'| 'width' | 
	|--------|---------| 
	|    1   |    6    | 
	|    2   |    4    | 
	|    3   |    5    | 
 If we want to sort the table with values in column k='height' in descending order, the output should be: 
	|'height'| 'width' | 
	|--------|---------| 
	|    3   |    5    | 
	|    2   |    4    | 
	|    1   |    6    | 
 If we want to sort the table with values in column k='width' in descending order, the output should be: 
	|'height'| 'width' | 
	|--------|---------| 
	|    1   |    6    | 
	|    3   |    5    | 
	|    2   |    4    |. 
    ---- Inputs: --------
    * X: (Type: pd.DataFrame), a pandas dataframe.
    * k: (Type: str), a string indicating the name of a column in a data frame.
    ---- Outputs: --------
    * Y: (Type: pd.DataFrame), a pandas dataframe.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def sort_values(X:pd.DataFrame, k:str)->pd.DataFrame:
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    Y = X.sort_values(by=k, ascending=False)
    #########################################
    return Y

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_2.py::test_sort_values
        (Mac /Linux): python3 -m pytest -v test_2.py::test_sort_values
---------------------------------------------------------------'''



''' ---------Function: divide (3 points)--------------------
    Goal: Given a dataframe X and two columns (k, l), create a pandas series, where each element is the value in column k divided by column l. Suppose we have the following data frame X: 
	|'height'| 'width' | 
	|--------|---------| 
	|    1   |    6    | 
	|    2   |    4    | 
	|    3   |    5    | 
 If we want to divide column k='width' by column l='height', the output should be a pandas series: 
	|   5/1   | 
	|   4/2   | 
	|   6/3   | 
 If we want to divide column k='height' by column l='width', the output should be a pandas series: 
	|  1/5   | 
	|  2/4   | 
	|  3/6   |. 
    ---- Inputs: --------
    * X: (Type: pd.DataFrame), a pandas dataframe.
    * k: (Type: str), a string indicating the name of a column in a data frame.
    * l: (Type: str), a string indicating the name of a column in a data frame.
    ---- Outputs: --------
    * y: (Type: pd.Series), a pandas series, which is a column of a dataframe.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def divide(X:pd.DataFrame, k:str, l:str)->pd.Series:
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    y = X[k] / X[l]
    #########################################
    return y

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_2.py::test_divide
        (Mac /Linux): python3 -m pytest -v test_2.py::test_divide
---------------------------------------------------------------'''



''' ---------Function: insert_column (3 points)--------------------
    Goal: Given a dataframe X, a pandas series y and a column name (k), create a new column in X as name k, insert the series y into the new column. Suppose we have the following data frame X: 
	|'height'| 'width' | 
	|--------|---------| 
	|    1   |    6    | 
	|    2   |    4    | 
	|    3   |    5    | 
 and a pandas series y: 
	|  10 | 
	|  20 | 
	|  30 | 
 If we want to insert the series y into X with a column name 'depth', the output should be a pandas series: 
	|'height'| 'width' | 'depth' | 
	|--------|---------|---------| 
	|    1   |    6    |   10    | 
	|    2   |    4    |   20    | 
	|    3   |    5    |   30    |. 
    ---- Inputs: --------
    * X: (Type: pd.DataFrame), a pandas dataframe.
    * y: (Type: pd.Series), a pandas series, which is a column of a dataframe.
    * k: (Type: str), a string indicating the name of a column in a data frame.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def insert_column(X:pd.DataFrame, y:pd.Series, k:str)->None:
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    X[k] = y
    #########################################
'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): python -m pytest -v test_2.py::test_insert_column
        (Mac /Linux): python3 -m pytest -v test_2.py::test_insert_column
---------------------------------------------------------------'''




'''---------- Static Type Checking (optional) ---------
Before running unit tests for this problem file, please consider using the static typing checker to check your code above. Using static typing can help catch type-related issues, which can save time and prevent bugs from reaching runtime. Static type checking examines function signatures and variable types to ensure they align as intended, reducing the likelihood of encountering unexpected type errors.
Please type the following command in your terminal to check types in this problem file:
        (Windows OS): python -m mypy --check-untyped-defs problem2.py
        (Mac /Linux): python3 -m mypy --check-untyped-defs problem2.py
Note: Type-checking is optional. It's only used for debuging. The errors in the type checking are NOT considered in the grading. So you coud ignore the type-checking errors. Only errors in the unit tests (in grading.py) are considered in the grading.
---------------------------------------------------'''
'''-------- TEST problem2.py file: (27 points) ----------
Please type the following command in your terminal to test the correctness of all the above functions in this file:
        (Windows OS): python -m pytest -v test_2.py
        (Mac /Linux): python3 -m pytest -v test_2.py
------------------------------------------------------'''





'''---------List of All Variables ---------------
* X: (Type: pd.DataFrame),  a pandas dataframe. 
* Y: (Type: pd.DataFrame),  a pandas dataframe. 
* y: (Type: pd.Series),  a pandas series, which is a column of a dataframe. 
* J: (Type: pd.DataFrame),  the result pandas dataframe after joining two dataframes. 
* filename: (Type: str),  the file name of a CSV file, a string. 
* k: (Type: str),  a string indicating the name of a column in a data frame. 
* l: (Type: str),  a string indicating the name of a column in a data frame. 
* s: (Type: int),  an integer scalar, the sum of the values in the column of the data frame. 
* v: (Type: list),  a list of values. 
* t: (Type: int),  an integer scalar, the threshold of the height. 
* Xt: (Type: pd.DataFrame),   the result dataframe, containing only the records with heights greater or equals to the threshold t. 
--------------------------------------------'''



