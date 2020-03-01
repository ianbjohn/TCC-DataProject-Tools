#!/usr/bin/python3

#Quick test code to organize our csv data a bit better

import sys
from io import open  #Seems hacky, but test without it, the machine I'm currently working on might just have python2 installed or something
import numpy as np


def main():
    if len(sys.argv) < 2:
        print("No input filename detected.")
        return -1
    if len(sys.argv) < 3:
        print("No output filename detected.")
        return -1

    try:
        file = open(sys.argv[1], mode = "r", encoding = "utf-8")
    except IOError as e:
        print(e)
        return -1
        
    print("File Opened.");
        
    #We'll assume that the user is smart enough to have typed a .csv file. Maybe add error handling eventually
    
    #set up our array
    data_array = np.zeros([12, 31])
    
    for line in file:
        #Ignore first line
        #Parse the 3 values on the line
        #Use them as indices for the 2D array, increment that cell
        print(line)
    
    print("Success.");
    
    file.close()
    
    #Save array to a new .csv file (Maybe 2nd argument)
    
    return 0
    
if __name__ == "__main__":
    main()
