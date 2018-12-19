# Power of Hydrogen

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def funWithPlots():
    welcome_message = input("Hello! Want to integrate today?: ")
    if welcome_message in ['yes', 'YES', 'yEs', 'YES!', 'ya', 'yep','yas', 'Yes']:
        # Generating x data from given range
        a = float(input("Generating data. What is your lower bound?: "))
        b = float(input("Generating data. What is your upper bound?: "))
        # Setting up x data as numpy array
        x = np.arange(a, b+1)
        
