# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

try:
    i = int(input("Enter a number:"))
    #print("i=",i)
except:
    print("Enter a valid number")
    quit()
max = -1
min = None
while i != 'done':
    #print("here")
    try:
        i = input("Enter a number again:")
        #print("i=",i)
        num = int(i)
        #print("num=",num)
        #smallest
        if min is None:
            min = num
        elif num < min:
            min = num
        #print("min:",min)   
        #largest
        if num > max:
            max = num
        #print("max:",max)     
    except: 
        #print("except i=",i)
        if(i!='done'):    
            print("Enter a valid number")
            continue            

print("Largest number is:",max)
print("Smallest number is:",min)
    