




#------------ No New Package --------------
# NOTE: Please don't import any new package. You should be able to solve the problems using only the package(s) imported here.
import numpy as np
#---------------------------------------------------------


# ---------------------------------------------------------
'''
    Goal of Problem 2: Linear Regression (Ridge Regression) (20 points)
    In this problem, we will solve a linear regression problem using ridge regression.
    A list of all variables being used in this problem is provided at the end of this file. 
'''
# ---------------------------------------------------------

''' ---------Function: least_square (10 points)--------------------
    Goal: (Linear Regression with Least Square Loss) Let's start with a simpler method (called 'Least Square'). Given a set of training samples (X) and their labels (y), train a linear model (with parameters w) on training samples using least-square regression. 
    ---- Inputs: --------
    * X: (Type: np.ndarray), the feature matrix of the training samples, a numpy matrix of shape n by p, where X[i] represents the p-dimensional feature vector for the i-th training sample in the training dataset.
    * y: (Type: np.ndarray), the labels, a numpy vector of length n, y[i] represents the label of the i-th training sample in the training dataset.
    ---- Outputs: --------
    * w: (Type: np.ndarray), the weights of the linear regression model, a numpy float vector of length p.
    ---- Hints: --------
    * You could use np.linalg.inv() to compute the inverse of a matrix. 
    * You could use @ operator in numpy for matrix multiplication: A@B represents the matrix multiplication between matrices A and B. 
    * You could use A.T to compute the transpose of matrix A. 
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def least_square(X:np.ndarray, y:np.ndarray)->np.ndarray:
    #########################################
    ## INSERT YOUR CODE HERE (10 points)
    
    #########################################
    return w

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_2.py::test_least_square
        (Mac /Linux): python3 -m pytest -v test_2.py::test_least_square
---------------------------------------------------------------'''



''' ---------Function: ridge_regression (10 points)--------------------
    Goal: (Ridge Regression) Now let's build the ridge regression by adding a regularization term to the least square loss.   Given a set of training samples (X) and their labels (y), train a linear model (with parameters w) on training samples using ridge regression (i.e., least square regression with L2 regularization). 
    ---- Inputs: --------
    * X: (Type: np.ndarray), the feature matrix of the training samples, a numpy matrix of shape n by p, where X[i] represents the p-dimensional feature vector for the i-th training sample in the training dataset.
    * y: (Type: np.ndarray), the labels, a numpy vector of length n, y[i] represents the label of the i-th training sample in the training dataset.
    * a: (Type: float), (alpha) the weight of the regularization term in ridge regression, a float scalar.
    ---- Outputs: --------
    * w: (Type: np.ndarray), the weights of the linear regression model, a numpy float vector of length p.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def ridge_regression(X:np.ndarray, y:np.ndarray, a:float=0.0001)->np.ndarray:
    #########################################
    ## INSERT YOUR CODE HERE (10 points)
    
    #########################################
    return w

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_2.py::test_ridge_regression
        (Mac /Linux): python3 -m pytest -v test_2.py::test_ridge_regression
---------------------------------------------------------------'''




'''---------- Static Type Checking (optional) ---------
Before running unit tests for this problem file, please consider using the static typing checker to check your code above. Using static typing can help catch type-related issues, which can save time and prevent bugs from reaching runtime. Static type checking examines function signatures and variable types to ensure they align as intended, reducing the likelihood of encountering unexpected type errors.
Please type the following command in your terminal to check types in this problem file:
        (Windows OS): py -m mypy --check-untyped-defs problem2.py
        (Mac /Linux): python3 -m mypy --check-untyped-defs problem2.py
Note: Type-checking is optional. It's only used for debuging. The errors in the type checking are NOT considered in the grading. So you coud ignore the type-checking errors. Only errors in the unit tests (in grading.py) are considered in the grading.
---------------------------------------------------'''
'''-------- TEST problem2.py file: (20 points) ----------
Please type the following command in your terminal to test the correctness of all the above functions in this file:
        (Windows OS): py -m pytest -v test_2.py
        (Mac /Linux): python3 -m pytest -v test_2.py
------------------------------------------------------'''





'''---------List of All Variables ---------------
* p: (Type: int),  the number of features of each data sample. 
* n: (Type: int),  the number of training samples in training data set. 
* X: (Type: np.ndarray),  the feature matrix of the training samples, a numpy matrix of shape n by p, where X[i] represents the p-dimensional feature vector for the i-th training sample in the training dataset. 
* y: (Type: np.ndarray),  the labels, a numpy vector of length n, y[i] represents the label of the i-th training sample in the training dataset. 
* w: (Type: np.ndarray),  the weights of the linear regression model, a numpy float vector of length p. 
* a: (Type: float),  (alpha) the weight of the regularization term in ridge regression, a float scalar. 
--------------------------------------------'''



