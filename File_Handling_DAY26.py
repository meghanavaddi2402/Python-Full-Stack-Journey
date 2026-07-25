'''


=> FILE HANDLING :-
- File is an object that gives options like creating, updating
- Ways to open a file :-
1.open
- Syntax :-
            var = open('file_name','mode')
            ----
            ----
            close()
-Example :-
            
2.with(keyword)
- Syntax :-
            with open('file_name','mode') as var:
- Example :-
with open('doc.txt','r') as me:
    print(me.read())

-> Modes :-
r ----> Used to read the file, is file is not present it will rise error

w ----> Used to write the text inside the file and it will overwrite the text inside the file
        incase if the file is not present it will create a new file with given name
- Example:-
with open('doc.txt','w') as me:
    print(me.write("hello!!!\nHow are you...???"))

with open('demo.txt','w') as me:
    print(me.write("hello!!!\nHow are you...???"))

a ----> Used to add the text to last position of the file
- Example :-
with open('doc.txt','a') as me:
    print(me.write("I am good\nHow are you...???"))

x ----> Ued to create a new file by adding the text inside file, incase the file it will ries an error 
- Example :-
with open('doc.txt','x') as me:
    print(me.write("hello!!!\nHow are you...???"))  #FileExistsError: [Errno 17] File exists: 'doc.txt'

with open('document.txt','x') as me:
    print(me.write("hello!!!\nHow are you...???"))   #creates a file 'document' and writes

-> Functions :-

write() :-
This used to add text inside a file or update a file with newly added text
- Example :-
with open('doc.txt','w') as me:
    print(me.write("hello!!!\nHow are you...???"))
with open('doc.txt','a') as me:
    print(me.write("hello!!!\nHow are you...???"))

read() :-
Used to read file line-by-line, we can also specify the size 
- Example :-
with open('doc.txt','r') as me:
    print(me.read(10))

readline() :-
This function will read only one line at a time
-Example :-
with open('doc.txt','r') as me:
    print(me.readline())            #output:- hello!!!

readlines() :-
This function will read whole file and give it in list, each line is one index
-Example :-
with open('doc.txt','r') as me:
    print(me.readlines())            #output:- ['hello!!!\n', 'How are you...???hello!!!\n', 'How are you...???']

    
'''

