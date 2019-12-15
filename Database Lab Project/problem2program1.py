#!/usr/local/bin/python3

A=open("25.txt", "r")
B=open("27.txt", "r")
C=open("output.txt", "w+")


for line in A:
    for word in line.split():
    
        C.write( word + " 25\n" )
    

for line in B:
    for word in line.split():

        C.write( word + " 27\n" )
