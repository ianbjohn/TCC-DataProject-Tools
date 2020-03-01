#Quick test code to organize our csv data a bit better

import sys
import numpy as np


def main():
    if len(sys.argv) < 2:
        print("No filename detected.")
        return -1;

    try:
        file = open(sys.argv[1], "r", "utf-8")
    except IOError, e:
        print(e.strerr())
        return -1;
        
    #We'll assume that the user is smart enough to have typed a .csv file. Maybe add error handling eventually
    
    #set up our array
    data_array = np.array([12, 31])
    
    return 0
    
if __name__ == "__main__":
    main()