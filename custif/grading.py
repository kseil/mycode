#!/usr/bin/env python

#What is the grade?


#run if/elif through all possible options for 0-100

def gradecheck():


    grade = int(input("What is the student's grade?"))

    if grade <= int(100) & grade >= int(90):
        print("A")
    elif grade <= int(89) & grade >= int(80):
        print("B")
    elif grade <= int(79) & grade >= int(70):
        print("C")
    elif grade <= int(69) & grade >= int(60):
        print("D")
    elif grade <= int(59) & grade >= int(0):
        print("F")
    else:
        print("Please put in a grade from 0-100")


gradecheck()

