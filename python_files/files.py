

fname=open("file_name",'r' or 'w')

#here fname is called file handler
#it holds sequence of strings in the given file.

for line in fname:
    line=line.rstrip()#strips of the space and new line in file to avoid 2 \n which occurs while printing..try to run it removing this files
    if not line.startswith("abcd:"): continue
    print(line)

# QUESTION:
#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# solution:

fname = input("Enter file name: ")
fh = open(fname)
count=0
ans=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count=count+1
    x=line.find(":")
    y=float(line[x+2:])
    ans=ans+y


print("Average spam confidence: "+str(ans/count))


##########################################################################################################

how to read entire file as a single string?


fname=open("files")
x=fname.read()
now x variable has entire file contents as a single string
print(len(x))
print(x[20:])#prints first 20 characters from the file

########################################################################################################

how to handle invalid file names?

try:
    fname=open("abc.txt")
except:
    print("name doesnt exist")
    quit()
# rest of the code

#########################################################################################################
