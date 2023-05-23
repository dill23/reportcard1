"""
Dylan Hilse
2/6/23
This project will countiune to test my knowledge of dictionarys. I will create a programe that will create a reporet card that will be stored in a dictonary. we will also have a log file to log all the changes. 
"""
"""Import all needed APIs"""
import sys
import os
from datetime import datetime

from replit import db

import reportcard as rc
import database_manager as dm
import reportcard_log as rl
"""Message for the main menu."""
MAIN_MESSAGE = """
Main menu
1 - Add student
2 - Modify student info
3 - Delete student
4 - Print report card
5 - Quit
"""
"""Prompet the person for the preinfo."""
def preinfo():
    try:
        name_of_teacher = input("Enter your name: ").strip()
        while name_of_teacher == '' or name_of_teacher.isdigit() == True or len(name_of_teacher) <= 2:
            print("I don't think that is your name")
            name_of_teacher = input("Enter your name: ").strip()
            
        course_name = input("enter the name of the course: ").strip()
        while course_name == '' or len(course_name) <= 3:
            print("I don't think that this is a course.")
            course_name = input("enter the name of the course: ").strip()
        
        term = int(input("enter the term number between 1-4: "))
        while term > 4 or term < 1:
            print("Please try again")
            term = int(input("Enter the term number between 1-4: "))
        while True:  
            """Prompts for dates formating and validations"""
            try:
                format = "%m/%d/%y"
                date = input("Enter today's date mm/dd/yy: ").strip()
                bool(datetime.strptime(date, format))
                print(f"correct {date}")
                break
            except ValueError:
                print("Inccorect")
        return name_of_teacher.capitalize(), course_name.capitalize(), term, date
    except ValueError:
        print("That is not a intager.")
    except KeyboardInterrupt:
        sys.exit(0)
"""This function prompts for the needed information for adding students."""
def add_student():
    while True:
        try:
            student_id = int(input("Enter the student id please: "))
            while student_id < 100:
                print("Please try again.")
                student_id = int(input("Enter the student id please: "))

            student_name = input("Enter the name of the student: ")
            while len(student_name) == 0 or student_name.isdigit() == True:
                print("Please try again")
                student_name = input("Enter the name of the student: ")
            """Creates the key for the database"""
            student_id_key = str(student_id) + "_student_id"
            student_name_key = str(student_id) + "_student_name"
            grades = []
            while True:
                try:
                    student_grades = input("Please enter the grade or press enter to end: ").strip( )
                    
                    if student_grades == '':
                        grades_key = str(student_id) + "_grades" 
                        dm.add_info(student_name_key, student_name, student_id_key, student_id, grades_key, grades)
                        rl.add_student_log(student_id, student_name, grades)
                        break
                    else:
                        grade = float(student_grades)
                    grades.append(grade)
                except ValueError:
                    print("Please try again ")
            
            another_student = input("Do you want to enter another student y or n: ")
            print(grades)
            if another_student == 'y':
                continue
            elif another_student == 'n':
                break
        except ValueError:
            print("That is not a number please try again.")
"""This function is used to modify the student data"""
def modify_student():
    while True:
        try:
            student = input("enter the student id:")
            old_name = db[student + "_student_name"]
            new_name = input("Enter the new name: ")
            key = student + "_student_name"
            dm.update_info(key, new_name)
            old_grades =  db[student + "_grades"]
            print(old_name, old_grades, student)
            grades = []
            while True:
                try:
                    student_grades = input("Enter the grade or press enter to end: ").strip()
                    if student_grades == '':
                        key = student + "_grades"
                        dm.update_info(key, grades)
                        rl.modify_student_log(student, old_name, new_name, grades, old_grades)
                        
                        break
                    else:
                        grade = float(student_grades)
                    grades.append(grade)
                except ValueError:
                    print("Please try again ")
            exit = input("Do you want to exit y or n: ")
            if exit == 'y':
                break
            elif exit == 'n':
                continue
        except KeyError:
            print("That field does not exist")
"""Deletes all of the students data """
def delete_student_info(teacher):
    while True:
        delete_all = input("do you want to delete the entire database: ").strip()
        wdd = False
        if delete_all == '666':
            dm.list_info()
            sure = input("Are you sure y or n: ").strip() 
            if sure == 'y':
                db.clear()
                """wdd means whole database deleted"""
                wdd = True
                rl.delete_data_log(teacher, wdd)
                break
            else:
                continue
        delete_student = input("enter the id of student you want to delete or q to quit: ").strip()
        if delete_student == 'q':
            break
        prefix = db.prefix(delete_student)
        print(dm.search_info(delete_student))
        sure = input("Are you sure y or n: ").strip() 
        if sure == 'y':
            dm.delete_info(prefix[0])
            dm.delete_info(prefix[1])
            dm.delete_info(prefix[2])
            rl.delete_data_log(teacher, wdd, prefix)
	
"""Main function to prompt for you choice of what to do."""
def main(teacher, course, date):
    print(MAIN_MESSAGE)
    choice = input("Enter your choice 1-5: ").strip()
    if choice == "1":
        add_student()
    elif choice =='2':
        modify_student()
    elif choice == '3':
        delete_student_info(teacher)
    elif choice == '4':
        rc.call_report_card(course, date)
    elif choice == '5':
        rl.end_of_programe(teacher)
        sys.exit(0)
    else:
        print("Please try again.")

"""This code sees if it is the main file and runs the code in the if statment"""
if __name__ == "__main__":
    teacher, course, term, date = preinfo()
    pre_info = ' ', date, ' ', teacher, ' ', f"The term {str(term)}", ' ', course
    rl.start_of_programe(teacher)
    while True:
        os.system("clear")
        main(teacher, course, date)
        rl.log_file_pre(pre_info)
        input("Press enter to continue.")