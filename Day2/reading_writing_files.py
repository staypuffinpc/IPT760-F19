############ PURPOSE: Read and write a .txt file to python. Learn to ############
import os
## First, retrieve the file and store it in a variable ##
fileDir = os.path.dirname(os.path.realpath('__file__'))
fileName = os.path.abspath(os.path.join(fileDir,'../data/us_constitution.txt'))

#open the file, read it into a variable named 'constitution' as a single string and then close it ('with' will close the file)
with open(fileName,'r') as text:
    constitution = text.read().replace('\n','')

print(constitution)
    #possible modes (2nd argument))
        # r = read only
        # w = write mode.  Will overwrite existing info
        # a = append mode. Adds to the end of the file
        # r+ = read/write
        # x  open for exclusive creation.  Only works for NEW files
        # b = binary mode
        # t = text mode (Default)
