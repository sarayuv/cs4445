
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
import numpy as np
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
    Goal of Problem 1: Getting Familiar with NumPy Package (30 points)
    In this problem, we will continue to get familiar with numpy package. Specially, we will learn about the matrix operations in linear algebra
.
    A list of all variables being used in this problem is provided at the end of this file. 
'''
# ---------------------------------------------------------

''' ---------Function: transpose (3 points)--------------------
    Goal:  Given an input numpy matrix X, compute the transpose of the matrix X. For example X is 
	 1,2,3 
	 4,5,6 
	 Then the transpose of matrix X is 
	 1,4 
	 2,5 
	 3,6. 
    ---- Inputs: --------
    * X: (Type: np.ndarray), a numpy matrix (2D array).
    ---- Outputs: --------
    * Xt: (Type: np.ndarray), a numpy matrix (2D array), which is the transpose of matrix X .
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def transpose(X:np.ndarray)->np.ndarray:
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    
    #########################################
    return Xt

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_1.py::test_transpose
        (Mac /Linux): python3 -m pytest -v test_1.py::test_transpose
---------------------------------------------------------------'''



''' ---------Function: identity_matrix (3 points)--------------------
    Goal: Create an identity matrix of shape n X n, all the values in the matrix should be 0, except the diagonal elements (which should be 1). For example, an identity matrix of shape 3 X 3 will be 
	 1, 0, 0 
	 0, 1, 0 
	 0, 0, 1. 
    ---- Inputs: --------
    * n: (Type: int), an integer, the number of rows/columns in an identity matrix I.
    ---- Outputs: --------
    * I: (Type: np.ndarray), a numpy identity matrix of shape n X n, where all diagonal elements are 1s and off-diagonal elements are 0s.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def identity_matrix(n:int)->np.ndarray:
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    
    #########################################
    return I

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_1.py::test_identity_matrix
        (Mac /Linux): python3 -m pytest -v test_1.py::test_identity_matrix
---------------------------------------------------------------'''



''' ---------Function: matrix_multiplication (6 points)--------------------
    Goal: Given two matrices X (of shape r X k) and Y (k X c), compute the matrix multiplication between the matrix X and Y: Z = X Y 
 For example, if matrix X is: 
	 1, 2, 3 
	 4, 5, 6 
 and matrix Y is, 
	 -1, -4 
	 -2, -5 
	 -3, -6 
 then, ( Z = X Y) should be: 
	 -14, -32 
	 -32, -77 
	Here is how we calculated Z: 
	Z[0,0] =  1*(-1)+ 2*(-2) + 3*(-3) = -14 
	Z[0,1] =  1*(-4)+ 2*(-5) + 3*(-6) = -32 
	Z[1,0] =  4*(-1)+ 5*(-2) + 6*(-3) = -32 
	Z[1,1] =  4*(-4)+ 5*(-5) + 6*(-6) = -77 . 
    ---- Inputs: --------
    * X: (Type: np.ndarray), a numpy matrix (2D array).
    * Y: (Type: np.ndarray), a numpy matrix (2D array).
    ---- Outputs: --------
    * Z: (Type: np.ndarray), a numpy matrix (2D array), which is the result of the matrix multiplication of matrices X and Y.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def matrix_multiplication(X:np.ndarray, Y:np.ndarray)->np.ndarray:
    #########################################
    ## INSERT YOUR CODE HERE (6 points)
    
    #########################################
    return Z

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_1.py::test_matrix_multiplication
        (Mac /Linux): python3 -m pytest -v test_1.py::test_matrix_multiplication
---------------------------------------------------------------'''



''' ---------Function: matrix_inverse (6 points)--------------------
    Goal: Given a matrix X (of shape r X c), the compute the inverse matrix of X (called Xi), so that  X Xi = I (identity matrix) 
 For example, if matrix X is: 
	 2, 0 
	 0, 4 
 the inverse matrix Xi of X is, 
	 1/2,  0 
	  0 , 1/4 
 So, when we compute the matrix multiplication X Xi, we get an identity matrix I: 
	  1, 0 
	  0, 1 
 For example, if matrix X is: 
	 1, 2 
	 3, 4 
 the inverse matrix Xi of X is, 
	  -2,  1 
	 3/2,-1/2 
 So, when we compute the matrix multiplication (X * Xi = I), we get an identity matrix I: 
	  1, 0 
	  0, 1 . 
    ---- Inputs: --------
    * X: (Type: np.ndarray), a numpy matrix (2D array).
    ---- Outputs: --------
    * Xi: (Type: np.ndarray), a numpy matrix (2D array), which is the inverse of matrix X.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def matrix_inverse(X:np.ndarray)->np.ndarray:
    #########################################
    ## INSERT YOUR CODE HERE (6 points)
    
    #########################################
    return Xi

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_1.py::test_matrix_inverse
        (Mac /Linux): python3 -m pytest -v test_1.py::test_matrix_inverse
---------------------------------------------------------------'''



''' ---------Function: is_missing (3 points)--------------------
    Goal:  Given an input numpy array x (with missing values), compute a boolean array indicating the locations of the missing values. 
	 For example, x = [1,2,?,3,?] 
	 Here ? represents a missing value (np.nan) 
	 Then output m should be 
	 m= [False, False, True, False, True] 
	 Which means that the 3rd and 5th elements are missing (True), while all the other elements are not missing (False). 
    ---- Inputs: --------
    * x: (Type: np.ndarray), a numpy vector (with missing values), x[i] = np.nan if the i-th element of x is missing.
    ---- Outputs: --------
    * m: (Type: np.ndarray), a numpy boolean vector, where each element is True/False.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def is_missing(x:np.ndarray)->np.ndarray:
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    
    #########################################
    return m

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_1.py::test_is_missing
        (Mac /Linux): python3 -m pytest -v test_1.py::test_is_missing
---------------------------------------------------------------'''



''' ---------Function: inverse (3 points)--------------------
    Goal:  Given an input boolean array (m), compute the inverse of the boolean array (m_). 
	 For example, if m= [False, False, True, False, True], 
	 The inverse of m will be: 
	 m_ = [True, True, False, True, False]. 
    ---- Inputs: --------
    * m: (Type: np.ndarray), a numpy boolean vector, where each element is True/False.
    ---- Outputs: --------
    * m_: (Type: np.ndarray), a numpy boolean vector, which is the inverse of vector m, m_[i] = False if m[i]=True.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def inverse(m:np.ndarray)->np.ndarray:
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    
    #########################################
    return m_

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_1.py::test_inverse
        (Mac /Linux): python3 -m pytest -v test_1.py::test_inverse
---------------------------------------------------------------'''



''' ---------Function: subset_vector (3 points)--------------------
    Goal:  Given an input numpy vector x and a boolean vector (m) of the same length as x, extract the subset of elements in x indexed by m (where the elements to be used are True in m, the elements to be discarded are False in m). 
	 For example, x = [1,2,3,4,5] and m = [True, True, False, True, False] 
	 Then the subset of the vector x indexed by m will be 
	 x_m= [1,2,4] 
	 For example, x = [1,2,3,4,5] and m = [True, False, False, False, True] 
	 Then the subset of the vector x indexed by m will be 
	 x_m= [1,5]. 
    ---- Inputs: --------
    * x: (Type: np.ndarray), a numpy vector (with missing values), x[i] = np.nan if the i-th element of x is missing.
    * m: (Type: np.ndarray), a numpy boolean vector, where each element is True/False.
    ---- Outputs: --------
    * x_m: (Type: np.ndarray), a numpy vector, which is a subset of vector x indexed by m.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def subset_vector(x:np.ndarray, m:np.ndarray)->np.ndarray:
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    
    #########################################
    return x_m

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_1.py::test_subset_vector
        (Mac /Linux): python3 -m pytest -v test_1.py::test_subset_vector
---------------------------------------------------------------'''



''' ---------Function: subset_matrix (3 points)--------------------
    Goal:  Given an input numpy matrix X and a boolean vector (m), extract the subset matrix in X indexed by m (where the rows of X to be used are True in m, the rows of X to be discarded are False in m). 
	 For example, X = [[1,2], 
	                   [3,4], 
	                   [5,6]] 
	 The index vector m = [True, False, True], then the sub-matrix will be (keeping the 1st and 3rd rows of the matrix X) 
	 X_m= [[1,2], 
	       [5,6]] 
	 If the index vector m = [False, True, True], then the sub-matrix will be (keeping the 2nd and 3rd rows of the matrix X) 
	 X_m= [[3,4], 
	       [5,6]] . 
    ---- Inputs: --------
    * X: (Type: np.ndarray), a numpy matrix (2D array).
    * m: (Type: np.ndarray), a numpy boolean vector, where each element is True/False.
    ---- Outputs: --------
    * X_m: (Type: np.ndarray), a numpy matrix, which is a subset of matrix X indexed by m.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def subset_matrix(X:np.ndarray, m:np.ndarray)->np.ndarray:
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    
    #########################################
    return X_m

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_1.py::test_subset_matrix
        (Mac /Linux): python3 -m pytest -v test_1.py::test_subset_matrix
---------------------------------------------------------------'''




'''---------- Static Type Checking (optional) ---------
Before running unit tests for this problem file, please consider using the static typing checker to check your code above. Using static typing can help catch type-related issues, which can save time and prevent bugs from reaching runtime. Static type checking examines function signatures and variable types to ensure they align as intended, reducing the likelihood of encountering unexpected type errors.
Please type the following command in your terminal to check types in this problem file:
        (Windows OS): py -m mypy --check-untyped-defs problem1.py
        (Mac /Linux): python3 -m mypy --check-untyped-defs problem1.py
Note: Type-checking is optional. It's only used for debuging. The errors in the type checking are NOT considered in the grading. So you coud ignore the type-checking errors. Only errors in the unit tests (in grading.py) are considered in the grading.
---------------------------------------------------'''
'''-------- TEST problem1.py file: (30 points) ----------
Please type the following command in your terminal to test the correctness of all the above functions in this file:
        (Windows OS): py -m pytest -v test_1.py
        (Mac /Linux): python3 -m pytest -v test_1.py
------------------------------------------------------'''





'''---------List of All Variables ---------------
* X: (Type: np.ndarray),  a numpy matrix (2D array). 
* Y: (Type: np.ndarray),  a numpy matrix (2D array). 
* Z: (Type: np.ndarray),  a numpy matrix (2D array), which is the result of the matrix multiplication of matrices X and Y. 
* Xt: (Type: np.ndarray),  a numpy matrix (2D array), which is the transpose of matrix X . 
* Xi: (Type: np.ndarray),  a numpy matrix (2D array), which is the inverse of matrix X. 
* r: (Type: int),  an integer, the number of rows in the matrix X. 
* c: (Type: int),  an integer, the number of columns in the matrix. 
* I: (Type: np.ndarray),  a numpy identity matrix of shape n X n, where all diagonal elements are 1s and off-diagonal elements are 0s. 
* n: (Type: int),  an integer, the number of rows/columns in an identity matrix I. 
* k: (Type: int),  an integer, the number of columns in the matrix X. 
* x: (Type: np.ndarray),  a numpy vector (with missing values), x[i] = np.nan if the i-th element of x is missing. 
* m: (Type: np.ndarray),  a numpy boolean vector, where each element is True/False. 
* x_m: (Type: np.ndarray),  a numpy vector, which is a subset of vector x indexed by m. 
* m_: (Type: np.ndarray),  a numpy boolean vector, which is the inverse of vector m, m_[i] = False if m[i]=True. 
* X_m: (Type: np.ndarray),  a numpy matrix, which is a subset of matrix X indexed by m. 
--------------------------------------------'''



