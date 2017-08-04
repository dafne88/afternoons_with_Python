import sys
import os

##########   WRITING FILE OUT   ##########

#open file to write and read
f = open('read_write.txt', 'w+')


for number in range(1, 10):
    #write number to file (with a new line)
    f.write("{0}\n".format(number))

#create a list of letters to output to our file
letters = ['a', 'b', 'c', 'd', 'e']

for letter in letters:
    #write letter to file (with a new line)
    f.write("{0}\n".format(letter))

f.seek(0)

for line in f:
    print("Line:{0}".format(line))


f.close()

with open("read_write.txt") as f, open("output.txt", "w") as g:
        for line in f:
                g.write(line)



