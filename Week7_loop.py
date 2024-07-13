# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the count, total and average. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

count = 0
total = 0.0

while True:
    i = input('Enter a number:')
    if i == 'done':
        break
    try:
        num = int(i)
        count = count+1
        total = total + num
    except:
        print('Enter a valid number')
        continue    
print('count:',count,'total:',total,'average:',total/count)