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
		cur = self.cur
		cur.row_factory = sqlite3.Row
		cur.execute(employee_query)
		rows = cur.fetchall()
		for row in rows:
			p = PersonalInformation()
			w = WorkInformation()
			# Employee Information
			p.student_id = str(row['student_id'])
			p.name_first = str(row['employee_name_first'])
			p.name_last = str(row['employee_name_last'])
			p.email = str(row['employee_email'])
			p.phone_number = str(row['employee_phone_number'])
			w.job_type = str(row['employee_job_type'])
			w.date_hire = str(row['employee_date_hire'])
			w.date_graduate = str(row['employee_date_graduate'])
			w.shirt_size = str(row['employee_shirt_size'])
			w.notes = str(row['employee_notes'])

			# Training Information to initialize new employee
			training_query = "select * from trainings where student_id="+str(row['student_id'])
			cur.execute(training_query)
			training_list = cur.fetchone()
			# Initialize Employee
			s = Employee(p, w, training_list)
			employee_list.append(s)

		return employee_list
