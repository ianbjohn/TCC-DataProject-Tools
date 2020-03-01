#Quick test code to organize our csv data a bit better

#! /usr/bin/python3

import sys
from io import open  #Seems hacky, but test without it, the machine I'm currently working on might just have python2 installed or something
import numpy as np


def main():
    if len(sys.argv) < 2:
        print("No filename detected.")
        return -1;

    try:
        file = open(sys.argv[1], mode = "r", encoding = "utf-8")
    except IOError as e:
        print(e)
        return -1;
        
    print("File Opened.\n");
        
    #We'll assume that the user is smart enough to have typed a .csv file. Maybe add error handling eventually
    
    #set up our array
    data_array = np.array([12, 31])
    
    file.close()
    
    return 0
    
if __name__ == "__main__":
    main()