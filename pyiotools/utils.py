# Utilities
# Author: Andy Hunter

from IPython import get_ipython

def clear_var(): 
    get_ipython().magic('reset -sf')
    
def clear_console():
    get_ipython().magic('clear')