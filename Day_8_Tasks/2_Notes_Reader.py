# 2. Notes Reader Program A student stores daily notes in a file called notes.txt. Write a program that opens the file, reads all the contents, and displays them on the screen.


f=open("Notes.txt","a")
note=input("Todays notes \n")
f.write(note + '\n')
f.close()

f=open("Notes.txt","r")
print(f.read())
f.close()
