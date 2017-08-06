"""Student Handler Refactor"""
import sqlite3
import os.path
from TechTypes import *


class DatabaseHandler:

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
											student_name_first varchar(32),
											student_name_last varchar(32),
											student_job_type varchar(8),
											student_phone_number integer,
											student_email varchar(64),
											student_date_hire date,
											student_date_graduate date,
											student_shirt_size varchar(4),
											student_notes varchar(255))""")
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

	def add_new_student(self, new_student=Student):
		student_info_list = new_student.return_all_info_as_list()
		print(student_info_list)

p = PersonalInformation()
p.name_first = "Stephen"
p.name_last = "Reilly"
p.email = "stephencreilly7@gmail.com"
p.phone_number = "9788688473"
w = WorkInformation()
w.student_id = "01358308"
w.job_type = EmployeeType.MANAGER
w.date_hire = "2013-04-01"
w.date_graduate = "2017-05-13"
w.shirt_size = "L"
w.notes = "Great Employee"
t = {"training_aud_sound": True, "training_aud_lights": True, "training_mobile_sound": True, "training_mobile_lights": True, "training_stage_safety": True, "training_commuter_cafe": True, "training_woodland_commons": True, "training_grand_reading_room": True, "training_professionalism": True, "training_x32": True, "training_sound_consoles": True, "training_sound_design": True, "training_amp_speaker_matching": True, "training_advanced_ion": True, "training_lighting_design": True, "training_networking": True, "training_equiptment_repair": True, "training_scenery_shop": True}
s = Student(p, w, t)

d = DatabaseHandler()
d.add_new_student(s)