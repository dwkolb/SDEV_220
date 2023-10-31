#Author: Derek W. Kolb
#Version 1.  10/31/2023
#File Name: kolb_m02_caseStudy.py
# Description: This program allows users to enter student information, including their first and last names
# and GPA. It then determines the students' academic achievements based on their GPA, such as the Dean's list
# or Honor Roll. Users can enter 'ZZZ' to quit the program.

while True:
    studentLastName = input("Enter student's last name here (or 'ZZZ' to quit): ").strip().lower()
    if studentLastName == 'zzz':
        break #exit loop if ZZZ is entered
    
    studentFirstName = input("Enter student's first name here: ").strip().lower()
    
    #Capitalize the first letter of each name and concatenate with a space 
    studentFullName = studentFirstName.title() + " " + studentLastName.title()
    
    try:
        gpa = float(input("Enter Student's GPA here: "))
        if 0 <= gpa <= 4.0: #Check if GPA is within a valid range
            if gpa >= 3.5:
                print(f"{studentFullName} has made the Dean's list.")
            elif gpa >= 3.25:
                print(f"{studentFullName} has made the Honor Roll.")
            else:
                print(f"{studentFullName} did not qualify for the Dean's list nor the Honor Roll.")
        else:
            print("Invalid GPA input. GPA must be between 0 and 4.")
    except ValueError:
        print("Invalid GPA input. Please enter a valid GPA as a number.")
        continue #Restart loop if an invalid GPA is entered
    
    
