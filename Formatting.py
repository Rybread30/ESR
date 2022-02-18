import numpy as np 

class Formatting(object):
    '''A class designed to import data from a text file and format it

    Attributes
    ----------

    '''
    def __init__(self, file_name, delimeter, data_range, coloumn_nums, coloumn_names, data_units=None, row_num=1, data_type=float, null_value=-10000):
        
        data_array = np.genfromtxt(file_name, # Gets the data from the file 
                       delimiter=delimeter, # Sets what seperates the values 
                       dtype=data_type, # Sets the type of the data
                       skip_header=row_num, # Sets how many rows are skipped 
                       filling_values=null_value) # Sets a value to fill empty values
        self.data={}
        self.data_units={}
        for i in coloumn_nums:
            name = coloumn_names[i]
            self.data[name] = data_array[:,i]
            if data_units is not None: 
                self.data_units[name] = data_units[i]
        print(file_name,"data has been saved")
        
    def update_units(self, key, scale, new_unit): 
        self.data[key] =  self.data[key]*scale
        self.data_units[key] = new_unit
        print(key, "has new unit", new_unit)
    
    def get_data(self, key): 
        return self.data[key], self.data_units[key]
    
    def get_all_data(self): 
        return self.data
    
    def add_data(self, data, key, data_units=None): 
        self.data[key] = data
        if data_units is not None: 
            self.data_units[key] = data_units