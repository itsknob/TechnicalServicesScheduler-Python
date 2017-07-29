"""Handles database (students) interaction"""
import sqlite3

""" 
Check for config file.
	if found:
		use database name from config file
	if not found: (else)
		run first_run_function() and set up config file
"""

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

ALL CAN BE TEXT
"""
