




#------------ No New Package --------------
# NOTE: Please don't import any new package. You should be able to solve the problems using only the package(s) imported here.
import torch as th
from model import CNN
#---------------------------------------------------------


# ---------------------------------------------------------
'''
    Goal of Problem 3: Convolutional Neural Network for Binary Image Classification (using PyTorch) (20 points)
    In this problem, we will implement a convolutional neural network (CNN) with three convolution layers with max pooling and ReLU activations, and one fully-connected layer at the end to predict the label. The classification task is that given an input gray-scale image, predict the binary label of the image (e.g., whether the image is the owner of the smartphone or not). The structure of the CNN has already been defined in the 'model.py', which is (Conv layer 1) -> ReLU -> maxpooling -> (Conv layer 2) -> ReLU -> maxpooling -> (Conv layer 3) -> ReLU -> maxpooling -> (Fully-connected layer)
.
    A list of all variables being used in this problem is provided at the end of this file. 
'''
# ---------------------------------------------------------

''' ---------Function: compute_z (5 points)--------------------
    Goal: (Forward Function 1) Given a convolutional neural network model (m) defined as in 'model.py' (CNN), please compute the linear logits z on a mini-batch of data samples x =[x1, x2, ... x_batch_size]. 
    ---- Inputs: --------
    * x: (Type: th.Tensor), a mini-batch of input gray-scale images, a float torch tensor of shape (n, 1, h, w), where x[i,0] is the i-th gray-scale image in the mini-batch.
    * m: (Type: th.nn.Module), a convolutional neural network model, which is defined in "model.py" (CNN), it includes the weights and biases in all layers.
    ---- Outputs: --------
    * z: (Type: th.Tensor), the linear logits of the last layer in CNN on a mini-batch of data samples, a float torch vector of length (n), where z[i,0] is the linear logit on the i-th data sample in the mini-batch.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_z(x:th.Tensor, m:th.nn.Module)->th.Tensor:
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    
    #########################################
    return z

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_3.py::test_compute_z
        (Mac /Linux): python3 -m pytest -v test_3.py::test_compute_z
---------------------------------------------------------------'''



''' ---------Function: compute_L (5 points)--------------------
    Goal: (Forward Function 2) Suppose we are given a convolutional neural network model and we have already computed the linear logits z on a mini-batch of training samples. Suppose the labels of the training samples are in y. Please compute the average cross-entropy loss of the logistic regression model on the mini-batch of training samples. In the mean time, please also connect the global gradients of the linear logits z (dL_dz) with the loss L correctly. 
    ---- Inputs: --------
    * z: (Type: th.Tensor), the linear logits of the last layer in CNN on a mini-batch of data samples, a float torch vector of length (n), where z[i,0] is the linear logit on the i-th data sample in the mini-batch.
    * y: (Type: th.Tensor), the binary labels of the images in a mini-batch, a torch integer vector of length n, where y[i,0] is the label of the i-th image in the mini-batch, which can be 0 or 1.
    ---- Outputs: --------
    * L: (Type: th.Tensor), the average binary cross entropy loss on a mini-batch of training samples, a torch float scalar.
    ---- Hints: --------
    * This problem can be solved using 1 line(s) of code. More lines are okay. ''' 

def compute_L(z:th.Tensor, y:th.Tensor)->th.Tensor:
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    
    #########################################
    return L

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_3.py::test_compute_L
        (Mac /Linux): python3 -m pytest -v test_3.py::test_compute_L
---------------------------------------------------------------'''



''' ---------Function: update_parameters (5 points)--------------------
    Goal: (Gradient Descent) Suppose we are given a convolutional neural network model and we have a mini-batch of training data samples (x,y).  Suppose we have already computed the global gradients of the average loss L w.r.t. the weights w and biases on the mini-batch of data samples. Assume that we have already created an optimizer for all the parameters. Please update the parameters using gradient descent. After the update, the global gradients of all parameters should be set to zero. 
    ---- Inputs: --------
    * optimizer: (Type: th.optim.Optimizer), a PyTorch optimizer (such as SGD, ADAM, RMSProp) to handle the gradient descent for parameters in the model (weights and bias).
    ---- Hints: --------
    * Although the parameters of the CNN model are NOT given explicitly in the input of this function, but we can assume that all the parameters are already properly configured in the optimizer. So the optimizer is configured to handle the parameters. 
    * This problem can be solved using 2 line(s) of code. More lines are okay. ''' 

def update_parameters(optimizer:th.optim.Optimizer)->None:
    #########################################
    ## INSERT YOUR CODE HERE (5 points)
    
    pass 
    #########################################
'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_3.py::test_update_parameters
        (Mac /Linux): python3 -m pytest -v test_3.py::test_update_parameters
---------------------------------------------------------------'''



''' ---------Function: train (5 points)--------------------
    Goal: (Training CNN) Given a training dataset X (features), Y (labels) in a data loader, train a convolutional neural network model using mini-batch stochastic gradient descent: iteratively update the parameters using the gradients on each mini-batch of data samples.  We repeat n_epoch passes over all the training samples. 
    ---- Inputs: --------
    * data_loader: (Type: th.utils.data.DataLoader), a PyTorch loader of a dataset.
    * alpha: (Type: float), the step-size parameter of gradient descent, a float scalar.
    * n_epoch: (Type: int), the number of passes to go through the training dataset in the training process, an integer scalar.
    ---- Outputs: --------
    * m: (Type: th.nn.Module), a convolutional neural network model, which is defined in "model.py" (CNN), it includes the weights and biases in all layers.
    ---- Hints: --------
    * Step 1 Forward pass: compute the linear logits z and loss L. 
    * Step 2 Back propagation: compute the gradients of parameters. 
    * Step 3 Gradient descent: update the parameters using gradient descent. 
    * This problem can be solved using 3 line(s) of code. More lines are okay. ''' 

def train(data_loader:th.utils.data.DataLoader, alpha:float=0.001, n_epoch:int=100)->th.nn.Module:
    m = CNN() # initialize the model
    optimizer = th.optim.SGD(m.parameters(), lr=alpha) # create an SGD optimizer
    for _ in range(n_epoch): # iterate through the dataset n_epoch times
        for mini_batch in data_loader: # iterate through the dataset, with one mini-batch of random training samples (x,y) at a time
            x=mini_batch[0] # the gray-scale images in a mini-batch
            y=mini_batch[1] # the labels of the images in a mini-batch
            #########################################
            ## INSERT YOUR CODE HERE (5 points)
    
            #########################################
    return m

'''---------- Test This Function -----------------
Please type the following command in your terminal to test the correctness of your code above:
        (Windows OS): py -m pytest -v test_3.py::test_train
        (Mac /Linux): python3 -m pytest -v test_3.py::test_train
---------------------------------------------------------------'''

''' 
    If you have passed the above test, the trained CNN model should have been saved into a file, named "cnn.pt"
    
'''

'''---------- Demo -----------------
Please type the following command in your terminal to run a demo of the face recognition method that you have built:
        (Windows OS): py demo.py
        (Mac /Linux): python3 demo.py
The website will be hosted in your computer and you could copy the testing URL shown in the terminal to a web browser to use the website. Once it is done, you could terminate the web server by pressing Ctrl+C in the terminal.
-------------------------------------'''



'''---------- Static Type Checking (optional) ---------
Before running unit tests for this problem file, please consider using the static typing checker to check your code above. Using static typing can help catch type-related issues, which can save time and prevent bugs from reaching runtime. Static type checking examines function signatures and variable types to ensure they align as intended, reducing the likelihood of encountering unexpected type errors.
Please type the following command in your terminal to check types in this problem file:
        (Windows OS): py -m mypy --check-untyped-defs problem3.py
        (Mac /Linux): python3 -m mypy --check-untyped-defs problem3.py
Note: Type-checking is optional. It's only used for debuging. The errors in the type checking are NOT considered in the grading. So you coud ignore the type-checking errors. Only errors in the unit tests (in grading.py) are considered in the grading.
---------------------------------------------------'''
'''-------- TEST problem3.py file: (20 points) ----------
Please type the following command in your terminal to test the correctness of all the above functions in this file:
        (Windows OS): py -m pytest -v test_3.py
        (Mac /Linux): python3 -m pytest -v test_3.py
------------------------------------------------------'''

'''---------- TEST ALL problem files in this HW assignment (100 points) ---------
 This is the last problem file in this homework assignment. 
Please type the following command in your terminal to test the correctness of all the problem files:
        (Windows OS): py -m pytest -v
        (Mac /Linux): python3 -m pytest -v
---------------------------------------------------'''

'''-------- Automatic Grading of This HW Assignment -------
Please type the following command in your terminal to compute your score of this HW assignment:
        (Windows OS): py grading.py
        (Mac /Linux): python3 grading.py
 The grading.py will run all the unit tests of this HW assignment and compute the scores you get. 
 For example, if your code for this HW can get 95 points, you will see this message at the end in the terminal
 ****************************
 ** Total Points: 95 / 100 ** (this is just an example, you need to run the grading.py to know your grade)
 ****************************

 NOTE: Due to the randomness of the test data and/or initialization of parameters, the results of the same unit test may vary in different runs. If your code could pass a test case with more than 80% probability, you won't lose points in that test case. If you lose points after the grading by the TA due to randomness of the testing, you could contact the TA to show that your code could pass that test case with more than 80% chance, and get the lost points back.

-------------------------------------------------
***   How to submit your work?  ***

After running the above grading script, a zip file named "submission.zip" will be created in the same folder of this homework assignment. Please upload this "submission.zip" file in canvas for your final submission. 
NOTE: Please only use the "submission.zip" generated by the grading script as your submision. Don't create a zip file yourself by including all the data files and folder structures in the zip. Because the TA will use an automatic script to grade all the submissions. The script requires all submissions to have a standard format and folder structure. If you create your own zip file, you may be using a different format or name in the submission, which may cause errors in the grading of your submission. Thanks a lot for your contribution to streamlining the grading of homework assignments.

 That's all! Great job! You did it!
----------------------------------------------------'''



'''---------List of All Variables ---------------
* n: (Type: int),  batch size, the number of images in a mini-batch, an integer scalar. 
* h: (Type: int),  the height of each input image, an integer scalar. 
* w: (Type: int),  the width of each input image, an integer scalar. 
* x: (Type: th.Tensor),  a mini-batch of input gray-scale images, a float torch tensor of shape (n, 1, h, w), where x[i,0] is the i-th gray-scale image in the mini-batch. 
* y: (Type: th.Tensor),  the binary labels of the images in a mini-batch, a torch integer vector of length n, where y[i,0] is the label of the i-th image in the mini-batch, which can be 0 or 1. 
* m: (Type: th.nn.Module),  a convolutional neural network model, which is defined in "model.py" (CNN), it includes the weights and biases in all layers. 
* z: (Type: th.Tensor),  the linear logits of the last layer in CNN on a mini-batch of data samples, a float torch vector of length (n), where z[i,0] is the linear logit on the i-th data sample in the mini-batch. 
* L: (Type: th.Tensor),  the average binary cross entropy loss on a mini-batch of training samples, a torch float scalar. 
* data_loader: (Type: th.utils.data.DataLoader),  a PyTorch loader of a dataset. 
* alpha: (Type: float),  the step-size parameter of gradient descent, a float scalar. 
* n_epoch: (Type: int),  the number of passes to go through the training dataset in the training process, an integer scalar. 
* optimizer: (Type: th.optim.Optimizer),  a PyTorch optimizer (such as SGD, ADAM, RMSProp) to handle the gradient descent for parameters in the model (weights and bias). 
--------------------------------------------'''



