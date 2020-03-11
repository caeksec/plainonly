# Import 
import os
import glob
import timeit
import sys
# Sort Data Section

# Timer VAR
start = timeit.default_timer()


def Temp():
    try:
         newFile = open("buffer.txt","w+") # Makes buffer for email and password if not already made
    except OSError as error:
        print(error)
        print("Program could not start correctly! Try running with sudo.")
    newFile.close() # Closes file
    print("Temp file Made!")
Temp()


def In():
    inFileUser = input("File to Sort: ")
    inFile = open(inFileUser,"r+") # Puts the input file into memory
    outTemp = open("buffer.txt","w+") # Puts the buffer file into memory
    for line in inFile:
        print(line.replace(":",";"),file=outTemp,end="") # Moves and filters : into ;      
    inFile.close() # Closes file		  # Also places into buffer
    outTemp.close() # Closes file
    print("Sorted Semi-colons!")
In()

def cleanUp():
    outTemp = open("buffer.txt","a+") # Puts the buffer file into memory
    for line in outTemp:
        print(line)
        print(line.replace("\r",""),file=outTemp,end="")
        print(line.replace("\n",""),file=outTemp,end="")
    outTemp.close() # Closes file
    print("Clean Up Done!")
cleanUp()

def Out():    
    outTemp = open("buffer.txt","r+") # Puts the buffer file into memory
    outFileUser = input("Output File: ")
    try:
        outFile = open(outFileUser,"w+") # Puts the output file into memory
    except OSError as error:
        print(error)
        print("File could not be created. Try running with sudo")
    for line in outTemp:
        print(line[line.index(";")+1:],file=outFile,end="") # Removes everything before the ; 
    outFile.close() # Closes file       		    # Also places into output
    outTemp.close() # Closes file
    print("Sorted Passwords!")
Out()

def removeTemp():
    os.remove("buffer.txt")
    print("Removed Temp Files!")
removeTemp()


print("Sorting Done!")

# Time it took for the Script to complete
stop = timeit.default_timer()
total_time = stop - start
mins, secs = divmod(total_time, 60)
hours, mins = divmod(mins, 60)
sys.stdout.write("Running for: %d:%d:%d.\n" % (hours, mins, secs))





