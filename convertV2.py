# Import 
from encodings import utf_8
from encodings.utf_8 import encode
import subprocess as subp
import timeit
import sys




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


def main():
    print(color.BOLD + color.GREEN +"[-] Running Collection Module"+ color.END)
    
    subp.run('cat *.txt > buffer.log', shell=True)
    print(color.BOLD + color.CYAN +"[+] Files combined"+ color.END)  
    
    output_filtered = input(color.BOLD + color.YELLOW +"[!] Filtered Output File: "+ color.END)
    filtered_file = open(output_filtered, "w+", encoding='utf_8', errors='ignore')

    # with open("buffer.log", "r+", encoding='utf_8', errors='ignore') as buff_file: # Puts the buffer file into memory
    #     for line in buff_file:
    #         print(line.replace(":",";"),file=buff_file,end="")

    with open("buffer.log", "r+", encoding='utf_8', errors='ignore') as buff_file: # Puts the buffer file into memory
        for line in buff_file:
            if (";") in line:
                print(line.split(';')[1],file=filtered_file,end="") # Removes everything before the ; 
            if (":") in line:
                print(line.split(':')[1],file=filtered_file,end="")
            else:
                pass
    filtered_file.close()

    print(color.BOLD + color.CYAN +"[+] Files filtered"+ color.END)
    print(color.BOLD + color.GREEN +"[-] Removing Buffer Files"+ color.END)      
    subp.run('rm buffer.log', shell=True)
    print(color.BOLD + color.RED +"[~] Done" + color.END)     


if __name__ == "__main__":
    main()
    # Time it took for the Script to complete
    stop = timeit.default_timer()
    total_time = stop - start
    mins, secs = divmod(total_time, 60)
    hours, mins = divmod(mins, 60)
    sys.stdout.write("Running for: %d:%d:%d \n" % (hours, mins, secs))