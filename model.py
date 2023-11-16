# TODO: Import Modules
import pandas
from random import choice

# TODO: Create New Variables
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


# TODO: Create Static Functions

# TODO: Function For Generate Student ID
def GENERATE_ID() -> str:
    GENERATED_ID_LIST = [choice(NUMBERS) for _ in range(0, 17)]
    GENERATED_ID_LIST_AS_STRING = "".join(GENERATED_ID_LIST)
    return "S" + GENERATED_ID_LIST_AS_STRING


# TODO: Function For Formate Student Contact Info
def FORMATE_CONTACT(NUMBER: str) -> str:
    SETUP_STRING = "(+880)"
    FORMAT_CONTACT_INFO = SETUP_STRING + " " + NUMBER
    return FORMAT_CONTACT_INFO


# TODO: Create New Class Name: DB
class DB:

    # TODO: Create New Constructor
    def __init__(self):

        # TODO: Create New Attribute Name: FILE, That Store All Data From Main DataBase
        self.FILE = pandas.read_csv("DATA.csv")

    # TODO: Create New Method Name: DISPLAY_ALL_STUDENT_DATA For Print Main DataBase
    def DISPLAY_ALL_STUDENT_DATA(self):
        print("MAIN DB:")
        print(self.FILE)

    # TODO: Create New Method Name: FIND_STUDENT_DATA_BY_ID That Take Student ID As Input and Return
    #  Student Entry Index Number From Main Database
    def FIND_STUDENT_DATA_BY_ID(self, _STUDENT_ID: str) -> int:

        # TODO: Select Student Entry By ID and Store It To a Variable Called: USER_ENTRY
        USER_ENTRY = self.FILE[self.FILE["ID"] == _STUDENT_ID]

        # TODO: Print USER_ENTRY Variable
        print("STUDENT ENTRY:")
        print(USER_ENTRY)

        # TODO: Return Student Entry Index Number From Main Database
        return USER_ENTRY.index.item()

    # TODO: Create New Method Name: CREATE_NEW_STUDENT_ENTRY That Take Many Input and Add New
    #  Student Entry To Main DataBase
    def CREATE_NEW_STUDENT_ENTRY(self, _STUDENT_NAME: str, _STUDENT_DEPT: str, _STUDENT_SEMESTER: str, _CONTACT: str):

        # TODO: Take Student All Info and Store It
        NEW_STUDENT_NAME = _STUDENT_NAME
        NEW_STUDENT_ID = GENERATE_ID()
        NEW_STUDENT_DEPT = _STUDENT_DEPT
        NEW_STUDENT_SEMESTER = _STUDENT_SEMESTER
        NEW_STUDENT_CONTACT = FORMATE_CONTACT(_CONTACT)

        # TODO: Create NEW_STUDENT_DATA_LIST List The Hold All Student Data As Formatted
        NEW_STUDENT_DATA_LIST = [
            NEW_STUDENT_NAME, NEW_STUDENT_ID, NEW_STUDENT_DEPT, NEW_STUDENT_SEMESTER, NEW_STUDENT_CONTACT
        ]

        # TODO: Add NEW_STUDENT_DATA_LIST List As a Variable To The FILE Attribute
        self.FILE.loc[len(self.FILE)] = NEW_STUDENT_DATA_LIST

        # TODO: Save It To The Main DataBase Called: DATA.csv
        self.FILE.to_csv("DATA.csv", index=False)

        # TODO: Print New Student Entry
        print("STUDENT ENTRY ADD SUCCESSFUL")
        self.FIND_STUDENT_DATA_BY_ID(NEW_STUDENT_ID)

    # TODO: Create New Method Name: DELETE_STUDENT_ENTRY That That Take Student ID As Input and Delete
    #  The Student Entry From Main DataBase
    def DELETE_STUDENT_ENTRY(self, _STUDENT_ID: str):

        # TODO: Call FIND_STUDENT_DATA_BY_ID Method To Print Student Entry and Store Index Number From Main DataBase
        STUDENT_DB_INDEX = self.FIND_STUDENT_DATA_BY_ID(_STUDENT_ID=_STUDENT_ID)

        # TODO: Take Input and Store It To a Variable Called: USER_OPTION
        USER_OPTION = input("ARE YOU SURE. YOU WANT TO DELETE THE STUDENT ENTRY (YES => Y) (NO => N)? ").upper()

        # TODO: Check IF USER_OPTION == Yes, Then Delete The Student Entry From Main DataBase
        if USER_OPTION == "Y" or USER_OPTION == "YES":

            # TODO: Delete The Student Entry From FILE Attribute
            self.FILE.drop(index=STUDENT_DB_INDEX, inplace=True)

            # TODO: Update Main DateBase
            self.FILE.to_csv("DATA.csv", index=False)
            print("STUDENT ENTRY DELETE SUCCESSFUL")

        # TODO: Check IF USER_OPTION == No, Then Pass
        elif USER_OPTION == "N" or USER_OPTION == "NO":
            print("WELCOME BACK")

        # TODO: IF EveryThing False Then Print Error
        else:
            F"{USER_OPTION} : The Term '{USER_OPTION}' Not Recognized as The Name Of a Function or Operable Keyword"

    # TODO: Create New Method Name: EDIT_STUDENT_ENTRY That That Take Student ID As Input and Update
    #  Student Information From Main DataBase
    def EDIT_STUDENT_ENTRY(self, _STUDENT_ID: str):

        # TODO: Call FIND_STUDENT_DATA_BY_ID Method To Print Student Entry and Store Index Number From Main DataBase
        SELECTED_ENTRY_INDEX = self.FIND_STUDENT_DATA_BY_ID(_STUDENT_ID)

        # TODO: Create Infinite Loop
        while True:

            # TODO: Take Input What User Want To Update and Store It To a Variable Name: USER_OPTION
            USER_OPTION = input("WHAT DO YOU WANT TO UPDATE ( NAME OR DEPT OR CONTACT ): ").upper()

            # TODO: Check IF USER_OPTION == NAME, Then Update Student Name From FILE Attribute
            if USER_OPTION == "NAME":

                # TODO: Take Student New NAME As Input and Store It To a Variable Name: STUDENT_NEW_NAME
                STUDENT_NEW_NAME = input("ENTER STUDENT NEW NAME: ").title()

                # TODO: Update The Name In The FILE Attribute
                self.FILE.at[SELECTED_ENTRY_INDEX, "Name"] = STUDENT_NEW_NAME
                print("STUDENT NAME UPDATE SUCCESSFUL")

            # TODO: Check IF USER_OPTION == DEPT, Then Update Student DEPT From FILE Attribute
            elif USER_OPTION == "DEPT":

                # TODO: Take Student New DEPT As Input and Store It To a Variable Name: STUDENT_NEW_DEPT
                STUDENT_NEW_DEPT = input("ENTER STUDENT NEW DEPT: ").upper()

                # TODO: Update The DEPT In The FILE Attribute
                self.FILE.at[SELECTED_ENTRY_INDEX, "DEPT"] = STUDENT_NEW_DEPT
                print("STUDENT DEPT UPDATE SUCCESSFUL")

            # TODO: Check IF USER_OPTION == CONTACT, Then Update Student CONTACT Info From FILE Attribute
            elif USER_OPTION == "CONTACT":

                # TODO: Take Student New CONTACT As Input and Store It To a Variable Name: STUDENT_NEW_CONTACT
                STUDENT_NEW_CONTACT = input("ENTER STUDENT NEW CONTACT: (+880) ")

                # TODO: Formate The Student Contact Info and Store It To New Variable Name: STUDENT_NEW_CONTACT_FORMATE
                STUDENT_NEW_CONTACT_FORMATE = FORMATE_CONTACT(STUDENT_NEW_CONTACT)

                # TODO: Update The CONTACT In The FILE Attribute
                self.FILE.at[SELECTED_ENTRY_INDEX, "Contact"] = STUDENT_NEW_CONTACT_FORMATE
                print("STUDENT CONTACT UPDATE SUCCESSFUL")

            # TODO: IF EveryThing False Then Print Error
            else:
                print(
                    F"{USER_OPTION} : The Term '{USER_OPTION}' Not Recognized as The Name Of a Operable Keyword"
                )

            # TODO: Update The Main DataBase Name: DATA.csv
            self.FILE.to_csv("DATA.csv", index=False)

            # TODO: Take Input That User Want To Update Info Again and Store It To a Variable Name: USER_OPTION_AGAIN
            USER_OPTION_AGAIN = input("DO YOU WANT TO UPDATE AGAIN (YES => Y) (NO => N) ? ").upper()

            # TODO: Check IF USER_OPTION_AGAIN == Yes, Then Do All Of The Work Again
            if USER_OPTION_AGAIN == "Y" or USER_OPTION_AGAIN == "YES":
                pass

            # TODO: IF USER_OPTION_AGAIN == No, Then Exit The Infinite Loop
            else:
                break
