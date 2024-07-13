#__author__ = 'edwardlau'
#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008. Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. Note that the autograder does not have support for the sorted() function.

filename = input('Enter filename:')
try:
    fhandle = open(filename)
except:
    print(filename, 'entered is not valid.')
    quit()

hours = dict()
for line in fhandle:
    if line.startswith('From '):
        hourindex = line.index(':')-2
        hours[line[hourindex:hourindex+2]] = hours.get(line[hourindex:hourindex+2],0)+1

#print(sorted(hours.items(),reverse=True))        

hourlist=list()
for k,v in hours.items():
        hourlist.append((v,k))

hourlist=sorted(hourlist)
#print(hourlist)

sortedhourlist = list()
for v,k in hourlist:
        #print ('('+k+','+str(v)+')',end="")
        newtuple = (k,v)
        sortedhourlist.append(newtuple)


print(sortedhourlist)