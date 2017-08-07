"""Employee Handler Refactor"""
import sqlite3
import os.path
from TechTypes import *


class DatabaseHandler:

	# Fields 
	employee_fields = "(student_id, employee_name_first, employee_name_last, employee_email, employee_phone_number, employee_job_type, employee_date_hire, employee_date_graduate, employee_shirt_size, employee_notes)"
	training_fields = "(student_id, mobile_sound, mobile_lights, auditorium_sound, auditorium_lights, stage_safety, commuter_cafe, woodland_commons, grand_reading_room, professionalism, x32, sound_consoles, sound_design, amp_speaker_matching, advanced_ion, lighting_design, networking, scenery_shop)"
	# May be moved elsewhere to be used as a first-run setup. IE __init__.py
	def __init__(self):
		# Config file exists
		if os.path.isfile("config.txt"):
			print("Found Config File")
			# Parse config file into dictionary
			config_information = self.parse_config() # Config will always be named 'config.txt'
			# If database is not in the config file
			if config_information['database'] is None:
				self.check_if_database_exists()
		# Config file does not exist
		else:
			print("Could Not Find Config File")
			open("config.txt", "w+").close() # touch 'config.txt', creates empty file
			self.check_if_database_exists() # User may have a database

		# Get database name from config file, Config file should exist and be setup properly by this point
		config_information = self.parse_config() # Config will always be named 'config.txt'
		self.con, self.cur = self.connect_to_database(config_information['database'])

	def check_if_database_exists(self):
		print("Database not found in config file")
		# Ask if database exsists
		does_db_exist = input("Does a database exist? (y/n)").upper()
		print(does_db_exist)
		# Database exists, ask where it is
		if does_db_exist == 'Y':
			self.locate_database()
		else:
			self.create_database()

	def parse_config(self):
		"""Opens config.txt, reads, closes, and parses lines to, and returns, a dictionar"""
		data = dict()
		with open("config.txt") as config_file:
			config_data = config_file.readlines()
		for line in config_data:
			line = line.strip()
			key, value = line.split(":") # This will break if file path is used for database ie "C:\""
			data.update({str(key): str(value)})
		return data

	def locate_database(self):
		"""Find existing database"""
		from tkinter import Tk
		from tkinter.filedialog import askopenfilename
		Tk().withdraw()
		# Select database
		existing_database_name = askopenfilename(title="Choose a Database")
		# Strip path from filename
		existing_database_name = os.path.basename(existing_database_name)
		# Write to config file
		with open("config.txt", "w+") as config_file:
			config_file.write("database:"+existing_database_name)

	def create_database(self):
		# Prompt for new database name
		new_database_name = input("Enter new name for database (please include '.db'): ")
		# Create database file
		open(new_database_name, "w+").close() # touch new_database_name (creates file)
		# Add filename to config file
		with open("config.txt", "w+") as config_file:
			config_file.write("database:"+new_database_name)
		# Ensure connection is made
		self.con, self.cur = self.connect_to_database(new_database_name)
		# Set up tables
		self.create_tables()
		self.con.close()	# This will be reopened when returned to __init__()

	def create_tables(self):
		self.con.execute("""create table if not exists employees (student_id varchar(8) primary key,
											employee_name_first varchar(32),
											employee_name_last varchar(32),
											employee_email varchar(64),
											employee_phone_number integer,
											employee_job_type varchar(8),
											employee_date_hire date,
											employee_date_graduate date,
											employee_shirt_size varchar(4),
											employee_notes varchar(255))""")
		self.con.execute("""create table if not exists trainings (student_id varchar(8) primary key,
											mobile_sound integer,
											mobile_lights integer,
											auditorium_sound integer,
											auditorium_lights integer,
											stage_safety integer,
											commuter_cafe integer,
											woodland_commons integer,
											grand_reading_room integer,
											professionalism integer,
											x32 integer,
											sound_consoles integer,
											sound_design integer,
											amp_speaker_matching integer,
											advanced_ion integer,
											lighting_design integer,
											networking integer,
											scenery_shop integer)""")
		self.con.commit()

	def connect_to_database(self, database):
		"""Returns connection and cursor"""

		# Database name from config file
		connection = sqlite3.connect(database)
		cursor = connection.cursor()
		return connection, cursor

	def add_new_employee(self, new_employee=Employee):
		employee_info_list = new_employee.return_all_info_as_list()
		employee_info_string = str()
		for item in employee_info_list:
			employee_info_string += "\""+str(item)+"\", "
		# Strip trailing comma and space
		employee_info_string = employee_info_string[:-2]
		print(employee_info_string)
		query = "insert into employees"+self.employee_fields+" values ("+employee_info_string+")"
		print(query)
		self.con.execute(query)
		self.con.commit()

	def get_employee_list(self):
		employee_query = "select * from employees"
		employee_list = list()
		training_list = list()
		p = PersonalInformation()
		w = WorkInformation()
		cur = self.cur
		cur.row_factory = sqlite3.Row
		for row in cur.execute(employee_query):
			# Employee Information
			p.student_id = row['student_id']
			p.name_first = row['employee_name_first']
			p.name_last = row['employee_name_last']
			p.email = row['employee_email']
			p.phone_number = row['employee_phone_number']
			w.job_type = row['employee_job_type']
			w.date_hire = row['employee_date_hire']
			w.date_graduate = row['employee_date_graduate']
			w.shirt_size = row['employee_shirt_size']
			w.note = row['employee_notes']

			# Training Information to initialize new employee
			training_query = "select * from trainings where student_id="+row['student_id']
			cur.execute(training_query)
			training_list = cur.fetchone()
			# Initialize Employee
			s = Employee(p, w, training_list)
			employee_list.append(s)

		print(employee_list)
		return employee_list

"""
d = DatabaseHandler()

p = PersonalInformation()
p.student_id = "01358308"
p.name_first = "Stephen"
p.name_last = "Reilly"
p.email = "stephencreilly7@gmail.com"
p.phone_number = "9788688473"
w = WorkInformation()
w.job_type = EmployeeType.MANAGER
w.date_hire = "2013-04-01"
w.date_graduate = "2017-05-13"
w.shirt_size = "L"
w.notes = "Great Employee"
t = {"training_aud_sound": True, "training_aud_lights": True, "training_mobile_sound": True, "training_mobile_lights": True, "training_stage_safety": True, "training_commuter_cafe": True, "training_woodland_commons": True, "training_grand_reading_room": True, "training_professionalism": True, "training_x32": True, "training_sound_consoles": True, "training_sound_design": True, "training_amp_speaker_matching": True, "training_advanced_ion": True, "training_lighting_design": True, "training_networking": True, "training_equiptment_repair": True, "training_scenery_shop": True}
e = Employee(p, w, t)

d.add_new_employee(e)
"""
"""
d = DatabaseHandler()

t = {"training_aud_sound": False, "training_aud_lights": False, "training_mobile_sound": False, "training_mobile_lights": False, "training_stage_safety": False, "training_commuter_cafe": False, "training_woodland_commons": False, "training_grand_reading_room": False, "training_professionalism": False, "training_x32": False, "training_sound_consoles": False, "training_sound_design": False, "training_amp_speaker_matching": False, "training_advanced_ion": False, "training_lighting_design": False, "training_networking": False, "training_equiptment_repair": False, "training_scenery_shop": False}
test_data_list = [["01355284", "Lisa", "Blubaugh", "lblubaugh@umassd.edu", "6175550139", "General Staff", "9/1/2014 0:00:00", "4/20/2017 0:00:00", "M", "I'm Lisa"],
["01355226", "Sarah", "Brown", "sbrown12@umassd.edu", "6175550138", "MIT", "9/1/2016 0:00:00", "5/31/2019 0:00:00", "M", "I unplug things"],
["01355227", "Gabii", "Barthe", "gbarthe@umassd.edu", "7742184892", "General Staff", "9/1/2013 0:00:00", "5/31/2017 0:00:00", "M", "I'm Gabii"],
["01354896", "Rachel", "Brownell", "rbrownell@umassd.edu", "6175550193", "General Staff", "9/1/2014 0:00:00", "5/31/2017 0:00:00", "M", "I'm Rachel"],
["01358796", "Nathaniel", "Cady", "ncady@umassd.edu", "6175550114", "General Staff", "9/1/2016 0:00:00", "5/31/2017 0:00:00", "M", "I'm Nate"],
["01357943", "Victoria", "Carter", "vcarter@umassd.edu", "6175550114", "General Staff", "9/1/2014 0:00:00", "5/31/2017 0:00:00", "M", "I'm Tori"],
["01348933", "Josh", "Casseus", "jcasseus@umassd.edu", "6175550181", "General Staff", "9/1/2016 0:00:00", "5/31/2019 0:00:00", "M", "I'm Josh"],
["01358794", "Amandie", "Delva", "adelva@umassd.edu", "6175550104", "General Staff", "9/1/2016 0:00:00", "5/31/2020 0:00:00", "L", "I'm Amandie"],
["01349758", "Amina", "Dualeh", "adualeh@umassd.edu", "6175550176", "General Staff", "9/1/2016 0:00:00", "5/31/2020 0:00:00", "M", "I'm Amina"],
["00135178", "Patrick", "Gouveia", "pgouveia1@umassd.edu", "6175550171", "General Staff", "9/1/2014 0:00:00", "5/31/2018 0:00:00", "L", "I'm Pat"],
["01358008", "Sarah", "Grasso", "sgrasso@umassd.edu", "6175550104", "General Staff", "9/1/2016 0:00:00", "5/31/2020 0:00:00", "S", "I'm Sarah"],
["01346985", "Emily", "Hatstat", "ehatstat@umassd.edu", "6175550177", "MIT", "9/1/2016 0:00:00", "5/31/2019 0:00:00", "M", "I'm a dumbass"],
["01321486", "Nicole", "Howell", "nhowell1@umassd.edu", "6175550119", "MIT", "9/1/2014 0:00:00", "5/31/2018 0:00:00", "L", "I'm Nicole"],
["01354712", "Ross", "Jacques", "rjacques@umassd.edu", "6175550197", "General Staff", "9/1/2016 0:00:00", "5/31/2020 0:00:00", "L", "I'm Ross"],
["01358913", "Christina", "Luby", "cluby@umassd.edu", "6175550177", "General Staff", "9/1/2016 0:00:00", "5/31/2020 0:00:00", "M", "I'm Christina"],
["01354614", "Sara", "Mahan", "smahan@umassd.edu", "6175550126", "General Staff", "9/1/2014 0:00:00", "5/31/2019 0:00:00", "M", "I'm Sara"],
["01347815", "Courtney", "Mitchell", "cmitchell@umassd.edu", "6175550112", "General Staff", "9/1/2016 0:00:00", "5/31/2020 0:00:00", "M", "I'm Cortney"],
["01324816", "Marcus", "Nelson", "mnelson5@umassd.edu", "6175550178", "General Staff", "9/1/2014 0:00:00", "5/31/2018 0:00:00", "L", "I'm Marcus"],
["01352417", "Linda", "Nguyen", "lnguyen@umassd.edu", "6175550110", "General Staff", "9/1/2016 0:00:00", "5/31/2020 0:00:00", "S", "I'm Linda"],
["01326818", "Kyle", "Pacheco", "kpacheco@umassd.edu", "6175550195", "General Staff", "9/1/2016 0:00:00", "5/31/2019 0:00:00", "XL", "I'm Kyle"],
["01357819", "Jay", "Patel", "jpatel@umassd.edu", "6175550107", "General Staff", "9/1/2016 0:00:00", "5/31/2018 0:00:00", "XL", "I'm Jay!"],
["01345620", "Nolan", "Raymond", "nraymon@umassd.edu", "6175550185", "General Staff", "9/1/2013 0:00:00", "5/31/2017 0:00:00", "L", "I don't even work here"],
["01369421", "Sofia", "Repuccia", "srepuccia@umassd.edu", "6175550132", "General Staff", "9/1/2013 0:00:00", "5/31/2017 0:00:00", "L", "I'm Sofia"],
["01357823", "Seth", "Rossie", "srossie@umassd.edu", "6175550159", "General Staff", "9/1/2016 0:00:00", "5/31/2017 0:00:00", "L", "I'm Seth"],
["01384624", "Ehasanuzzama", "Satu", "esatu@umassd.edu", "6175550173", "General Staff", "9/1/2016 0:00:00", "5/31/2017 0:00:00", "M", "I'm Satu"]]

for employee in test_data_list:
	p = PersonalInformation()
	p.student_id = employee[0]
	p.name_first = employee[1]
	p.name_last = employee[2]
	p.email = employee[3]
	p.phone_number = employee[4]
	w = WorkInformation()
	if employee[5] == "MIT":
		w.job_type = EmployeeType.MANAGER_IN_TRAINING
	else:
		w.job_type = EmployeeType.GENERAL
	w.date_hire = employee[6]
	w.date_graduate = employee[7]
	w.shirt_size = employee[8]
	w.notes = employee[9]
	e = Employee(p, w, t)
	d.add_new_employee(e)

print("Completed Process")
"""
