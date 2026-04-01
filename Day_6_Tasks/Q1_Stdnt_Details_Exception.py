"""Develop a Python program to manage student marks for three subjects.
Store the subject names in a tuple, maintain unique student names in a set,and store each student’s marks in a list inside a dictionary
where the key is the student name.
Create user-defined functions to add a student with marks,
display all student records,
and calculate the average marks of a student.
Implement a recursive function to calculate the total marks from the list of marks.
The program should interact with the user through a simple menu.
Also include exception handling to handle ValueError (non-numeric marks input),
ZeroDivisionError (average calculation issues),
TypeError (incorrect data type in marks), and NameError (when a student name entered does not exist in the dictionary)."""


def sum_marks(marks):
    if not marks:
        return 0
    return marks[0]+sum_marks(marks[1:])

def std_details():

    std_names=set()
    sub_names=tuple(("Maths","Science","English"))
    std_marks={}

    while True:
        print("1. Add Student")
        print("2. Display Students")
        print("3. Calculate Average")
        print("4. Exit")
        choice=int(input("Enter your choice "))
        if choice==1:
            while len(std_names)<3:
                name=input("Enter Student name: ")
                if name not in std_names:
                    std_names.add(name)
                else:
                    print("Student name exist or you have eneterd 3 students already")
                    continue
                try:
                    m_marks=int(input(f"Enter {sub_names[0]} marks: "))
                    s_marks=int(input(f"Enter {sub_names[1]} marks: "))
                    e_marks=int(input(f"Enter {sub_names[2]} marks: "))

                    std_marks[name]=[m_marks,s_marks,e_marks]
                
                except ValueError:
                    print("Enter valid Number")
                    
        elif choice==2:
            if not std_marks:
                print("Student name not in List!")
            else:
                for name, marks in std_marks.items():
                    print(f"{name}:{marks}")
                    
        elif choice==3:
            name=input("Enter student name: ")
            if name not in std_marks:
                raise NameError("Name not in List")
            total=sum_marks(std_marks[name])
            avg=total/len(std_marks[name])
            print("Total: ",total,"\nAverage: ",avg)
                    
        elif choice==4:
            print("Exiting the program")
            break

std_details()
