# 8.4 Open the file data.txt and read it line by line. For each line,
#split the line into a list of words using the split() method.
#The program should build a list of words.
#For each word on each line check to see if the word is already in the list and if not
#append it to the list. When the program completes,
#sort and print the resulting words in alphabetical order.

#fname = input("Enter file name: ")
fh = open("data.txt")
lst = []
for line in fh:
    line=line.rstrip()
    words_in_line=line.split()
    print(words_in_line)
    for word in words_in_line:
        print(word)
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
