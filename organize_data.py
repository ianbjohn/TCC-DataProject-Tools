#!/usr/bin/python3

#Takes raw data from PIEthon (Just a list of events and when they happen) and outputs it in a much more organized fashion (For each data, how many events happened)

import sys
#from io import open  #Seems hacky, but test without it, the machine I'm currently working on might just have python2 installed or something
import numpy as np


def main():
    days_of_month = np.array([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]) #Used to prevent outputting dates that don't exist

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
    for line in file:
        #Parse the 4 values on the line
        line = line.split(',')
    
        if line_count == 0:
            #ignore the first line
            line_count += 1
            continue
        elif line_count == 1:
            #fetch the year
            year = line[1]
            line_count += 1
        
        #Use them as indices for the 2D array, increment that cell. Add the current sum to the accumulation array
        data_array[int(line[2]) - 1, int(line[3]) - 1] += 1
        
    #traverse our data array and get the integral / accumulation of data
    sum = 0
    for i in range(0, 12):
        for j in range(0, 31):
            sum += data_array[i, j]
            accum_array[i, j] = sum

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
    file.write("date,value,sum\n")
    for i in range(0, 12):
        for j in range(0, 31):
            #ignore dates that don't exist (such as february the 31st)
            if (j + 1) > days_of_month[i]:
                continue
        
            file.write(str(i + 1) + "/" + str(j + 1) + "/" + str(year) + "," + str(int(data_array[i, j])) + "," + str(int(accum_array[i, j])) + "\n")

    print("Output file written.")
    file.close()

    print("Success.")
    return 0
    
if __name__ == "__main__":
    main()
