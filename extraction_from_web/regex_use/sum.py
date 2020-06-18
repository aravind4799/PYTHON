# program to find all integers from a text file and find its sum using regex
import re

new_list=[]
fh=open('data.txt',"r")
for line in fh:
    lst=re.findall('[0-9]+',line)
    for num in lst:
        new_list.append(int(num))

print(sum(new_list))
