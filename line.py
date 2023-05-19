import os

file='bin_data/encode_base.txt'
f=open(file,'r')
ff=f.readlines()
for line in ff:
    line=line.rstrip("\n")
    print