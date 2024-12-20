
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: hw1_torch_intro.ipynb

import torch
### DO NOT CHANGE ANY CODE ABOVE THIS LINE IN THIS CELL ###
def diag_matrix(n, x):
    diag = torch.eye(n, dtype=torch.float32) * x
    return diag
    # TODO: complete this function, return a tensor with the shape n x n, and the values on the diagonal are all x, all other values are zero

import torch
### DO NOT CHANGE ANY CODE ABOVE THIS LINE IN THIS CELL ###
class LinearRegression:
    def __init__(self, fit_intercept=True):
        """
        @param fit_intercept: Whether to calculate the intercept for this model.
        If set to False, no intercept will be used in calculations (i.e. data is expected to be centered).
        """
        self.fit_intercept = fit_intercept
        self.theta = None

    def fit(self, X, Y):
        """
        @param X: X is a tensor with shape m x n. Every row of X represents the features of a data point.
        @param Y: Y is a 1d tensor with length n. Every value of Y is the target value.
        """
        m = X.shape[0]
        assert(m == Y.shape[0])
        # Add constant terms if set
        if self.fit_intercept:
            constants = torch.ones(size=(m, 1), dtype=X.dtype)
            new_X = torch.cat((X, constants), dim=1)
        else:
            new_X = X
        new_X_T = torch.t(new_X)
        # TODO: Complete the training of the linear regression model.
        New_X = torch.matmul(new_X_T, new_X)
        New_X = torch.inverse(New_X)
        New_X = torch.matmul(New_X,new_X_T)
        theta = torch.matmul(New_X,Y)
        self.theta = theta
        pass

    def predict(self, X):
        """
        @param X: X is a tensor with shape k x n
        @return: the Y you should return is a 1d tensor with length n
        """
        m = X.shape[0]
        # Add constant terms if set
        if self.fit_intercept:
            constants = torch.ones(size=(m, 1), dtype=X.dtype)
            new_X = torch.cat((X, constants), dim=1)
        else:
            new_X = X
        Y = torch.matmul(new_X,self.theta)
        # TODO: Complete this function to predict Y based on X.
        return Y
        pass

######################################################################
########## DON'T WRITE ANY CODE OUTSIDE THE CLASS! ###################
######## IF YOU WANT TO CALL OR TEST IT CREATE A NEW CELL ############
######################################################################

import torch
### DO NOT CHANGE ANY CODE ABOVE THIS LINE IN THIS CELL ###
def generate_non_linear_features(x):
    """
    @param x: 1d tensor with length n, every value represents a data point. Every data point has only one feature.
    @return: n x 3 tensor, every row of this matrix represents the new features of this data point. A data point x_k in x should have features [x_k, x_k^2, x_k^3]
    """
    # TODO: Complete this function.
    x1 = x **2
    x2 = x **3
    new_x = torch.stack((x,x1,x2))
    test = torch.reshape(new_x, (3,len(x))).t()
    return test
    pass