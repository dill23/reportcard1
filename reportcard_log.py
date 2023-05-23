import datetime as dt
def time():
    time = dt.datetime.now()
    return time.strftime("%X")
def start_of_programe(name):
    with open("reportcard_logfile.log", "a") as log_file:
        times = dt.datetime.now()
        log_file.write(f"datetime of the start of programe: {times.strftime('%X')}")
        log_file.write("\n")
        log_file.write(f"Name of teacher {name}")
        log_file.write("\n")
def log_file_pre(pre):
    with open("reportcard_logfile.log", "a") as log_file:
        log_file.write(f"datetime: {time()}")
        log_file.writelines(pre)
        log_file.write("\n")
def add_student_log(id, name, grades):
     with open("reportcard_logfile.log", "a") as log_file:
         log_file.write(f"ID: {id}")
         log_file.write("     ")
         log_file.write(f"Name: {name}")
         log_file.write("\n")
         log_file.writelines(f"Grades: {grades}")
         log_file.write("\n")
         log_file.write("********************************")
         log_file.write("\n")
def modify_student_log(id, old_name, name, new_grades, old_grades):
    with open("reportcard_logfile.log", "a") as log_file:
        log_file.write(f"ID: {id}")
        log_file.write("       ")
        log_file.write(f"Name: {name}")
        log_file.write("\n")
        log_file.write(f"Old name: {old_name}")
        log_file.write("        ")
        log_file.write(f"New name: {name}")
        log_file.write("\n")
        log_file.write(f"old grades: {old_grades}")
        log_file.write("        ")
        log_file.write(f"New grades {new_grades}")
        log_file.write("\n")

def delete_data_log(teacher, wdd, prefix=None):
    with open("reportcard_logfile.log", "a") as log_file:
        """wdd stands for whole databases deleted"""
        if wdd == True:
            log_file.write(f"the whole database was deleted at {time()}")
            log_file.write("        ")
            log_file.write(f"It was deleted by {teacher}")
            log_file.write("\n")
        else:
            log_file.write(f"student data deleted {prefix}")
            log_file.write("        ")
            log_file.write(f"It was deleted by {teacher}")
            log_file.write("\n")
            log_file.write(f"It was deleted at this {time()} time.")
            log_file.write("\n")

def end_of_programe(name):
    with open("reportcard_logfile.log", "a") as log_file:
        log_file.write(f"Time at the end of programe: {time()}")
        log_file.write("\n")
        log_file.write(f"Name of teacher {name}")
        log_file.write("\n")
        log_file.write("********************************")
        log_file.write("\n")