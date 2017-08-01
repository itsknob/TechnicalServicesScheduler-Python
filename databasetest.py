"""Database testing"""

import sqlite3 # No enum type
from TechTypes import Student

# Database name should be kept in config file.
connection = sqlite3.connect("test.db")

cursor = connection.cursor()

"""
student_id 				-				INTEGER
student_name_first 		-				TEXT
student_name_last		-				TEXT
student_job_type		-				TEXT
student_phone_number	-				INTEGER/TEXT
student_email			-				TEXT
student_date_hire		-				TEXT - Datetime?		
student_date_graduate 	- 				TEXT - Datetime?
student_shirt_size		-				TEXT
student_notes			-				TEXT

"""


test = Student("01358308", 'Stephen', 'Reilly', 'manager', "9788688473", "sreilly@umassd.edu", "2013-04-01", "2017-05-07", 'L', "Best employee we've ever had.")
sql_values = test.return_all_data_as_string()


connection.execute("""create table if not exists employees (student_id varchar(8) primary key,
											student_name_first varchar(32),
											student_name_last varchar(32),
											student_job_type varchar(8),
											student_phone_number integer,
											student_email varchar(64),
											student_date_hire date,
											student_date_graduate date,
											student_shirt_size varchar(4),
											student_notes varchar(255))""")

# sql_statement = """insert into employees (student_id, student_name_first, student_name_last, student_job_type, student_phone_number, student_email, student_date_hire, student_date_graduate, student_shirt_size, student_notes) values(01358308, 'Stephen', 'Reilly', 'manager', 9788688473, 'sreilly@umassd.edu', '2013-04-01', '2017-05-07', 'L', "Best employee we've ever had.")"""
sql_fields = (student_id, student_name_first, student_name_last, student_job_type, student_phone_number, student_email, student_date_hire, student_date_graduate, student_shirt_size, student_notes)
connection.execute("insert into employees ({}) values(?)".format(sql_fields), sql_values)
# print(sql_statement)
# sql_statement = "insert into employees ({0}) values({1})".format(sql_fields, sql_values)
print(sql_statement)
connection.execute(sql_statement)
connection.commit()

connection.close()


"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
'''
import pymysql.cursors

connection = pymysql.connect(db='test.db')

try:
	with connection.cursor() as cursor:
		sql_statement = """create table employees (student_id integer primary key,
						 					student_name_first varchar(32),
											student_name_last varchar(32),
											student_job_type enum('general', 'mit', 'manager'),
											student_phone_number integer,
											student_email varchar(64),
											student_date_hire date,
											student_date_graduate date,
											student_shirt_size enum('XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL'),
											student_notes varchar(255))"""
		cursor.execute(sql_statement)
	# Does not commit automatically
	cursor.commit()

finally:
	connection.close()
'''

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""