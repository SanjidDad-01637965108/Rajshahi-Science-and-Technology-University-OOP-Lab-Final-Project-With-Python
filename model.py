# TODO: Import Modules
import pandas
from random import choice

# TODO: Create New Variables
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


# TODO: Create Static Functions
def GENERATE_ID() -> str:
    GENERATED_ID_LIST = [choice(NUMBERS) for _ in range(0, 17)]
    GENERATED_ID_LIST_AS_STRING = "".join(GENERATED_ID_LIST)
    return "S" + GENERATED_ID_LIST_AS_STRING


def FORMATE_CONTACT(NUMBER: str) -> str:
    SETUP_STRING = "(+880)"
    FORMAT_CONTACT_INFO = SETUP_STRING + " " + NUMBER
    return FORMAT_CONTACT_INFO


# TODO: Create New Class Name: DB
class DB:
    # TODO: Create New Constructor
    def __init__(self):
        # TODO: Create New Attribute Name: FILE
        self.FILE = pandas.read_csv("DATA.csv")

    def DISPLAY_ALL_STUDENT_DATA(self):
        print("MAIN DB:")
        print(self.FILE)

    def FIND_STUDENT_DATA_BY_ID(self, _STUDENT_ID: str) -> int:
        USER_ENTRY = self.FILE[self.FILE["ID"] == _STUDENT_ID]
        print("STUDENT ENTRY:")
        print(USER_ENTRY)
        return USER_ENTRY.index.item()

    def CREATE_NEW_STUDENT_ENTRY(self, _STUDENT_NAME: str, _STUDENT_DEPT: str, _STUDENT_SEMESTER: str, _CONTACT: str):
        NEW_STUDENT_NAME = _STUDENT_NAME
        NEW_STUDENT_ID = GENERATE_ID()
        NEW_STUDENT_DEPT = _STUDENT_DEPT
        NEW_STUDENT_SEMESTER = _STUDENT_SEMESTER
        NEW_STUDENT_CONTACT = FORMATE_CONTACT(_CONTACT)
        NEW_STUDENT_DATA_LIST = [
            NEW_STUDENT_NAME, NEW_STUDENT_ID, NEW_STUDENT_DEPT, NEW_STUDENT_SEMESTER, NEW_STUDENT_CONTACT
        ]
        self.FILE.loc[len(self.FILE)] = NEW_STUDENT_DATA_LIST
        self.FILE.to_csv("DATA.csv", index=False)
        print("STUDENT ENTRY ADD SUCCESSFUL")
        self.FIND_STUDENT_DATA_BY_ID(NEW_STUDENT_ID)

    def DELETE_STUDENT_ENTRY(self, _STUDENT_ID: str):
        STUDENT_DB_INDEX = self.FIND_STUDENT_DATA_BY_ID(_STUDENT_ID=_STUDENT_ID)
        USER_OPTION = input("ARE YOU SURE. YOU WANT TO DELETE THE STUDENT ENTRY (YES => Y) (NO => N)? ").upper()
        if USER_OPTION == "Y" or USER_OPTION == "YES":
            self.FILE.drop(index=STUDENT_DB_INDEX, inplace=True)
            self.FILE.to_csv("DATA.csv", index=False)
            print("STUDENT ENTRY DELETE SUCCESSFUL")
        elif USER_OPTION == "N" or USER_OPTION == "NO":
            print("WELCOME BACK")
        else:
            print("ERROR")

    def EDIT_STUDENT_ENTRY(self, _STUDENT_ID: str):
        SELECTED_ENTRY_INDEX = self.FIND_STUDENT_DATA_BY_ID(_STUDENT_ID)
        while True:
            USER_OPTION = input("WHAT DO YOU WANT TO UPDATE ( NAME OR DEPT OR CONTACT ): ").upper()
            if USER_OPTION == "NAME":
                STUDENT_NEW_NAME = input("ENTER STUDENT NEW NAME: ").title()
                self.FILE.at[SELECTED_ENTRY_INDEX, "Name"] = STUDENT_NEW_NAME
                print("STUDENT NAME UPDATE SUCCESSFUL")
            elif USER_OPTION == "DEPT":
                STUDENT_NEW_DEPT = input("ENTER STUDENT NEW DEPT: ").upper()
                self.FILE.at[SELECTED_ENTRY_INDEX, "DEPT"] = STUDENT_NEW_DEPT
                print("STUDENT DEPT UPDATE SUCCESSFUL")
            elif USER_OPTION == "CONTACT":
                STUDENT_NEW_CONTACT = input("ENTER STUDENT NEW CONTACT: (+880) ")
                STUDENT_NEW_CONTACT_FORMATE = FORMATE_CONTACT(STUDENT_NEW_CONTACT)
                self.FILE.at[SELECTED_ENTRY_INDEX, "Contact"] = STUDENT_NEW_CONTACT_FORMATE
                print("STUDENT CONTACT UPDATE SUCCESSFUL")
            else:
                print("ERROR")
            self.FILE.to_csv("DATA.csv", index=False)
            USER_OPTION_AGAIN = input("DO YOU WANT TO UPDATE AGAIN (YES => Y) (NO => N) ? ").upper()
            if USER_OPTION_AGAIN == "Y" or USER_OPTION_AGAIN == "YES":
                pass
            else:
                break
