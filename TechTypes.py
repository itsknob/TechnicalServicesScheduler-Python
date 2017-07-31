""" Used for creating Job Types"""
from enum import Enum

class EmployeeType(Enum):
    """Defines Job Types

    General Staff, Manager in Training, or Manager
    """

    GENERAL = 0
    MANAGER_IN_TRAINING = 1
    MANAGER = 2


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


class PersonalInformation:

    @property
    def name_first(self):
        return self.name_first
    @name_first.setter
    def name_first(self, new_name_first):
        self.name_first = new_name_first

    @property
    def name_last(self):
        return self.name_last
    @name_last.setter
    def name_last(self, new_name_last):
        self.name_last = new_name_last

    @property
    def email(self):
        return self.email
    @email.setter
    def email(self, new_email):
        self.email = new_email

    @property
    def phone_number(self):
        return self.phone_number
    @phone_number.setter
    def phone_number(self, new_phone_number):
        self.phone_number = new_phone_number

class WorkInformation:

    @property
    def job_type(self):
        return self.job_type
    @job_type.setter
    def job_type(self, new_job_type=EmployeeType):
        self.job_type = new_job_type

    @property
    def date_hire(self):
        return self.date_hire
    @date_hire.setter
    def date_hire(self, new_date_hire):
        self.date_hire = new_date_hire

    @property
    def date_graduate(self):
        return self.date_graduate
    @date_graduate.setter
    def date_graduate(self, new_date_graduate):
        self.date_graduate = new_date_graduate

    @property
    def shirt_size(self):
        return self.shirt_size
    @shirt_size.setter
    def shirt_size(self, new_shirt_size):
        self.shirt_size = new_shirt_size

    @property
    def notes(self):
        return self.notes
    @notes.setter
    def note(self, new_notes):
        self.note = new_notes


class Student:
    """
    Contains Personal and Work-related information about the student

    Requires PersionalInformation and WorkInformation Objects on Initialization
    """

    """
    trainings_completed = {"training_aud_sound": False, "training_aud_lights": False, "training_mobile_sound": False, "training_mobile_lights": False, "training_stage_safety": False, "training_commuter_cafe": False, "training_woodland_commons": False, "training_grand_reading_room": False, "training_professionalism": False, "training_x32": False, "training_sound_consoles": False, "training_sound_design": False, "training_amp_speaker_matching": False, "training_advanced_ion": False, "training_lighting_design": False, "training_networking": False, "training_equiptment_repair": False, "training_scenery_shop": False}
    """

    def __init__(self, p_info=PersonalInformation, w_info=WorkInformation, trainings=list):
        self.personal_information = p_info
        self.work_information = w_info
        self.trainings_completed = trainings

    def get_full_name(self):
        return self.personal_information.name_first.append(" " + self.personal_information.name_last)

    def get_personal_info_as_list(self):
        personal_info_list = list()
        personal_info_list.append(self.personal_information.name_first)
        personal_info_list.append(self.personal_information.name_last)
        personal_info_list.append(self.personal_information.email)
        personal_info_list.append(self.personal_information.phone_number)
        return personal_info_list

    def get_work_info_as_list(self):
        work_info_list = list()
        work_info_list.append(self.work_information.job_type)
        work_info_list.append(self.work_information.date_hire)
        work_info_list.append(self.work_information.date_graduate)
        work_info_list.append(self.work_information.shirt_size)
        work_info_list.append(self.work_information.notes)
        return work_info_list

    def return_all_info_as_list(self):
        all_info_list = list()
        temp1 = self.get_personal_info_as_list()
        temp2 = self.get_work_info_as_list()
        all_info_list.append(temp1)
        all_info_list.append(temp2)
        return all_info_list
