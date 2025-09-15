

import pytest
import zipfile  
from pytest import ExitCode

#------------------------------------------
# AutoGrading of HW assignment
# How to run?  In the terminal, type:
#  (Windows OS) python grading.py
#  (Mac OS & Linux) python3 grading.py
#------------------------------------------

#------------------------------------------
# run one test
def test_function(pid,name, point,total_points):
    result = pytest.main(["--no-header","--tb=no",f"test_{pid}.py::{name}"])
    if result == ExitCode.OK:
        total_points += point
        print(f'*** Pass ({point} pt) --- {name}')
    else:
        print(f'*** Fail (0 / {point} pt) --- {name}')
    return total_points

#------------------------------------------
# test all tests
def test_all(output_zip=True):
    total_points = 0
    if output_zip:
        file_submit = zipfile.ZipFile('submission.zip','w')


    if output_zip:
        file_submit.write('problem1.py') 
    print('------- Problem 1 (60 points) --------')
    total_points = test_function(1, "test_compute_z", 5,total_points)
    total_points = test_function(1, "test_compute_dz_db", 5,total_points)
    total_points = test_function(1, "test_compute_dz_dw", 5,total_points)
    total_points = test_function(1, "test_compute_L", 5,total_points)
    total_points = test_function(1, "test_compute_dL_dz", 5,total_points)
    total_points = test_function(1, "test_compute_dL_db", 5,total_points)
    total_points = test_function(1, "test_compute_dL_dw", 5,total_points)
    total_points = test_function(1, "test_backward", 5,total_points)
    total_points = test_function(1, "test_update_b", 5,total_points)
    total_points = test_function(1, "test_update_w", 5,total_points)
    total_points = test_function(1, "test_train", 5,total_points)
    total_points = test_function(1, "test_predict", 5,total_points)
    

    


    if output_zip:
        file_submit.write('problem2.py') 
    print('------- Problem 2 (20 points) --------')
    total_points = test_function(2, "test_compute_z", 5,total_points)
    total_points = test_function(2, "test_compute_L", 5,total_points)
    total_points = test_function(2, "test_update_parameters", 5,total_points)
    total_points = test_function(2, "test_train", 5,total_points)
    

    


    if output_zip:
        file_submit.write('problem3.py') 
    print('------- Problem 3 (20 points) --------')
    total_points = test_function(3, "test_compute_z", 5,total_points)
    total_points = test_function(3, "test_compute_L", 5,total_points)
    total_points = test_function(3, "test_update_parameters", 5,total_points)
    total_points = test_function(3, "test_train", 5,total_points)
    

    if output_zip:
        file_submit.close()
    print('****************************')
    print(f'** Total Points: {round(total_points)} / 100  **')
    print('****************************')
    print('[HOW TO SUBMIT]: If you are good with this grade, you could submit your work in canvas. After running this grading script, a zip file named "submission.zip" was automatically generated in the same folder of this homework assignment on your computer. This zip file is the only file that you need to submit in canvas. Thanks!')
    return total_points


if __name__ == "__main__":
    test_all()
