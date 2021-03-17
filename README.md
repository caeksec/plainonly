# Generate wordlists from database leaks!

<p align="center">
  <div>Because there are no other scripts that work </div> 
  <img width="536" height="266" src="https://i.imgur.com/NTf2PJ4.png">
</p>

## Why?
Looking around the internet there wasn't any python scripts that would do what I wanted, which was to just get the passwords from leaked databases.
After about a week I found that these sort of scripts are no longer being maintained, so why don't I learn some python and make it myself? Well the answer was because this was a questionable thing at best, hence why nothing is maintained.  


## Usage
```
python3 convert.py
```
1. Place the python script in the Folder containing all the .txt files. 
2. It will ask you for an an ```output``` file after filtering. If you are getting errors, be sure to run this as ```sudo```. 
3. It will automatically find and start to filter each file into a buffer.

## TODO (Highest to Lowest priority)
```
1. FIX combiner to work with multiple files ✔️
2. ADD support for multiple files to be analyzed ✔️
3. ADD support for files in a dir to be analyzed ✔️
3. ADD support for the combiner to combine multiple files into one file (without breaking) ✔️
4. Optimize the script for larger files. ✔️
5. ADD support for other file formates. csv, zip, tar | Maybe ⚠️ 
6. Redo the script to be able to choose which to output. 1) Emails, 2) Passwords| Maybe ⚠️
```
