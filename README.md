# Generate wordlists from database leaks!

<p align="center">
  <img width="536" height="266" src="https://i.imgur.com/NTf2PJ4.png">
</p>

## Why?
Looking around the internet there wasn't any python scripts that would do what I wanted, which was to just get the passwords from leaked databases.

After about a week I found that these sort of scripts are no longer being maintained, so why don't I learn some python and make it myself? 

Well the answer was because this was a questionable thing at best, hence why nothing is maintained.  


## V1 Usage
```
python3 convert.py
```
1. Place the python script in the Folder containing all the .txt files. 
2. It will ask you for an an ```output``` file after filtering. If you are getting errors, be sure to run this as ```sudo```. 
3. It will automatically find and start to filter each file into a buffer.

## V2 Usage
```
pypy convertV2.py
```
V2 is optimised to use the builtin Linux command set.

As such, if you are using windows install cywin with linux command set (add it to PATH as well)

1. Same as V1

## De Dupe
rling is recommended for this due to its speed. 

It will need more RAM the bigger the input file however, so keep it < 5gig 

https://github.com/Cynosureprime/rling

### Usage
```
rling INFILE.txt OUTFILE.txt
```

