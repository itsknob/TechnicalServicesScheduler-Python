""" Used for creating Job Types"""
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


    """In order to reduce arguments, may need to create WorkInfo and PersonalInfo classes"""
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
    """Holds information about Events"""

    def __init__(self, name, location, date, start_time, end_time, number_employees, req_manager):
        self.__event_name = name
        self.__event_location = location
        self.__event_date = date
        self.__event_start_time = start_time
        self.__event_end_time = end_time
        self.__event_number_employees = number_employees
        self.__event_req_manager = req_manager

    @property
    def event_name(self):
        """Name of Event"""
        return self.event_name
    @event_name.setter
    def event_name(self, new_name):
        self.event_name = new_name

    @property
    def event_location(self):
        return self.event_location
    @event_location.setter
    def event_location(self, new_location):
        self.event_location = new_location

    @property
    def event_date(self):
        return self.event_date
    @event_date.setter
    def event_date(self, new_date):
        self.event_date = new_date

    @property
    def event_start_time(self):
        return self.event_start_time
    @event_start_time.setter
    def event_start_Time(self, new_start_time):
        self.event_start_time = new_start_time

    @property
    def event_end_time(self):
        return self.event_end_time
    @event_end_time.setter
    def event_end_time(self, new_end_time):
        self.event_end_time = new_end_time

    @property
    def event_number_employees(self):
        return self.event_number_employees
    @event_number_employees.setter
    def event_number_employees(self, new_number):
        self.event_number_employees = new_number

    @property
    def event_requires_manager(self):
        return self.event_requires_manager
    @event_requires_manager.setter
    def event_requires_manager(self, new_requires):
        self.event_requires_manager = new_requires


    @property
    def event_employee_list(self):
        return self.event_employee_list
    @event_employee_list.setter
    def event_employee_list(self, new_employee_list):
        self.event_employee_list = new_employee_list

    @property
    def event_manager(self):
        return self.event_manager
    @event_manager.setter
    def event_manager(self, new_manager):
        self.event_manager = new_manager


class Student:
    """Contains information about student. Fields are private."""

    __student_id = None
    __student_name_first = None
    __student_name_last = None
    __student_job_type = EmployeeType
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


    def set_student_id(new_id: str):
        self.__student_id = new_id

    def set_student_name_first(new_name_first: str):
        self.__student_name_first = new_name_first

    def set_student_name_last(new_name_last: str):
        self.__student_name_last = new_name_last

    def set_student_job_type(new_job_type: EmployeeType):
        self.__student_job_type = new_job_type

    def set_student_phone_number(new_phone_number: str):
        self.__student_phone_number = new_phone_number

    def set_student_email(new_email: str):
        self.__student_email = new_email

    def set_student_date_hire(new_date_hire: str):
        self.__student_date_hire = new_date_hire

    def set_student_date_graduate(new_date_graduate: str):
        self.__student_date_graduate = new_date_graduate

    def set_student_shirt_size(new_shirt_size: str):
        self.__student_shirt_size = new_shirt_size

    def set_student_notes(new_notes: str):
        self.__student_notes = new_notes

    def return_all_data_as_string(self):
        """This function exists for ease of use when dealing with the database.
        When creating an SQL statement for inserting a student into the database
        this will return all values needed for insert. """
        value_string = "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(self.__student_id, self.__student_name_first, self.__student_name_last, self.__student_job_type, self.__student_phone_number, self.__student_email, self.__student_date_hire, self.__student_date_graduate, self.__student_shirt_size, self.__student_notes)
        return value_string

class Student_Trainings():
    """Contains information about trainings

    Change to single dictionary in Student Class
    """
    student_id = str
    training_aud_sound = False
    training_aud_lights = False
    training_mobile_sound = False
    training_mobile_lights = False
    training_stage_safety = False
    training_commuter_cafe = False
    training_woodland_commons = False
    training_grand_reading_room = False
    training_professionalism = False
    training_x32 = False
    training_sound_consoles = False
    training_sound_design = False
    training_amp_speaker_matching = False
    training_advanced_ion = False
    training_lighting_design = False
    training_networking = False
    training_equiptment_repair = False
    training_scenery_shop = False

    def __init__(student_id):
        self.student_id = student_id

    def complete_training(self, variable):
        return self.variable.__owner__()
