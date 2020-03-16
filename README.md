# passHelper

ATM it's a bare bones script but it works as intended. It will convert any ':' to ';' when required  
It will only work with single ( raw text) files currently. 

## Why I wrote this script
Looking around the internet there wasn't any python scripts that would do what I wanted, which was to just get the passwords from leaked databases.
After looking around the internet for about a week I found that these sort of scripts are no longer being maintained, so why don't I learn some python and make it myself! 
So begain my journey into python formating and syntax ;_;


## Usage
```
python3 convert.py
```
It will ask you for an ```input``` file and then an ```output``` file. Be sure to run this as ```sudo``` otherwise you might get some errors. 

## TODO (Highest to Lowest priority)
```FIX combiner to work with multiple files
ADD support for multiple files to be analyzed 
ADD support for files in a dir to be analyzed 
ADD support for the combiner to combine multiple files into one file (without breaking)
Optimize the script for larger files. 
ADD support for other file formates. csv, zip, tar
Redo the script to be able to choose which to output. 1) Emails, 2) Passwords
```
