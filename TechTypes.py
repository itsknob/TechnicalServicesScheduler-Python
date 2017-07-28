import time as Time
from enum import Enum


class EmployeeType(Enum):
    """Defines Job Types

    General Staff, Manager in Training, or Manager
    """

    GENERAL = 0
    MANAGER_IN_TRAINING = 1
    MANAGER = 2


class Employee:
    """Contains information about employee

    No Shirt Size
    """

    __employee_name_first = None
    __employee_name_last = None
    __employee_student_id = None
    __employee_employee_id = None
    __employee_email = None
    __employee_phone_number = None
    __employee_job_type = EmployeeType

    def __init__(self, name_first, name_last, s_id, e_id, email, phone_number, job_type: EmployeeType):
        self.__employee_name_first = name_first
        self.__employee_name_last = name_last
        self.__employee_student_id = s_id
        self.__employee_employee_id = e_id
        self.__employee_email = email
        self.__employee_phone_number = phone_number
        self.__employee_job_type = job_type

    def get_employee_name(self):
        """Returns first name concatenated with last name
        """
        return self.__employee_name_last + " " + self.__employee_name_last

    def get_employee_student_id(self):
        return self.__employee_student_id

    def get_employee_employee_id(self):
        return self.__employee_employee_id

    def get_employee_email(self):
        return self.__employee_email

    def get_employee_phone_number(self):
        return self.__employee_phone_number

    def get_employee_job_type(self):
        return self.__employee_job_type

    def set_employee_name_first(self, new_name_first):
        self.__employee_name_first = new_name_first

    def set_employee_name_last(self, new_name_last):
        self.__employee_name_last = new_name_last

    def set_employee_student_id(self, new_student_id):
        self.__employee_student_id = new_student_id

    def set_employee_employee_id(self, new_employee_id):
        self.__employee_employee_id = new_employee_id

    def set_employee_email(self, new_email):
        self.__employee_email = new_email

    def set_employee_phone_number(self, new_phone_number):
        self.__employee_phone_number = new_phone_number

    def set_employee_job_type(self, new_job_type: EmployeeType):
        self.__employee_job_type = new_job_type


class Event:
    """Holds information about Events

    Setters are strongly typed
    """

    # Variables Required on initialization
    __event_name = None
    __event_location = None
    __event_date = None
    __event_start_time = 0
    __event_end_time = 0
    __event_number_employees = 0
    __event_req_manager = False

    # Variables later initialized
    __event_employee_list = []
    __event_manager = None
    # __event_length = None         # Later Contemplated

    def __init__(self, name, location, date, start_time, end_time, number_employees, req_manager):
        self.__event_name = name
        self.__event_location = location
        self.__event_date = date
        self.__event_start_time = start_time
        self.__event_end_time = end_time
        self.__event_number_employees = number_employees
        self.__event_req_manager = req_manager

    def get_event_name(self):
        return self.__event_name

    def get_event_location(self):
        return self.__event_location

    def get_event_date(self):
        return self.__event_date

    def get_event_start_time(self):
        return self.__event_start_time

    def get_event_end_time(self):
        return self.__event_end_time

    def get_event_number_employees(self):
        return self.__event_number_employees

    def get_event_req_manager(self):
        return self.__event_req_manager

    def set_event_name(self, new_name):
        if not isinstance(new_name, str):
            return TypeError
        self.__event_name = new_name

    def set_event_location(self, new_location):
        if not isinstance(new_location, str):
            return TypeError
        self.event_location = new_location

    def set_event_date(self, new_date):
        if not isinstance(new_date, str):
            return TypeError
        self.event_date = new_date

    def set_event_start_time(self, new_start_time):
        if not isinstance(new_start_time, str):
            return TypeError
        self.event_start_time = new_start_time

    def set_event_end_time(self, new_end_time):
        if not isinstance(new_end_time, str):
            return TypeError
        self.event_end_time = new_end_time

    def set_event_number_employees(self, new_number_employees):
        if not isinstance(new_number_employees, int):
            return TypeError
        self.event_number_employees = new_number_employees

    def set_event_req_manager(self, req_manager):
        if not isinstance(req_manager, bool):
            return TypeError
        self.event_req_manager = req_manager

class Student:
    """Contains information about student. Fields are private."""

    __student_id = None
    __student_name_first = None
    __student_name_last = None
    __student_job_type = None
    __student_phone_number = None
    __student_email = None
    __student_date_hire = None
    __student_date_graduate = None
    __student_shirt_size = None
    __student_notes = None

    def __init__(self, student_id, student_name_first, student_name_last, student_job_type, student_phone_number, student_email, student_date_hire, student_date_graduate, student_shirt_size, student_notes):
        self.__student_id = student_id
        self.__student_name_first = student_name_first
        self.__student_name_last = student_name_last
        self.__student_job_type = student_job_type
        self.__student_phone_number = student_phone_number
        self.__student_email = student_email
        self.__student_date_hire = student_date_hire
        self.__student_date_graduate = student_date_graduate
        self.__student_shirt_size = student_shirt_size
        self.__student_notes = student_notes

    def get_student_id():   
        return self.__student_id

    def get_student_name_first():
        return self.__student_name_first

    def get_student_name_last():
        return self.__student_name_last

    def get_student_job_type():
        return self.__student_job_type

    def get_student_phone_number():
        return self.__student_phone_number

    def get_student_email():
        return self.__student_email

    def get_student_date_hire():
        return self.__student_date_hire

    def get_student_date_graduate():
        return self.__student_date_graduate

    def get_student_shirt_size():
        return self.__student_shirt_size

    def get_student_notes():
        return self.__student_notes


    def set_student_id(new_id):
        self.__student_id = new_id

    def set_student_name_first(new_name_first):
        self.__student_name_first = new_name_first

    def set_student_name_last(new_name_last):
        self.__student_name_last = new_name_last

    def set_student_job_type(new_job_type):
        self.__student_job_type = new_job_type

    def set_student_phone_number(new_phone_number):
        self.__student_phone_number = new_phone_number

    def set_student_email(new_email):
        self.__student_email = new_email

    def set_student_date_hire(new_date_hire):
        self.__student_date_hire = new_date_hire

    def set_student_date_graduate(new_date_graduate):
        self.__student_date_graduate = new_date_graduate

    def set_student_shirt_size(new_shirt_size):
        self.__student_shirt_size = new_shirt_size

    def set_student_notes(new_notes):
        self.__student_notes = new_notes

    def return_all_data_as_string(self):
        """This function exists for ease of use when dealing with the database.
        When creating an SQL statement for inserting a student into the database
        this will return all values needed for insert. """
        value_string = "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(self.__student_id, self.__student_name_first, self.__student_name_last, self.__student_job_type, self.__student_phone_number, self.__student_email, self.__student_date_hire, self.__student_date_graduate, self.__student_shirt_size, self.__student_notes)
        return value_string

class Student_Trainings():
    """"""

test = Student("01358308", 'Stephen', 'Reilly', 'manager', "9788688473", 'sreilly@umassd.edu', "2013-04-01", "2017-05-07", 'L', "Best employee we've ever had.")
test.return_all_data_as_string()
