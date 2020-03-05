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
        
    print("Input file opened.")
        
    #We'll assume that the user is smart enough to have typed a .csv file. Maybe add error handling eventually
    
    #set up our array (Organized by months and days of the month)
    data_array = np.zeros([12, 31])
    accum_array = np.zeros([12, 31])

    line_count = 0
    sum = 0
    for line in file:
        #Ignore first line
        if line_count == 0:
            line_count += 1
            continue
        
        #Parse the 3 values on the line
        line = line.split(',')
        
        #Use them as indices for the 2D array, increment that cell. Add the current sum to the accumulation array
        data_array[int(line[1]) - 1, int(line[2]) - 1] += 1
        sum += 1
        accum_array[int(line[1]) - 1, int(line[2]) - 1] = sum

    print("Input file read.")
    file.close()
    
    #Save array to a new .csv file (2nd argument)
    try:
        file = open(sys.argv[2], mode = "w", encoding = "utf-8")
    except IOError as e:
        print(e)
        return -1

    print("Output file opened.")

    #store our array values in the new .csv output file
    file.write("month,day,value,sum\n")
    for i in range(0, 12):
        for j in range(0, 31):
            file.write(str(i + 1) + "," + str(j + 1) + "," + str(int(data_array[i, j])) + "," + str(int(accum_array[i, j])) + "\n")

    print("Output file written.")
    file.close()

    print("Success.")
    return 0
    
if __name__ == "__main__":
    main()
