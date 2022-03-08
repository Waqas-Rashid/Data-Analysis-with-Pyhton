# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main
import numpy as np

def calculate(x1,x2,x3,x4,x5,x6,x7,x8,x9 = None):
  if x9 is None:
    raise Exception ("List must contain nine numbers.")
  else:
   
    l = [x1,x2,x3,x4,x5,x6,x7,x8,x9]; #list of 9 integers
    print(l)
    arr = np.array(l);
    print(arr)
    newarr = arr.reshape(3,3)
    print(newarr)

    # calculating values of the dictionary
    # calculating mean values
    mean_axis1 =newarr.mean(axis=0) #axis =0 for colums
    mean_axis2 =newarr.mean(axis=1) #axis =1 for row
    flattened_mean = np.mean(newarr)  # whole array
    
    # variance calculation
    var_axis1 = newarr.var(axis=0) #axis =0 for colums
    var_axis2 =newarr.var(axis=1)  #axis =1 for row
    flattened_var = np.var(newarr) # whole array
    
    # standard deviation calculation
    std_axis1 = newarr.std(axis=0) #axis =0 for colums
    std_axis2 =newarr.std(axis=1)  #axis =1 for row
    flattened_std = np.std(newarr)  # whole array
    
    # max calculation
    max_axis1 = newarr.max(axis=0) #axis =0 for colums
    max_axis2 =newarr.max(axis=1)  #axis =1 for row
    flattened_max = np.max(newarr)  # whole array

    

    # min calculation
    min_axis1 = newarr.min(axis=0) #axis =0 for colums
    min_axis2 =newarr.min(axis=1)  #axis =1 for row
    flattened_min = np.min(newarr)  # whole array

    # sum calculation
    sum_axis1 = newarr.sum(axis=0) #axis =0 for colums
    sum_axis2 =newarr.sum(axis=1)  #axis =1 for row
    flattened_sum = np.sum(newarr)  # whole array

    # Dictionary formation
    Dic = {
    'mean': [mean_axis1, mean_axis2, flattened_mean],
    'variance': [var_axis1, var_axis2, flattened_var],
    'standard deviation': [std_axis1, std_axis2, flattened_std],
    'max': [max_axis1, max_axis2, flattened_max],
    'min': [min_axis1, min_axis2, flattened_min],
    'sum': [sum_axis1, sum_axis2, flattened_sum]
    }
    print(Dic) #axis =1 for row
    

  #mean = np.mean(newarr);
calculate(0,1,2,3,4,5,6,7,8)

#try:
 #   calculate(0,1,2,3,4,5,6,7,8)
  #  if calculate.count == 9:
   #     calculate(0,1,2,3,4,5,6,7,8)
#except TypeError:
 #   print("List must contain nine numbers.")
#calculate(0,1,2,3,4,5,6,7,8)

