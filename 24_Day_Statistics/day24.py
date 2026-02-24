import numpy as np
print ('numpy:', np.__version__) # to know numpy version
print (dir(np)) # to know the different functions/ methods in numpy 

# creating int numpy array

# creating a python list
one_d_lst = [1,2,3,4,5]
print (type(one_d_lst))
two_d_lst = [[1,2,3],[4,5,6]]
print (one_d_lst,two_d_lst)
#creating numpy (numerical python) array from python list
numpy_arr_from_list = np.array(one_d_lst)
print (type(numpy_arr_from_list))
print (numpy_arr_from_list)
numpy_arr_from_list2 = np.array (two_d_lst)
print (type(numpy_arr_from_list2))
print (numpy_arr_from_list2)


# creating float numpy array
numpy_arr_from_list = np.array(one_d_lst,dtype = float)
print (type(numpy_arr_from_list))
print (numpy_arr_from_list)

# creating bool numpy array
numpy_bool_array = np.array([0,1,0,-1,2,0], dtype = bool)
print (type(numpy_bool_array))
print (numpy_bool_array)

# creating multi-dimentional numpy array
numpy_two_d_array = np.array (two_d_lst)
print (type(numpy_two_d_array))
print (numpy_two_d_array)

# converting numpy array to list
numpy_to_list = numpy_arr_from_list.tolist()
print (type(numpy_to_list))
print (numpy_to_list)

# creating numpy array from tuples
tup = (1,2,3,4,5)
print (type(tup))
print (tup)
numpy_tup_array = np.array(tup)
print (type (numpy_tup_array))
print (numpy_tup_array)

# shape of numpy array: it returns tuple, the first entry is the number of rows, and second entry is the number of columns. If the array is one dimentional, it returns the size of the array.
numpy_int_1d_array = np.array ([1,2,3,4,5])
print (type(numpy_int_1d_array))
print (numpy_int_1d_array.shape)
print (type(numpy_int_1d_array.shape))
numpy_int_2d_array = np.array ([[1,2,3],[4,5,6],[7,8,9]])
print (type(numpy_int_2d_array))
print (numpy_int_2d_array.shape)
numpy_int_2d_array = np.array ([[1,2,3],[7,8,9]])
print (type(numpy_int_2d_array))
print (numpy_int_2d_array.shape)

# data type of numpy array
one_d_int_list = [1,2,3,4,5]
numpy_int_1d_array = np.array(one_d_int_list)
numpy_float_1d_array = np.array(one_d_int_list, dtype=float)
print (one_d_int_list)
print (numpy_int_1d_array)
print (numpy_int_1d_array.dtype)
print (numpy_float_1d_array)
print (numpy_float_1d_array.dtype)

# size of numpy array: tells the number of elements in the array
np_int_1d_array = np.array([1,2,3,4,5])
print (np_int_1d_array.size)
np_int_2d_array = np.array([[1,2,3],[4,5,6]])
print (np_int_2d_array.size)


# MATHEMATICAL OPERATIONS USING NUMPY
# no need to loop through all the python list elements

# addition
numpy_array_from_list = np.array([1,2,3,4,5])
print (numpy_arr_from_list)
print (type(numpy_arr_from_list))
add_ten = numpy_array_from_list + 10
print (add_ten)
print (type(add_ten))

# subtraction
numpy_array_from_list = np.array([1,2,3,4,5])
print (numpy_arr_from_list)
print (type(numpy_arr_from_list))
sub_ten = numpy_array_from_list - 10
print (sub_ten)
print (type(sub_ten))

# multiplication
numpy_array_from_list = np.array([1,2,3,4,5])
print (numpy_arr_from_list)
print (type(numpy_arr_from_list))
mul_ten = numpy_array_from_list * 10
print (mul_ten)
print (type(mul_ten))

# division
numpy_array_from_list = np.array([1,2,3,4,5])
print (numpy_arr_from_list)
print (type(numpy_arr_from_list))
div_ten = numpy_array_from_list / 10
print (div_ten)
print (type(div_ten))

# modulus
numpy_array_from_list = np.array([1,2,3,4,5])
print (numpy_arr_from_list)
print (type(numpy_arr_from_list))
mod_ten = numpy_array_from_list % 10
print (mod_ten)
print (type(mod_ten))

# floor
numpy_array_from_list = np.array([1,2,3,4,5])
print (numpy_arr_from_list)
print (type(numpy_arr_from_list))
floor_ten = numpy_array_from_list // 10
print (floor_ten)
print (type(floor_ten))

# exponential
numpy_array_from_list = np.array([1,2,3,4,5])
print (numpy_arr_from_list)
print (type(numpy_arr_from_list))
exp_ten = numpy_array_from_list ** 2
print (exp_ten)
print (type(exp_ten))

# CONVERTING DATATYPE
# int to str
numpy_int_to_float = np.array([1,2,3,4,5], dtype= float)
print (numpy_int_to_float.astype('int').astype('str'))
print (type(numpy_int_to_float.astype('int').astype('str')))


# MULTI-DIMENTIONAL ARRAY
numpy_2d_array = np.array([[1,2,3],[4,5,6]])
print ("size: ",numpy_2d_array.size)
print ("shape: ",numpy_2d_array.shape)
print ("dtype",numpy_2d_array.dtype)

# getting items from 2d array
numpy_2d_array = np.array([[1,2,3],[4,5,6]])
print (type(numpy_2d_array))
first_row = numpy_2d_array[0]
print (first_row)
print (type(first_row))
second_row = numpy_2d_array[1]
print (second_row)
print (type(second_row))
first_column = numpy_2d_array[:,0]
print (first_column)
print (type(first_column))
second_column = numpy_2d_array[:,1]
print (second_column)
print (type(second_column))
third_column = numpy_2d_array[:,2]
print (third_column)
print (type(third_column))

# SLICING NUMPY ARRAY
numpy_2d_array = np.array ([[1,2,3],[4,5,6]])
first_2_rows_and_columns = numpy_2d_array [0:2,0:2]
print (first_2_rows_and_columns)

# reverse rows and column positions
print (numpy_2d_array[::-1,::-1])


# HOW TO REPRESENT MISSING VALUES
numpy_2d_array = np.array ([[1,2,3],[4,5,6]])
numpy_2d_array[0,1] = 44
numpy_2d_array[1,1] = 55
print (numpy_2d_array)
numpy_zeroes = np.zeros ((3,3), dtype = int, order = 'C')
numpy_ones = np.ones ((3,3), dtype = int, order = 'C')
numpy_twice = numpy_ones * 2
print (numpy_zeroes)
print (numpy_ones)
print (numpy_twice)

# reshaping the array
numpy_2d_array = np.array ([[1,2,3],[4,5,6]])
print (numpy_2d_array)
reshape_numpy_2d_array = numpy_2d_array.reshape(3,2)
print (reshape_numpy_2d_array)

# flattening the array
flattened_numpy_2d_array = reshape_numpy_2d_array.flatten()
print (flattened_numpy_2d_array)

# add two lists
np_1d_list1 = np.array([1,2,3])
np_1d_list2 = np.array([4,5,6])
print (np_1d_list1 + np_1d_list2)

#horizontal stacking
np_horizontal = np.hstack((np_1d_list1, np_1d_list2))
print (np_horizontal)

# vertical stacking
np_vertical = np.vstack((np_1d_list1, np_1d_list2))
print (np_vertical)
