#!/bin/python3
import sys
import math

def solve(grades):

    return_to = ""
    for grade in grades:
        new_grade = 0
        x = grade % 5
        if(grade >= 38 and 5-x < 3 and x != 0):
            new_grade = grade + 5 - x
            
            if (new_grade > 100):
                new_grade = 100

            print(str(new_grade))

        else:
            new_grade = grade
            print(str(new_grade))


point = int(input().strip())
grades = []
grades_i = 0

for grades_i in range(point):
   grades_t = int(input().strip())
   grades.append(grades_t)

result = solve(grades)
