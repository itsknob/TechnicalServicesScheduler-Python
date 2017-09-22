""" Used for creating Job Types"""
from enum import Enum

class EmployeeType(Enum):
    """Defines Job Types

    General Staff, Manager in Training, or Manager
    """

    GENERAL = 0
    MANAGER_IN_TRAINING = 1
    MANAGER = 2


class PersonalInformation:

    @property
    def student_id(self):
        return self._student_id
    @student_id.setter
    def student_id(self, new_id):
        self._student_id = new_id

    @property
    def name_first(self):
        return self._name_first
    @name_first.setter
    def name_first(self, new_name_first):
        self._name_first = new_name_first

    @property
    def name_last(self):
        return self._name_last
    @name_last.setter
    def name_last(self, new_name_last):
        self._name_last = new_name_last

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, new_email):
        #self._email = "\'"+new_email+"\'"
        self._email = new_email
        
    @property
    def phone_number(self):
        return self._phone_number
    @phone_number.setter
    def phone_number(self, new_phone_number):
        self._phone_number = new_phone_number


class WorkInformation:

    @property
    def job_type(self):
        return self._job_type
    @job_type.setter
    def job_type(self, new_job_type=EmployeeType):
        self._job_type = new_job_type

    @property
    def date_hire(self):
        return self._date_hire
    @date_hire.setter
    def date_hire(self, new_date_hire):
        self._date_hire = new_date_hire

    @property
    def date_graduate(self):
        return self._date_graduate
    @date_graduate.setter
    def date_graduate(self, new_date_graduate):
        self._date_graduate = new_date_graduate

    @property
    def shirt_size(self):
        return self._shirt_size
    @shirt_size.setter
    def shirt_size(self, new_shirt_size):
        self._shirt_size = new_shirt_size

    @property
    def notes(self):
        return self._notes
    @notes.setter
    def notes(self, new_notes):
        self._notes = new_notes


class Employee:
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
        return self.personal_information.name_first + " " + self.personal_information.name_last

    def get_personal_info_as_list(self):
        personal_info_list = list()
        personal_info_list.append(self.personal_information.student_id)
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
        all_info_list.extend(temp1)
        all_info_list.extend(temp2)
        return all_info_list


class Event:
    """Holds information about Events"""

    def __init__(self, name, location, date, start_time, end_time, number_employees, req_manager):
        self._event_name = name
        self._event_location = location
        self._event_date = date
        self._event_start_time = start_time
        self._event_end_time = end_time
        self._event_number_employees = number_employees
        self._event_requires_manager = req_manager

        self._event_employee_list = list()
        self._event_manager = None


    # "Getters/Setters" - Required Attributes
    @property
    def event_name(self):
        """Name of Event"""
        return self._event_name
    @event_name.setter
    def event_name(self, new_name):
        self._event_name = new_name

    @property
    def event_location(self):
        return self._event_location
    @event_location.setter
    def event_location(self, new_location):
        self._event_location = new_location

    @property
    def event_date(self):
        return self._event_date
    @event_date.setter
    def event_date(self, new_date):
        self._event_date = new_date

    @property
    def event_start_time(self):
        return self._event_start_time
    @event_start_time.setter
    def event_start_Time(self, new_start_time):
        self._event_start_time = new_start_time

    @property
    def event_end_time(self):
        return self._event_end_time
    @event_end_time.setter
    def event_end_time(self, new_end_time):
        self._event_end_time = new_end_time

    @property
    def event_number_employees(self):
        return self._event_number_employees
    @event_number_employees.setter
    def event_number_employees(self, new_number):
        self._event_number_employees = new_number

    @property
    def event_requires_manager(self):
        return self._event_requires_manager
    @event_requires_manager.setter
    def event_requires_manager(self, new_requires):
        self._event_requires_manager = new_requires

    # "Getters/Setters" - Additional Attributes
    @property
    def event_employee_list(self):
        return self._event_employee_list
    @event_employee_list.setter
    def event_employee_list(self, new_employee_list):
        self._event_employee_list = new_employee_list

    @property
    def event_manager(self):
        return self._event_manager
    @event_manager.setter
    def event_manager(self, new_manager):
        self._event_manager = new_manager

    # Event Methods
    def add_employee_to_event(self, employee=Employee):
        self.event_employee_list.append(employee)

    def remove_employee_from_event(self, employee=Employee):
        self.event_employee_list.remove(employee)
