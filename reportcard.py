
from replit import db

class report_card():
    
    def __init__(self):
        self.id = input("Enter the student id of person you want to print: ")
        self.name = db[self.id + "_student_name"]
        self.grades = db[self.id + "_grades"]
        self.honors = 0
        self.honors_states = ""
        self.GPA = 0
        self.grade = ""

    def calcAve(self):
        self.average = (sum(self.grades)) / len(self.grades)

    def dropScoreNewAve(self):
        grade_list = []
        for grade in range(len(self.grades)):
            grade_list.append(self.grades[grade])
        grade_list.remove(max(grade_list))
        grade_list.remove(min(grade_list))
        self.dropAve = (sum(grade_list)) / len(grade_list)
        
    def letterGradeGPA(self):
        """Finding what average to use"""
        if self.dropAve > self.average:
            useAve = self.dropAve
        elif self.average > self.dropAve:
            useAve = self.average
        elif self.average == self.dropAve:
            useAve = self.average
        '''Number to letter grade'''
        if useAve >= 0 and useAve <= 60:
            self.grade = 'F'
        elif useAve > 60 and useAve <= 65:
            self.grade = 'D-'
        elif useAve == 66 or useAve == 67:
            self.grade = 'D'
        elif useAve > 67 and useAve <= 69:
            self.grade = 'D+'
        elif useAve > 69 and useAve <= 72:
            self.grade = 'C-'
        elif useAve >= 73 and useAve <= 76:
            self.grade = 'C'
        elif useAve >= 77 and useAve <= 79:
            self.grade = 'C+'
        elif useAve >= 80 and useAve <= 82:
            self.grade = 'B-'
        elif useAve >= 83 and useAve <= 86:
            self.grade = 'B'
        elif useAve >= 87 and useAve <= 89:
            self.grade = 'B+'
        elif useAve >= 90 and useAve <= 92:
            self.grade = 'A-'
        elif useAve >= 93 and useAve <= 96:
            self.grade = 'A'
        elif useAve >= 97:
            self.grade = 'A+'

        '''Letter to GPA'''
        if self.grade == 'F':
            self.GPA = '0.0'
        if self.grade == 'D-':
            self.GPA = '0.7'
        if self.grade == 'D':
            self.GPA = '1.0'
        if self.grade == 'D+':
            self.GPA = '1.3'
        if self.grade == 'C-':
            self.GPA = '1.7'
        if self.grade == 'C':
            self.GPA = '2.0'
        if self.grade == 'C+':
            self.GPA = '2.3'
        if self.grade == 'B-':
            self.GPA = '2.7'
        if self.grade == 'B':
            self.GPA = '3.0'
        if self.grade == 'B+':
            self.GPA = '3.3'
        if self.grade == 'A-':
            self.GPA = '3.7'
        if self.grade == 'A':
            self.GPA = '4.0'
        if self.grade == 'A+':
            self.GPA = '4.3'

        '''Designation of Honors'''

        if useAve >= 88 and useAve <= 91:
            self.honors_states = 'Honors'
            self.honors = 1
        elif useAve >= 92 and useAve <= 95:
            self.honors_states = 'High Honors'
            self.honors = 2
        elif useAve >= 96 and useAve <= 100:
            self.honors_states = 'Highest Honors'
            self.honors = 3
        else:
            self.honors = 0
    def print_reportcard(self, course, date):
        """This function fromats and prints the report card to the need requirements."""
        with open("reportCard.txt", 'a') as file:
            file.write("******************************************************************")
            file.write("\n")
            file.write("*")
            file.write(f"Date: {date}")
            file.write("         ")
            file.write(f"course: {course}")
            file.write("\n")
            file.write("*")
            file.write(f"Student id: {self.id}")
            file.write("         ")
            file.write(f"Student name: {self.name}")
            file.write("\n")
            file.write("*")
            file.write("\n")
            if self.honors > 0:
                file.write("*")
                file.write(f"{self.honors_states}")
                file.write("\n")
            elif self.honors == 0:
                file.write("*\n")
            file.write("*")
            file.write(f"grade: {self.grade}")
            file.write("\n")
            file.write("*")
            file.write(f"GPA: {self.GPA}")
            file.write("\n")
            file.write("*")
            file.write("\n")
            file.write("*")
            file.write("Assignment Scores List:")
            file.write("\n")
            file.write("*")
            for grade in range(len(self.grades)):
                file.write(str(self.grades[grade]))
                file.write("|")
            file.write("\n")
            file.write("*")
            file.write("\n")
            file.write("*****************************************************************")

def call_report_card(course, date):
    call = report_card()
    call.calcAve()
    call.dropScoreNewAve()
    call.letterGradeGPA()
    call.print_reportcard(course, date)