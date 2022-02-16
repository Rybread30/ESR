import numpy as np 
import matplotlib.pyplot as plt
class Fitting(object):
    '''A class designed to take data and attempt to fit a best fit line

    Attributes
    ----------

    '''
    def __init__(self, x, *y, keys): 
        self.x = x
        self.y = {}
        if keys is not None:
            for i,j in enumerate(keys):
                self.y[j] = y[i]
        
        self.xname = None
        self.xunits = None
        self.yname = None
        self.yunits = None
        self.title = None
        self.legend = False
        self.size = None
    
    def get_x(self): return self.x
    def get_y(self, key): 
        index = self.keys[key]
        
    def add_y(self, key, y): 
        self.y[key] = y
    def update_x(self, x): 
        self.x = x
    def plot_info(self, xname=None, yname=None, xunits=None, yunits=None, title=None, legend=False, size=None): 
        '''A function designed to store plotting information
        '''
        self.xname=formats
        self.xunits=xunits
        self.yname=yname
        self.yunits=yunits
        self.title = title
        self.legend= legend
        self.size = size
        
    def plot(self, keys, linetype="", fitkey=None):
        if self.size is not None: 
            plt.figure(figsize = self.size)
        for key in keys
            plt.plot(x, y[key], linetype, label=key)
        
        if fitkey is not None:
            ##fitting will be done here

        # adds axis information 
        if self.xunits is not None: if self.xname is not None: plt.xlabel(self.xname+"["+xunits+"]")
        else: if self.xname is not None: plt.xlabel(self.xname)
        if self.yunits is not None: if self.yname is not None: plt.ylabel(self.yname+"["+yunits+"]")
        else: if self.yname is not None: plt.ylabel(self.yname)
        if self.legend: plt.legend()
        if title is not None: plt.title(self.title)
        