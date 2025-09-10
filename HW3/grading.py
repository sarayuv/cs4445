

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
    print('------- Problem 1 (15 points) --------')
    total_points = test_function(1, "test_load_webpages", 5,total_points)
    total_points = test_function(1, "test_count_word_frequency", 5,total_points)
    total_points = test_function(1, "test_rank_word_frequency", 5,total_points)
    

    


    if output_zip:
        file_submit.write('problem2.py') 
    print('------- Problem 2 (22 points) --------')
    total_points = test_function(2, "test_ndarray", 2,total_points)
    total_points = test_function(2, "test_float_array", 2,total_points)
    total_points = test_function(2, "test_get_shape", 2,total_points)
    total_points = test_function(2, "test_all_one_matrix", 2,total_points)
    total_points = test_function(2, "test_mat_sum", 3,total_points)
    total_points = test_function(2, "test_mat_scalar_multiplication", 3,total_points)
    total_points = test_function(2, "test_matrix_vector_multiplication", 3,total_points)
    total_points = test_function(2, "test_find_zeros", 3,total_points)
    total_points = test_function(2, "test_diag_mat", 2,total_points)
    

    


    if output_zip:
        file_submit.write('problem3.py') 
    print('------- Problem 3 (15 points) --------')
    total_points = test_function(3, "test_count_in_links", 5,total_points)
    total_points = test_function(3, "test_add_column_inlinks", 5,total_points)
    total_points = test_function(3, "test_rank_inlinks", 5,total_points)
    

    


    if output_zip:
        file_submit.write('problem4.py') 
    print('------- Problem 4 (48 points) --------')
    total_points = test_function(4, "test_count_out_links", 5,total_points)
    total_points = test_function(4, "test_remove_sink_nodes", 5,total_points)
    total_points = test_function(4, "test_compute_S", 5,total_points)
    total_points = test_function(4, "test_compute_G", 6,total_points)
    total_points = test_function(4, "test_random_walk_one_step", 6,total_points)
    total_points = test_function(4, "test_all_close", 5,total_points)
    total_points = test_function(4, "test_random_walk", 6,total_points)
    total_points = test_function(4, "test_add_column_pagerank", 5,total_points)
    total_points = test_function(4, "test_rank_pages", 5,total_points)
    

    if output_zip:
        file_submit.close()
    print('****************************')
    print(f'** Total Points: {round(total_points)} / 100  **')
    print('****************************')
    print('[HOW TO SUBMIT]: If you are good with this grade, you could submit your work in canvas. After running this grading script, a zip file named "submission.zip" was automatically generated in the same folder of this homework assignment on your computer. This zip file is the only file that you need to submit in canvas. Thanks!')
    return total_points


if __name__ == "__main__":
    test_all()
