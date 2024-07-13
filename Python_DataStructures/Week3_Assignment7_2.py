#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#        X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average
#of those values and produce an output as shown below.
#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when 
#you are testing below enter mbox-short.txt as the file name.

filename = input('Enter file name:')
try:
    filehandle = open(filename)
except:
    print('Filename is not valid')
    quit()

count=0
sum=0
for line in filehandle:
    line=line.rstrip()
    if 'X-DSPAM-Confidence:' in line:
        count = count+1
        findex = line.index(':')
        fnumber = float(line[findex+1:])
        #print(fnumber)
        sum = sum+fnumber
average = sum/count
print(average)