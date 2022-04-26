'''
Created on: April 25, 2022
Author: SiddhantSingh-dev
'''

courses = []

courses.append((0.5, 1, 10, 10))
courses.append((1, 1, 10, 20, 30, 40))

for course in courses:
    course = (*course, 1, 1)
    print(course)
