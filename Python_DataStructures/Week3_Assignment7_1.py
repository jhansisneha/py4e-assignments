#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below. You can download the sample data at http://www.pythonlearn.com/code/words.txt

filename = input('Enter filename:')
try:
    filehandle = open(filename)
except:
    print('Filename is not valid')
    quit()

fileString = filehandle.read()
#contents of file in uppercase
print(fileString.upper())

