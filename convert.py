# Import 
import os
import glob
import timeit
import sys
import re
import threading
import time
# Sort Data Section

# Timer VAR
start = timeit.default_timer()


def Temp():
    try:
         newFile = open("buffer.log","w+") # Makes buffer for email and password if not already made
    except OSError as error:
        print(error)
        print("Program could not start correctly! Try running with sudo.")
    newFile.close() # Closes file
    print("Temp file Made!")
Temp()


def In():
    with open("buffer.log","w+") as outTemp: # Puts the buffer file into memory
        for filename in glob.glob('*.txt'): # Locates all .txt files in Current DIR
            with open(os.path.join(os.getcwd(), filename), 'r', encoding="ISO-8859-1") as f: # open in readonly mode
                fileSize = os.path.getsize("buffer.log")
                for line in f:
                    print(line.replace(":",";"),file=outTemp,end="")
                    sys.stdout.write("\r")
                sys.stdout.write("Total File Size: " + str(fileSize))
                sys.stdout.flush()
    print("\n")           
    print("Sorted Semi-colons!")           
In()

def cleanUp():
    with open("buffer.log","a+") as outTemp: # Puts the buffer file into memory
        for line in outTemp:
            print(line)
            print(line.replace("\r",""),file=outTemp,end="")
            print(line.replace("\n",""),file=outTemp,end="")
        print("Clean Up Done!")
cleanUp()

def Out():    
    with open("buffer.log","r+") as outTemp: # Puts the buffer file into memory
        outFileUser = input("Output File: ")
        try:
            outFile = open(outFileUser,"w+") # Puts the output file into memory
        except OSError as error:
            print(error)
            print("File could not be created. Try running with sudo")
        for line in outTemp:
            if (";") in line:
                print(line.split(';')[1],file=outFile,end="") # Removes everything before the ; 
            else:
                pass
        print("Sorted Passwords!")
Out()

def removeTemp():
    os.remove("buffer.log")
    print("Removed Temp Files!")
removeTemp()


print("Sorting Done!")

# Time it took for the Script to complete
stop = timeit.default_timer()
total_time = stop - start
mins, secs = divmod(total_time, 60)
hours, mins = divmod(mins, 60)
sys.stdout.write("Running for: %d:%d:%d.\n" % (hours, mins, secs))





