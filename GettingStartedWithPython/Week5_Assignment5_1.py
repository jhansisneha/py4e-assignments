#3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.

try:
    hours = int(input("Enter hours:"))
    rateperhour = float(input("Enter rate per hour:"))
except:
    print("Error, please enter numeric input")
    quit()   
    
#After except block executes, it will continue execution with the rest of the program. However if any variables are defined in try block and if the execution is failed in try block, then rest of the program may throw compilation error if the variables defined in the failed try block are used later in the program. In that case, if you want the program to stop executing after the except block executes, use quit() command.

print("this")
if hours <=40:
    pay = hours * rateperhour
else:
    pay = (40*rateperhour) + (hours-40) * rateperhour * 1.5
print("Pay is ", pay)