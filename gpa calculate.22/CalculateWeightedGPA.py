'''
Created on: April 25, 2022
Author: SiddhantSingh-dev
Purpose: You gotta relish in the numbers ykwim?
'''

'''
Variables:
    1. Each course is assigned a grade value from 0 - 100
        a. Rank / GPA only counts for a grade value >= 70
    2. (~CT) Courses can be 1 credits, 2, credits, or 0.5 credits (semester classes like <= 2024 AP Physcology)
    3. (~LVL) Courses have a level: AP, on-level, PAP
    4. (~N) N number of courses
    
Notes:
    This calculator is meant to calculate the GPA of a student over the course of an entire year
    Inputs:
        1. ~LVL
        2. FORE(i, 0, ~N):
            3. ~CT
                a. ~CT == 1 || ~CT == 2
                    Quarter 1, Quarter 2, Quarter 3, Quarter 4
                b. ~CT == 0.5
                    Quarter 1, Quarter 2
    Output:
        1. Output cumulative GPA (weighted)
        2. Output cumulative GPA per class per semester (weighted)
            ie. AP Calc BC: S1 - 6.0; S2 - 6.0
    
Goals:
    1. Create a functioning GPA calculator
    2. Push this code to GitHub
    3. Eventually, create the 'hac v.sidd.22' application (hac alternative)
'''
def star_format(i):
    for _ in range(i):
        print('*' * 100)

def lvl_type(LVL):
    LVL = LVL.lower()
    if LVL == "ol":
        return 5.0
    elif LVL == "pap":
        return 5.5
    elif LVL == "ib" or LVL == "ap" or LVL == "cs3":
        return 6.0
    else: 
        return -1

def handle_invalid_input():
    print("Invalid Input, breaking program")
    star_format(5)

def main():
    # instance variables
    courses = []
    gpa = 0.0
    CT_sum = 0.0
    
    print("2022-23 FISD GPA Calculator (A terminal based application for GPA calculation)")
    N = int(input("Enter the number of courses you have taken:"))
    star_format(1)
    for i in range(N):
        print(f"Course #{i+1}: ")
        CT = float(input("\tEnter the number of credits for this course (0.5, 1, 2): "))
        if CT < 0.5 or CT > 2:
            handle_invalid_input()
            break
        LVL = lvl_type(input("\tCourse Level (on-level: OL; advanced: PAP; AP/IB: AP (or) IB (or) CS3): "))
        if LVL == -1:
            handle_invalid_input()
            break
        if CT == 1 or CT == 2:
            print("\t\tEnter grades (Q1 Q2 Q3 Q4): ")
            q1, q2, q3, q4 = int(input("\t\tQ1: ")), int(input("\t\tQ2: ")), int(input("\t\tQ3: ")), int(input("\t\tQ4: "))
            courses.append( (CT, LVL, q1, q2, q3, q4) )
        else:
            print("\t\tEnter grades (Q1 Q2): ")
            q1, q2 = int(input("\t\tQ1: ")), int(input("\t\tQ2: "))
            courses.append( (CT, LVL, q1, q2) )
        star_format(1)

    for course in courses:
        CT = course[0]
        LVL = course[1]
        
        CT_sum += CT
        
        gpa_delta = 0
        # testcase: IS NOT a full-year course (CT == 0.5)
        # semester_vals[0] is the semester one value
        semester_val_1 = (course[2] + course[3]) / 2.0
        if not semester_val_1 < 70:
            semester_val_1 = LVL - (1.0 - semester_val_1/100)*10
            gpa_delta += semester_val_1
        else:
            # weighted gpa is zero for grades below 70 😱 😱 😱
            semester_val_1 = 0.0
            pass
        # testcase: IS a full-year course
        if CT != 0.5:
            semester_val_2 = (course[4] + course[5]) / 2.0
            if not semester_val_2 < 70:
                semester_val_2 = LVL - (1.0 - semester_val_2/100)*10
                gpa_delta += semester_val_2
            else:
                # weighted gpa is zero for grades below 70 😱 😱 😱
                semester_val_2 = 0.0
                pass
            # must normalize the average...
            gpa_delta /= 2
        
        gpa += gpa_delta * CT
        # each course has corresponding semester GPA averages
        if CT != 0.5:
            course = (course[0], semester_val_1, semester_val_2)
        else:
            course = (course[0], semester_val_1)

    gpa /= CT_sum
    print(f"Weighted GPA: {gpa}")  
    
    i = 1
    # print("Course #ID: Weighted GPA Semester #1, Weighted GPA Semester #2")
    # for course in courses:
    #     if course[0] == 0.5:
    #         print(f"Course #{++i}: {course[1]}, DNE") 
    #     else:
    #         print(f"Course #{++i}: {course[1]}, {course[2]}") 
    #     i += 1

if __name__ == "__main__":
    main();
