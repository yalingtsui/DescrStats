'''
------------------------------------------------------------------------
This script defines a function DescrStat() that gives descriptive
statistics for a comma delimited text file of one variable in which the
data are in one column and each observation is a row.
------------------------------------------------------------------------
'''

# Import packages
import numpy as np


def DescrStat(datafile):
    
    ’’’
    --------------------------------------------------------------------
    This function prints and returns descriptive statistics on a comma-
    delimited text file of a single variable
    --------------------------------------------------------------------
    INPUTS:
    datafile = string, path of the data file to be used in the function
    
    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: None
    
    OBJECTS CREATED WITHIN FUNCTION:
    data = (N,) vector, data from datafile
    data_mean = scalar, mean of the data
    data_std = scalar >= 0, standard deviation of the data 
    data_var = scalar >= 0, variance of the data
    
    FILES CREATED BY THIS FUNCTION: None
        
    RETURNS: data_mean, data_std, data_var 
    --------------------------------------------------------------------
    ’’’
    data = np.loadtxt(datafile)
    data_mean = data.mean()
    data_std = data.std()
    data_var = data.var()
