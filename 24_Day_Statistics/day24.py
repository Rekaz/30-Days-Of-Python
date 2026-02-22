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

