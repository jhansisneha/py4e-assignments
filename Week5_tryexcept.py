astring = "Hello"
try:
    anumber = int(astring)
except:
    anumber = -1
print("Welcome", anumber) 
#anumber automatically typecasted to string (not sure if this is getting implicitly typecasted or being used as a number itself). However a number must be explicitly typecasted to a string if using + operator in print. See Week3_Repeating.
			
astring = "123"
try:
    anumber=int(astring)
except:
    anumber = -1
print("Hello", anumber)