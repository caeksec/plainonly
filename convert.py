# Import 
import os
import glob
import timeit
import sys
import re
import threading
import time

# Styles 
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


# Timer VAR
start = timeit.default_timer()


def Temp():
    try:
         newFile = open("buffer.log","w+") # Makes buffer for email and password if not already made
    except OSError as error:
        print(error)
        print("Program could not start correctly! Try running with sudo.")
    newFile.close() # Closes file
    print(color.BOLD + color.CYAN + "[+] Making temporary file"+ color.END)
Temp()


def In():
    with open("buffer.log","w+") as outTemp: # Puts the buffer file into memory
        for filename in glob.glob('*.txt'): # Locates all .txt files in Current DIR
            with open(os.path.join(os.getcwd(), filename), 'r', encoding="ISO-8859-1") as f: # open in readonly mode
                In.fileSize = os.path.getsize("buffer.log")
                In.fileSize = int(In.fileSize)/1000
                In.fileSize = int(In.fileSize)/1000
                for line in f:
                    print(line.replace(":",";"),file=outTemp,end="")
                    sys.stdout.write("\r")
                    sys.stdout.write(color.BOLD + color.BLUE + "[#] Combining files: "+ color.END + str(In.fileSize)+ " MB")
                sys.stdout.flush()
    print("\r")           
    print(color.BOLD + color.CYAN +"[+] Files combined"+ color.END)         
In()

def cleanUp():
    with open("buffer.log","a+") as outTemp: # Puts the buffer file into memory
        for line in outTemp:
            print(line)
            print(line.replace("\r",""),file=outTemp,end="")
            print(line.replace("\n",""),file=outTemp,end="")
        print(color.BOLD + color.CYAN + "[+] Looking for bad chars" + color.END)
cleanUp()

def Out():    
    with open("buffer.log","r+") as outTemp: # Puts the buffer file into memory
        outFileUser = input(color.BOLD + color.YELLOW +"[!] Output File: "+ color.END)
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
        print(color.BOLD + color.CYAN +"[+] Removing emails" + color.END)
        fileSize2 = os.path.getsize(outFileUser)
        fileSize2 = int(fileSize2)/1000
        fileSize2 = int(fileSize2)/1000
        print(color.BOLD + color.BLUE + "[#] Sorted file: " + color.END + str(fileSize2) + " MB")
        perChange = -100 * (fileSize2 - In.fileSize) / In.fileSize
        print(color.BOLD + color.BLUE + "[#] Percentage decrease: " + color.END + str(round(perChange, 2)) + "%")
Out()

def removeTemp():
    os.remove("buffer.log")
    print(color.BOLD + color.CYAN +"[+] Cleaning up" + color.END)
removeTemp()


print(color.BOLD + color.YELLOW +"[!] Done" + color.END)

# Time it took for the Script to complete
stop = timeit.default_timer()
total_time = stop - start
mins, secs = divmod(total_time, 60)
hours, mins = divmod(mins, 60)
sys.stdout.write("Running for: %d:%d:%d \n" % (hours, mins, secs))





