
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
import random
from flask import Flask, render_template
from jinja2 import Template
app= Flask(__name__) # create an app for the website
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
    Read_and_Agree = True
    #*******************************************
    return Read_and_Agree
#--------------------------

# ---------------------------------------------------------
'''
    Goal of Problem 1: Getting familiar with flask package (25 points)
     In this problem, we will get familiar with the flask python package.  Flask is a library for website development in Python.  It provides fast, flexible, and easy website design framework.  We will use flask to build a simple website. You could read the tutorials for Flask: 
	 https://flask.palletsprojects.com/en/1.1.x/quickstart/.
    A list of all variables being used in this problem is provided at the end of this file. 
'''
# ---------------------------------------------------------

''' ---------Function: hello_page (5 points)--------------------
    Goal: (Hello World Page) In the first URL ('/'), let's create a simple page: when a user visited the homepage of our website, we just return a string 'Hello World!'. This is a static homepage, where the content of the webpage is always the same. 
    ---- Outputs: --------
    * webpage: (Type: str), a webpage returned to the user's browser when a user visits the URL, a string of plain text or html.
    ---- Hints: --------
    * When returning the webpage string, please make sure to return exactly the string "Hello World!", not "hello world" or "Hello, World!". 
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

@app.route("/")
def hello_page()->str:
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    webpage = "Hello World!"
    #########################################
    return webpage

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_1.py::test_hello_page
        (Mac /Linux): python3 -m pytest -v test_1.py::test_hello_page
---------------------------------------------------------------'''


'''---------- Demo -----------------
Please type the following command in your terminal to test the website that you have built:
        (Windows OS): py demo1.py
        (Mac /Linux): python3 demo1.py
The website will be hosted in your computer and you could copy the testing URL shown in the terminal to a web browser to use the website. Once it is done, you could terminate the web server by pressing Ctrl+C in the terminal.
-------------------------------------'''


''' ---------Function: rand_page (5 points)--------------------
    Goal: (Random Number Page) In the second URL ('/rand'), let's create a simple dynamic page and send each user some different data in the webpage: Each time when a user visits this page, randomly generate a float number (between 0 and 1) and return the string of the number back to the user. So when a user visit this page for multiple times, the user will see a different random number each time. 
    ---- Outputs: --------
    * webpage: (Type: str), a webpage returned to the user's browser when a user visits the URL, a string of plain text or html.
    ---- Hints: --------
    * The returned variable 'webpage' should be a string instead of a float viable. You could convert a float number into a string before returning the value. 
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

@app.route("/rand")
def rand_page()->str:
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    webpage = str(random.random())
    #########################################
    return webpage

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_1.py::test_rand_page
        (Mac /Linux): python3 -m pytest -v test_1.py::test_rand_page
---------------------------------------------------------------'''


'''---------- Demo -----------------
Please type the following command in your terminal to test the website that you have built:
        (Windows OS): py demo1.py
        (Mac /Linux): python3 demo1.py
Open the browser to visit the website with relative path "/rand".
-------------------------------------'''


''' ---------Function: vote (5 points)--------------------
    Goal: (Vote Page) In the third URL ('/vote/<ID>'), let's create a simple webpage for users to send data to the website host: Each time when a user visits this page with a number (ID) in the URL (for example, /vote/10), return a webpage with 'Thank you for voting <ID>' (for example, 'Thank you for voting 10'). 
    ---- Inputs: --------
    * ID: (Type: int), the ID of a user votes for, an integer scalar.
    ---- Outputs: --------
    * webpage: (Type: str), a webpage returned to the user's browser when a user visits the URL, a string of plain text or html.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

@app.route("/vote/<int:ID>")
def vote(ID:int)->str:
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    webpage = f"Thank you for voting {ID}"
    #########################################
    return webpage

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_1.py::test_vote
        (Mac /Linux): python3 -m pytest -v test_1.py::test_vote
---------------------------------------------------------------'''


'''---------- Demo -----------------
Please type the following command in your terminal to test the website that you have built:
        (Windows OS): py demo1.py
        (Mac /Linux): python3 demo1.py
Open the browser to visit the website with relative path "/vote/2".
-------------------------------------'''


''' ---------Function: create_template (3 points)--------------------
    Goal: (Template) Let's get familiar with how to use a template which can be used to render webpages. This is very useful when multiple webpages (string) share a same template with only minor differences. For example, in this question, let's create a jinja2 template that can be used to render webpages like 'Hello, <username>!' In this template, we could to use a variable named 'username' in the template. If the username ='Alex', when rendering this template, the returned webpage/string will be 'Hello, Alex!'; If the username = 'Bob', when rendering this template, the returned webpage/string will be 'Hello, Bob!'. 
    ---- Outputs: --------
    * t: (Type: Template), a jinja2 template, which can be used to render a dynamic webpage.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def create_template()->Template:
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    t = Template("Hello, {{ username }}!")
    #########################################
    return t

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_1.py::test_create_template
        (Mac /Linux): python3 -m pytest -v test_1.py::test_create_template
---------------------------------------------------------------'''



''' ---------Function: render (3 points)--------------------
    Goal: Given a flask template in a file (for example, 'Good morning, <username>!') with a variable for 'username' and render the tempalte with a given username to generate a webpage/string as the output. 
    ---- Inputs: --------
    * t: (Type: Template), a jinja2 template, which can be used to render a dynamic webpage.
    * username: (Type: str), a username string, for example, 'Alex' or 'Bob' .
    ---- Outputs: --------
    * webpage: (Type: str), a webpage returned to the user's browser when a user visits the URL, a string of plain text or html.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def render(t:Template, username:str)->str:
    #########################################
    ## INSERT YOUR CODE HERE (3 points)
    webpage = t.render(username=username)
    #########################################
    return webpage

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_1.py::test_render
        (Mac /Linux): python3 -m pytest -v test_1.py::test_render
---------------------------------------------------------------'''



''' ---------Function: render_file (4 points)--------------------
    Goal: Given a file containing a flask template (for example, 'Good morning, <username>!') with a variable for 'username', load the template from file and render the tempalte with a given username to generate a webpage/string as the output. 
    ---- Inputs: --------
    * filename: (Type: str), the filename of the template to be used for rendering webpage response, a string.
    * username: (Type: str), a username string, for example, 'Alex' or 'Bob' .
    ---- Outputs: --------
    * webpage: (Type: str), a webpage returned to the user's browser when a user visits the URL, a string of plain text or html.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def render_file(filename:str, username:str)->str:
    with app.app_context():
        pass
        #########################################
        ## INSERT YOUR CODE HERE (4 points)
        webpage = render_template(filename, username=username)
        #########################################
    return webpage

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_1.py::test_render_file
        (Mac /Linux): python3 -m pytest -v test_1.py::test_render_file
---------------------------------------------------------------'''




'''---------- Static Type Checking (optional) ---------
Before running unit tests for this problem file, please consider using the static typing checker to check your code above. Using static typing can help catch type-related issues, which can save time and prevent bugs from reaching runtime. Static type checking examines function signatures and variable types to ensure they align as intended, reducing the likelihood of encountering unexpected type errors.
Please type the following command in your terminal to check types in this problem file:
        (Windows OS): py -m mypy --check-untyped-defs problem1.py
        (Mac /Linux): python3 -m mypy --check-untyped-defs problem1.py
Note: Type-checking is optional. It's only used for debuging. The errors in the type checking are NOT considered in the grading. So you coud ignore the type-checking errors. Only errors in the unit tests (in grading.py) are considered in the grading.
---------------------------------------------------'''
'''-------- TEST problem1.py file: (25 points) ----------
Please type the following command in your terminal to test the correctness of all the above functions in this file:
        (Windows OS): py -m pytest -v test_1.py
        (Mac /Linux): python3 -m pytest -v test_1.py
------------------------------------------------------'''





'''---------List of All Variables ---------------
* webpage: (Type: str),  a webpage returned to the user's browser when a user visits the URL, a string of plain text or html. 
* ID: (Type: int),  the ID of a user votes for, an integer scalar. 
* filename: (Type: str),  the filename of the template to be used for rendering webpage response, a string. 
* t: (Type: Template),  a jinja2 template, which can be used to render a dynamic webpage. 
* username: (Type: str),  a username string, for example, 'Alex' or 'Bob' . 
--------------------------------------------'''



