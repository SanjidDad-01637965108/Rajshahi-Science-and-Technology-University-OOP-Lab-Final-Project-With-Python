# TODO: Import Modules
from model import DB

# TODO: Create New Variables
CONTROL_LOOP = True

# TODO: Create New Object Name: DB_OBJECT
DB_OBJECT = DB()

# TODO: Create Loop For Continuously Running The Program
while CONTROL_LOOP:

    # TODO: Take Input From User, That What Do You Want and Store It To a Variable Name: USER_COMMAND
    USER_COMMAND = input("RSTU >>> ").upper()

    # TODO: Check IF USER_COMMAND == EXIT, Then Stop The Loop
    if USER_COMMAND == "EXIT":
        print("THANK YOU")

        # TODO: Update The CONTROL_LOOP Variable To False
        CONTROL_LOOP = False

    # TODO: Check IF USER_COMMAND == LIST, Then Print Main DataBase
    elif USER_COMMAND == "LIST":

        # TODO: Call DISPLAY_ALL_STUDENT_DATA Method From DB_OBJECT Object
        DB_OBJECT.DISPLAY_ALL_STUDENT_DATA()

    # TODO: Check IF USER_COMMAND == FIND, Then Find and Print Student Entry
    elif USER_COMMAND == "FIND":

        # TODO: Take Input Student ID
        USER_COMMAND = input("ENTER STUDENT ID: ").upper()

        # TODO: Call FIND_STUDENT_DATA_BY_ID Method From DB_OBJECT Object
        DB_OBJECT.FIND_STUDENT_DATA_BY_ID(USER_COMMAND)

    # TODO: Check IF USER_COMMAND == ADD, Then Add New Student Entry To The Main DataBase
    elif USER_COMMAND == "ADD":

        # TODO: Take Input Student All Info
        NEW_STUDENT_NAME = input("ENTER STUDENT NAME: ").title()
        NEW_STUDENT_DEPT = input("ENTER STUDENT DEPT: ").upper()
        NEW_STUDENT_SEMESTER = input("ENTER STUDENT SEMESTER: ").title()
        NEW_STUDENT_CONTACT = input("ENTER STUDENT CONTACT INFO: (+880) ")

        # TODO: Call CREATE_NEW_STUDENT_ENTRY Method From DB_OBJECT Object
        DB_OBJECT.CREATE_NEW_STUDENT_ENTRY(
            _STUDENT_NAME=NEW_STUDENT_NAME,
            _STUDENT_DEPT=NEW_STUDENT_DEPT,
            _STUDENT_SEMESTER=NEW_STUDENT_SEMESTER,
            _CONTACT=NEW_STUDENT_CONTACT
        )

    # TODO: Check IF USER_COMMAND == DELETE, Then Delete The Student Entry From Main DataBase
    elif USER_COMMAND == "DELETE":

        # TODO: Take Input Student ID
        USER_COMMAND = input("ENTER STUDENT ID: ").upper()

        # TODO: Call DELETE_STUDENT_ENTRY Method From DB_OBJECT Object
        DB_OBJECT.DELETE_STUDENT_ENTRY(USER_COMMAND)

    # TODO: Check IF USER_COMMAND == UPDATE, Then Update Student Entry From Main DataBase
    elif USER_COMMAND == "UPDATE":

        # TODO: Take Input Student ID
        USER_COMMAND = input("ENTER STUDENT ID: ").upper()

        # TODO: Call EDIT_STUDENT_ENTRY Method From DB_OBJECT Object
        DB_OBJECT.EDIT_STUDENT_ENTRY(USER_COMMAND)

    # TODO: IF EveryThing False Then Print Error
    else:
        print(
            F"{USER_COMMAND} : The Term '{USER_COMMAND}' Not Recognized as The Name Of a Function or Operable Program"
        )
