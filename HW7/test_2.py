from problem2 import *
import sys
import pytest 
import importlib.metadata 

import torch as th
from torch import nn
'''
    Unit test 2  (Total Points: 50)
    This file includes unit tests for problem2.py.
'''

def test_python_environment():
    assert sys.version_info[0]==3 # require python 3.11 or above 
    assert sys.version_info[1]>=11
    


# ============= Class: QK_DotProduct ===========================
# Total Points: 5.0
# ***********  Method: forward  (Class: QK_DotProduct) **************** 
# Total Points: 5.0

# ---- Test Case: shape1 (Method: forward, Class: QK_DotProduct) 
# Goal: Test if shape of the output tensor is correct
# Points: 1.0
@pytest.mark.QK_DotProduct_forward
def test_QK_DotProduct_forward_shape1():
    f = QK_DotProduct() # create the module/layer
    q = th.randn((2,2,4),requires_grad=True)
    k = th.randn( 2,2,4)
    y = f(q, k)
    assert y.size() == th.Size([2,2,2])
    y.sum().backward()
# --------------------------------

# ---- Test Case: shape2 (Method: forward, Class: QK_DotProduct) 
# Goal: Test if shape of the output tensor is correct
# Points: 1.0
@pytest.mark.QK_DotProduct_forward
def test_QK_DotProduct_forward_shape2():
    f = QK_DotProduct() # create the module/layer
    q = th.randn((3,4,5),requires_grad=True)
    k = th.randn(3,4,5)
    p = f(q, k)
    assert p.size() == th.Size([3,4,4])
    p.sum().backward()
# --------------------------------

# ---- Test Case: value (Method: forward, Class: QK_DotProduct) 
# Goal: Test if values of the output tensor are correct
# Points: 3.0
@pytest.mark.QK_DotProduct_forward
def test_QK_DotProduct_forward_value():
    f = QK_DotProduct()
    # Define query, key, and value tensors (batch_size=2, sequence_length=3, d_model=4)
    query = th.tensor([[[1.0, 2.0, 3.0, 4.0],
                        [2.0, 3.0, 4.0, 5.0],
                        [3.0, 4.0, 5.0, 6.0]],
                       [[-1.0, -2.0, -3.0, -4.0],
                        [-2.0, -3.0, -4.0, -5.0],
                        [-3.0, -4.0, -5.0, -6.0]]])
    key = th.tensor([[[0.1, 0.2, 0.3, 0.4],
                      [0.2, 0.3, 0.4, 0.5],
                      [0.3, 0.4, 0.5, 0.6]],
                     [[-0.1, -0.2, -0.3, -0.4],
                      [-0.2, -0.3, -0.4, -0.5],
                      [-0.3, -0.4, -0.5, -0.6]]])
    y = f(query, key)
    y_true = th.tensor([[[3,  4, 5  ],
                         [4,5.4, 6.8],
                         [5,6.8, 8.6]],
                        [[3, 4.0, 5  ],
                         [4, 5.4, 6.8],
                         [5, 6.8, 8.6]]])
    assert th.allclose(y,y_true)
# --------------------------------

# ============= Class: QK_ScaleDotProduct ===========================
# Total Points: 5.0
# ***********  Method: forward  (Class: QK_ScaleDotProduct) **************** 
# Total Points: 5.0

# ---- Test Case: shape1 (Method: forward, Class: QK_ScaleDotProduct) 
# Goal: Test if shape of the output tensor is correct
# Points: 1.0
@pytest.mark.QK_ScaleDotProduct_forward
def test_QK_ScaleDotProduct_forward_shape1():
    f = QK_ScaleDotProduct()
    p = th.randn((3,4,4),requires_grad=True)
    s = f(p, d_k=2)
    assert s.size() == th.Size([3,4,4])
    s.sum().backward()
# --------------------------------

# ---- Test Case: shape2 (Method: forward, Class: QK_ScaleDotProduct) 
# Goal: Test if shape of the output tensor is correct
# Points: 1.0
@pytest.mark.QK_ScaleDotProduct_forward
def test_QK_ScaleDotProduct_forward_shape2():
    f = QK_ScaleDotProduct() # create the module/layer
    p = th.randn((3,4,4),requires_grad=True)
    s = f(p, d_k=5)
    assert s.size() == th.Size([3,4,4])
    s.sum().backward()
# --------------------------------

# ---- Test Case: value1 (Method: forward, Class: QK_ScaleDotProduct) 
# Goal: Test if values of the output tensor are correct
# Points: 1.5
@pytest.mark.QK_ScaleDotProduct_forward
def test_QK_ScaleDotProduct_forward_value1():
    f = QK_ScaleDotProduct()
    p = th.tensor([[[3,  4, 5  ],
                    [4,5.4, 6.8],
                    [5,6.8, 8.6]],
                   [[3, 4.0, 5  ],
                    [4, 5.4, 6.8],
                    [5, 6.8, 8.6]]])
    s = f(p, d_k=4)
    s_true = th.tensor([[[1.5, 2.0, 2.5],
                         [2.0, 2.7, 3.4],
                         [2.5, 3.4, 4.3]],
                        [[1.5, 2.0, 2.5],
                         [2.0, 2.7, 3.4],
                         [2.5, 3.4, 4.3]]])
    assert th.allclose(s,s_true)
# --------------------------------

# ---- Test Case: value2 (Method: forward, Class: QK_ScaleDotProduct) 
# Goal: Test if values of the output tensor are correct
# Points: 1.5
@pytest.mark.QK_ScaleDotProduct_forward
def test_QK_ScaleDotProduct_forward_value2():
    f = QK_ScaleDotProduct()
    p = th.tensor([[[3,  4, 5  ],
                    [4,5.4, 6.8],
                    [5,6.8, 8.6]],
                   [[3, 4.0, 5  ],
                    [4, 5.4, 6.8],
                    [5, 6.8, 8.6]]])
    s = f(p, d_k=16)
    s_true = th.tensor([[[1.5, 2.0, 2.5],
                         [2.0, 2.7, 3.4],
                         [2.5, 3.4, 4.3]],
                        [[1.5, 2.0, 2.5],
                         [2.0, 2.7, 3.4],
                         [2.5, 3.4, 4.3]]])/2
    assert th.allclose(s,s_true)
# --------------------------------

# ============= Class: QK_SoftMax ===========================
# Total Points: 5.0
# ***********  Method: forward  (Class: QK_SoftMax) **************** 
# Total Points: 5.0

# ---- Test Case: shape1 (Method: forward, Class: QK_SoftMax) 
# Goal: Test if shape of the output tensor is correct
# Points: 1.0
@pytest.mark.QK_SoftMax_forward
def test_QK_SoftMax_forward_shape1():
    f = QK_SoftMax()
    s = th.randn((3,2,2),requires_grad=True)
    a = f(s)
    assert a.size() == th.Size([3,2,2])
    a.sum().backward()
# --------------------------------

# ---- Test Case: shape2 (Method: forward, Class: QK_SoftMax) 
# Goal: Test if shape of the output tensor is correct
# Points: 1.0
@pytest.mark.QK_SoftMax_forward
def test_QK_SoftMax_forward_shape2():
    f = QK_SoftMax()
    s = th.randn((2,4,4),requires_grad=True)
    a = f(s)
    assert a.size() == th.Size([2,4,4])
    a.sum().backward()
# --------------------------------

# ---- Test Case: value1 (Method: forward, Class: QK_SoftMax) 
# Goal: Test if values of the output tensor are correct (Batch size = 2, number of words in sequence = 2)
# Points: 1.5
@pytest.mark.QK_SoftMax_forward
def test_QK_SoftMax_forward_value1():
    f = QK_SoftMax()
    s = th.tensor([[[ 1., 1.],
                    [ 1., 3.] ],
                   [[ 1., 3.],
                    [-1.,-2.] ]] , requires_grad=True)
    a = f(s)
    assert a.size() == th.Size([2,2,2])
    assert th.allclose(a,th.tensor([[[0.5000, 0.5000],
                                     [0.1192, 0.8808]],
                                    [[0.1192, 0.8808],
                                     [0.7311, 0.2689]]]),atol= 0.01)
    a.sum().backward()
# --------------------------------

# ---- Test Case: value2 (Method: forward, Class: QK_SoftMax) 
# Goal: Test if values of the output tensor are correct
# Points: 1.5
@pytest.mark.QK_SoftMax_forward
def test_QK_SoftMax_forward_value2():
    f = QK_SoftMax()
    s = th.tensor([ [[ 1., 1., 1.], # batch_size = 2
                     [-2.,-2.,-2.],
                     [-1.,-1.,-1.]],
                    [[-3.,-3.,-3.],
                     [ 2., 2., 2.],
                     [-2.,-2.,-2.]]],requires_grad=True)
    a = f(s)
    assert a.size() == th.Size([2,3,3])
    assert th.allclose(a,th.ones(2,3,3)/3,atol= 0.01)
    a.sum().backward()
# --------------------------------

# ============= Class: QKV_Attention ===========================
# Total Points: 10.0
# ***********  Method: forward  (Class: QKV_Attention) **************** 
# Total Points: 10.0

# ---- Test Case: shape1 (Method: forward, Class: QKV_Attention) 
# Goal: Test if shape of the output tensor is correct
# Points: 2.0
@pytest.mark.QKV_Attention_forward
def test_QKV_Attention_forward_shape1():
    f = QKV_Attention()
    a = th.randn(3,2,2)
    v = th.randn((3,2,4),requires_grad=True)
    z = f(a, v)
    assert z.size() == th.Size([3,2,4])
    z.sum().backward()
# --------------------------------

# ---- Test Case: shape2 (Method: forward, Class: QKV_Attention) 
# Goal: Test if shape of the output tensor is correct
# Points: 2.0
@pytest.mark.QKV_Attention_forward
def test_QKV_Attention_forward_shape2():
    f = QKV_Attention()
    a = th.randn(5,3,3)
    v = th.randn((5,3,6),requires_grad=True)
    z = f(a, v)
    assert z.size() == th.Size([5,3,6])
    z.sum().backward()
# --------------------------------

# ---- Test Case: value1 (Method: forward, Class: QKV_Attention) 
# Goal: Test if the value of the output tensor is correct
# Points: 6.0
@pytest.mark.QKV_Attention_forward
def test_QKV_Attention_forward_value1():
    f = QKV_Attention()
    # batch_size = 2, number of words in the sequence = 3, number of features in value vectors= 4
    a = th.tensor([[[ 0.2,  0.2,  0.6], 
                    [ 0.3,  0.3,  0.4], 
                    [ 0.5,  0. ,  0.5]],
                   [[ 0. ,  0.5,  0.5], 
                    [ 0.4,  0.4,  0.2], 
                    [ 0.1,  0.0,  0.9]]])
    v = th.tensor([[[ 10.0,  20.0,  30.0,  20.0], 
                    [ 40.0,  50.0,  60.0,  50.0], 
                    [ 70.0,  80.0,  90.0,  80.0]],
                   [[-10.0, -20.0, -30.0, -20.0], 
                    [-40.0, -50.0, -60.0, -50.0], 
                    [-70.0, -80.0, -90.0, -80.0]]])
    z = f(a, v)
    print(z)
    z_true = th.tensor([[[ 52.,  62.,  72.,  62.],
                         [ 43.,  53.,  63.,  53.],
                         [ 40.,  50.,  60.,  50.]],
                        [[-55., -65., -75., -65.],
                         [-34., -44., -54., -44.],
                         [-64., -74., -84., -74.]]])
    assert th.allclose(z,z_true,atol=0.1)
# --------------------------------

# ============= Class: AttentionHead ===========================
# Total Points: 20.0

# ***********  Method: compute_qkv  (Class: AttentionHead) **************** 
# Total Points: 10.0

# ---- Test Case: shape (Method: compute_qkv, Class: AttentionHead) 
# Goal: Test if shape of the output tensor is correct
# Points: 2.0
@pytest.mark.AttentionHead_compute_qkv
def test_AttentionHead_compute_qkv_shape():
    f = AttentionHead(4,2)
    x = th.randn((3,5,4),requires_grad=True)
    q,k,v = f.compute_qkv(x)
    assert q.size() == th.Size([3,5,2])
    assert k.size() == th.Size([3,5,2])
    assert v.size() == th.Size([3,5,2])
    q.sum().backward()
# --------------------------------

# ---- Test Case: value (Method: compute_qkv, Class: AttentionHead) 
# Goal: Test if the values of the output tensor are correct
# Points: 8.0
@pytest.mark.AttentionHead_compute_qkv
def test_AttentionHead_compute_qkv_value():
    f = AttentionHead(4,2)
    # batch_size = 2, sequence_len=3, d_model = 4
    f = AttentionHead(3,2)
    x = th.tensor(
        [
            [
                [1,0,1,0],
                [0,1,0,1],
                [1,1,0,0]
            ],
            [
                [2,0,2,0],
                [0,2,0,2],
                [0,2,2,0]
            ]
        ]
    ).float()
    # d_model = 4, d_head = 2
    f.Wq=th.tensor(
        [
            [1,-1],
            [1,-1],
            [0, 0],
            [0, 0]
        ]
    ).float()
    f.Wk=th.tensor(
        [
            [0, 0],
            [0, 0],
            [1,-1],
            [1,-1]
        ]
    ).float()
    f.Wv=th.tensor(
        [
            [3,-2],
            [0, 0],
            [0, 0],
            [4,-1]
        ]
    ).float()
    q,k,v = f.compute_qkv(x)
    q_true = th.tensor([[[ 1., -1.],
                         [ 1., -1.],
                         [ 2., -2.]],
                        [[ 2., -2.],
                         [ 2., -2.],
                         [ 2., -2.]]])
    assert th.allclose(q,q_true)
    k_true = th.tensor([[[ 1., -1.],
                         [ 1., -1.],
                         [ 0.,  0.]],
                        [[ 2., -2.],
                         [ 2., -2.],
                         [ 2., -2.]]])
    assert th.allclose(k,k_true)
    v_true= th.tensor([[[ 3., -2.],
                        [ 4., -1.],
                        [ 3., -2.]],
                       [[ 6., -4.],
                        [ 8., -2.],
                        [ 0.,  0.]]])
    assert th.allclose(v,v_true)
# --------------------------------


# ***********  Method: forward  (Class: AttentionHead) **************** 
# Total Points: 10.0

# ---- Test Case: shape (Method: forward, Class: AttentionHead) 
# Goal: Test if shape of the output tensor is correct
# Points: 4.0
@pytest.mark.AttentionHead_forward
def test_AttentionHead_forward_shape():
    f = AttentionHead(4,2)
    x = th.randn((3,5,4),requires_grad=True)
    z = f(x)
    assert z.size() == th.Size([3,5,2])
    z.sum().backward()
# --------------------------------

# ---- Test Case: value (Method: forward, Class: AttentionHead) 
# Goal: Test if the values of the output tensor are correct
# Points: 6.0
@pytest.mark.AttentionHead_forward
def test_AttentionHead_forward_value():
    # batch_size = 2, sequence_len=3, d_model = 4
    f = AttentionHead(4,2)
    x = th.tensor(
        [
            [
                [1,0,1,0],
                [0,1,0,1],
                [1,1,0,0]
            ],
            [
                [2,0,2,0],
                [0,2,0,2],
                [0,2,2,0]
            ]
        ]
    ).float()
    # d_model = 4, d_k = 2
    f.Wq=th.tensor(
        [
            [1,-1],
            [1,-1],
            [0, 0],
            [0, 0]
        ]
    ).float()
    f.Wk=th.tensor(
        [
            [0, 0],
            [0, 0],
            [1,-1],
            [1,-1]
        ]
    ).float()
    f.Wv=th.tensor(
        [
            [3,-2],
            [0, 0],
            [0, 0],
            [4,-1]
        ]
    ).float()
    z = f(x)
    z_true= th.tensor([[[ 3.4458, -1.5542],
                        [ 3.4458, -1.5542],
                        [ 3.4856, -1.5144]],
                       [[ 4.6667, -2.0000],
                        [ 4.6667, -2.0000],
                        [ 4.6667, -2.0000]]])
    assert th.allclose(z,z_true,atol=0.01)
# --------------------------------

# ============= Class: ResidualLayer ===========================
# Total Points: 5.0

# ***********  Method: forward  (Class: ResidualLayer) **************** 
# Total Points: 5.0

# ---- Test Case: shape (Method: forward, Class: ResidualLayer) 
# Goal: Test if shape of the output tensor is correct
# Points: 5.0
@pytest.mark.ResidualLayer_forward
def test_ResidualLayer_forward_shape():
    f =  nn.Linear(2,2)
    r = ResidualLayer(f)
    x = th.tensor([ [1.,3.], # batch_size = 3
                    [3.,5.], # feature_dim = 2
                    [5.,7.]],requires_grad=True)
    y = r(x)
    fx= f(x)
    assert y.size() == th.Size([3,2])
    assert th.allclose(y, x+fx)
    y.sum().backward()
# --------------------------------


