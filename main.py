# TODO: Import Modules
from model import DB

# TODO: Create New Variables
CONTROL_LOOP = True

# TODO: Create New Object Name: DB_OBJECT
DB_OBJECT = DB()

# TODO: Create Loop For Continuously Running The Program
while CONTROL_LOOP:
    USER_COMMAND = input("RSTU >>> ").upper()

    if USER_COMMAND == "EXIT":
        print("THANK YOU")
        CONTROL_LOOP = False
    elif USER_COMMAND == "LIST":
        DB_OBJECT.DISPLAY_ALL_STUDENT_DATA()
    elif USER_COMMAND == "FIND":
        USER_COMMAND = input("ENTER STUDENT ID: ").upper()
        DB_OBJECT.FIND_STUDENT_DATA_BY_ID(USER_COMMAND)
    elif USER_COMMAND == "ADD":
        NEW_STUDENT_NAME = input("ENTER STUDENT NAME: ").title()
        NEW_STUDENT_DEPT = input("ENTER STUDENT DEPT: ").upper()
        NEW_STUDENT_SEMESTER = input("ENTER STUDENT SEMESTER: ").title()
        NEW_STUDENT_CONTACT = input("ENTER STUDENT CONTACT INFO: (+880) ")
        DB_OBJECT.CREATE_NEW_STUDENT_ENTRY(
            _STUDENT_NAME=NEW_STUDENT_NAME,
            _STUDENT_DEPT=NEW_STUDENT_DEPT,
            _STUDENT_SEMESTER=NEW_STUDENT_SEMESTER,
            _CONTACT=NEW_STUDENT_CONTACT
        )
    elif USER_COMMAND == "DELETE":
        USER_COMMAND = input("ENTER STUDENT ID: ").upper()
        DB_OBJECT.DELETE_STUDENT_ENTRY(USER_COMMAND)
    elif USER_COMMAND == "UPDATE":
        USER_COMMAND = input("ENTER STUDENT ID: ").upper()
        DB_OBJECT.EDIT_STUDENT_ENTRY(USER_COMMAND)
    else:
        print("ERROR")
