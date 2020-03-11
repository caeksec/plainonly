#include

#script
def multi_open(_list):
    out=""
    for x in _list:
        try:
            with open(x) as f:
                out+=f.read()
        except:
            pass
            # print(f"Cannot open file {x}")
    return(out)
fl = input("Files to combine: ")
combined = open("combined.txt", "w+")
print(multi_open(fl),file=combined)
print("Files combined!")
