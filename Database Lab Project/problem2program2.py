#!/usr/local/bin/python3

A=open("25.txt", "r")
B=open("27.txt", "r")
C=open("bfile.dat", "w+")
noise=["the", "or", "and", "that", "not", "to", "is", "are", "were", "then", "thus", "therfore"]


for line in A:
    for word in line.split():
        if(word.lower() in noise ):
            continue
        else:
            print( word + " 1")
            C.write( word + " 25\n" )
    

for line in B:
    for word in line.split():
        if(word.lower() in noise ):
            continue
        else:
            print( word + " 2")
            C.write( word + " 27\n" )
