#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method.The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.

filename = input('Enter filename:')
try:
    fhandle = open(filename)
except:
    print(filename, 'is not a valid filename')
    quit()

allwords = list()
for line in fhandle:
    line = line.strip()
    words = line.split()
    for word in words:
        if word not in allwords:
            allwords.append(word)

allwords.sort()
print(allwords)