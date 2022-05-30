# Write a program to read through a file and print the contents
# of the file (line by line) all in upper case. Executing the program will
# look as follows:

fname = open('mbox-short.txt','r')
fdata = fname.read()
fupper = fdata.upper()
print(fupper)
fname.close()