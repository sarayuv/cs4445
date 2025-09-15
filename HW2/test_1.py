from problem1 import *
import sys
import math
import importlib.metadata 

'''
    Unit test 1:
    This file includes unit tests for problem1.py.
'''

#-------------------------------------------------------------------------
def test_python_environment():
    ''' ----------- Problem 1 (25 points in total)---------------------'''
    assert sys.version_info[0]==3 # require python 3.11 or above 
    assert sys.version_info[1]>=11
    installed_pkg = {pkg.name.lower() for pkg in importlib.metadata.distributions()}
    assert len(set(['pytest', 'mypy', 'flask', 'pandas', 'pandas-stubs']) - installed_pkg) ==0 # Check if any required package is missing. If missing, please follow the instructions at the begining of problem1.py to install the packages

#---------------------------------------------------
def test_hello_page():
    ''' (5 points) hello_page'''
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.data == b"Hello World!"
#---------------------------------------------------
def test_rand_page():
    ''' (5 points) rand_page'''
    c = app.test_client()
    response = c.get("/rand")
    assert response.status_code == 200
    a =float(response.data)
    assert a<=1 and a>=0 # the number should be between 0 and 1
    response = c.get("/rand")
    assert response.status_code == 200
    b =float(response.data)
    assert b<=1 and b>=0
    assert a != b # the two visits/users should see different random numbers
#---------------------------------------------------
def test_vote():
    ''' (5 points) vote'''
    c = app.test_client()
    response = c.get("/vote/2")
    assert response.status_code == 200
    assert response.data==b"Thank you for voting 2"
    response = c.get("/vote/1")
    assert response.status_code == 200
    assert response.data==b"Thank you for voting 1"
#---------------------------------------------------
def test_create_template():
    ''' (3 points) create_template'''
    t=create_template()
    assert type(t)== Template
    assert t.render(username="Alex")== "Hello, Alex!"
    assert t.render(username="Bob")== "Hello, Bob!"
#---------------------------------------------------
def test_render():
    ''' (3 points) render'''
    t=Template("Good morning, {{username}}!")
    assert render(t,"Alex")== "Good morning, Alex!"
    assert render(t,"Bob")== "Good morning, Bob!"
    t=Template("Good afternoon, {{username}}!")
    assert render(t,"Alex")== "Good afternoon, Alex!"
    assert render(t,"Bob")== "Good afternoon, Bob!"
#---------------------------------------------------
def test_render_file():
    ''' (4 points) render_file'''
    assert render_file("A.html","Alex")== "Good morning, Alex!"
    assert render_file("A.html","Bob")== "Good morning, Bob!"
    assert render_file("B.html","Alex")== "Good afternoon, Alex!"
    assert render_file("B.html","Bob")== "Good afternoon, Bob!"

