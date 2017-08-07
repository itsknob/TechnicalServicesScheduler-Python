import tkinter as tk
from tkinter import ttk, Tk
from tkinter import *
import TechTypes
from DatabaseHandler import DatabaseHandler

class MainApp(tk.Frame):

	database_handler = DatabaseHandler()

	def __init__(self, master=None):
		super().__init__(master)
		master.minsize(width=800, height=600)
		master.maxsize(width=800, height=600)
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		# Holds Tabs
		self.notebook = ttk.Notebook()

		#####################
		# Create schedule_tab
		#####################
		self.schedule_tab = Frame(self.notebook)

		# Calendar
		# Pane to display calendar
		self.calendar_pane = PanedWindow(self.schedule_tab)
		self.calendar_pane.pack(fill='both', expand=1)
		self.calendar_label = Label(self.calendar_pane, text="Calendar")
		self.calendar_label.pack()

		# Buttons for Testing on Schedule Page
		self.button1 = Button(self.calendar_pane, text="test1")
		self.button1.pack()
		self.button2 = Button(self.calendar_pane, text="test2")
		self.button2.pack()

		# Event Information
		# Pane to display selected event information
		self.event_pane = PanedWindow(self.schedule_tab)
		self.event_pane.pack(fill='both', expand=1, side='left')
		self.event_label = Label(self.event_pane, text="Event Information")
		self.event_label.pack()

		# Buttons for Testing on Schedule Page
		self.button5 = Button(self.event_pane, text="test5")
		self.button5.pack()
		self.button6 = Button(self.event_pane, text="test6")
		self.button6.pack()



		# Employee List
		# Pane to display Employee List
		self.employee_list_schedule_pane = PanedWindow(self.schedule_tab)
		self.employee_list_schedule_pane.pack(fill='both', expand=1, side='right')
		self.employee_list_schedule_label = Label(self.employee_list_schedule_pane, text="Employee List")
		self.employee_list_schedule_label.pack()

		# Buttons for Testing on Schedule Page
		self.button7 = Button(self.employee_list_schedule_pane, text="test7")
		self.button7.pack()
		self.button8 = Button(self.employee_list_schedule_pane, text="test8")
		self.button8.pack()

		#####################
		# Create employee_tab
		#####################
		self.employee_tab = Frame(self.notebook)

		#############
		# Create Area to display employees
		self.employee_pane = PanedWindow(self.employee_tab)
		self.employee_pane.pack(fill='both', expand=1)

		# Create a widget to hold list of employees
		self.employee_list_box_scrollbar = Scrollbar(self.employee_pane)
		self.employee_list_box = Listbox(self.employee_pane)
		self.populate_employee_list_box()
		self.employee_list_box_scrollbar.pack(side='right', fill=Y)
		self.employee_list_box.pack(fill='both', expand=1)

		#############
		# Create Area to show employee information
		self.employee_information_pane = PanedWindow(self.employee_tab)
		self.employee_information_pane.pack(fill='both', expand=1)
		self.employee_information_label = Label(self.employee_information_pane, text="Employee Information")
		self.employee_information_label.pack(side='top')
		# Inner Panes
		self.employee_info_labels_pane = LabelFrame(self.employee_information_pane)
		self.employee_info_labels_pane.pack(fill='x', expand=1, side='left')

		# Labels for each field
		self.label_student_id = Label(self.employee_info_labels_pane, text="Student ID", anchor='w', width=16)
		self.label_full_name = Label(self.employee_info_labels_pane, text="Name", anchor='w', width=16)
		self.label_email = Label(self.employee_info_labels_pane, text="Email", anchor='w', width=16)
		self.label_phone_number = Label(self.employee_info_labels_pane, text="PHone Number", anchor='w', width=16)
		self.label_job_type = Label(self.employee_info_labels_pane, text="Position", anchor='w', width=16)
		self.label_date_hired = Label(self.employee_info_labels_pane, text="Hire Date", anchor='w', width=16)
		self.label_date_graduate = Label(self.employee_info_labels_pane, text="Graduation Date", anchor='w', width=16)
		self.label_shirt_size = Label(self.employee_info_labels_pane, text="Shirt Size", anchor='w', width=16)
		self.label_notes = Label(self.employee_info_labels_pane, text="Notes", anchor='w', width=16)
		# Pack LAbels
		self.label_student_id.pack()
		self.label_full_name.pack()
		self.label_email.pack()
		self.label_phone_number.pack()
		self.label_job_type.pack()
		self.label_date_hired.pack()
		self.label_date_graduate.pack()
		self.label_shirt_size.pack()
		self.label_notes.pack()

		# StringVars for each field, will change depending on active/current listbox selection
		self.employee_id = StringVar()
		self.employee_id = None
		self.employee_name = StringVar()
		self.employee_name = None
		self.employee_email = StringVar()
		self.employee_email = None
		self.employee_phone = StringVar()
		self.employee_phone = None
		self.employee_job = StringVar()
		self.employee_job = None
		self.employee_hired = StringVar()
		self.employee_hired = None
		self.employee_graduate = StringVar()
		self.employee_graduate = None
		self.employee_size = StringVar()
		self.employee_size = None
		self.employee_notes = StringVar()
		self.employee_notes = None

		self.employee_info_data_pane = LabelFrame(self.employee_information_pane)
		self.employee_info_data_pane.pack(fill='x', expand=1, side='right')

		self.data_student_id = Label(self.employee_info_data_pane, text=self.employee_id)
		self.data_full_name = Label(self.employee_info_data_pane, text=self.employee_name)
		self.data_email = Label(self.employee_info_data_pane, text=self.employee_email)
		self.data_phone_number = Label(self.employee_info_data_pane, text=self.employee_phone)
		self.data_job_type = Label(self.employee_info_data_pane, text=self.employee_job)
		self.data_date_hired = Label(self.employee_info_data_pane, text=self.employee_hired)
		self.data_date_graduate = Label(self.employee_info_data_pane, text=self.employee_graduate)
		self.data_shirt_size = Label(self.employee_info_data_pane, text=self.employee_size)
		self.data_notes = Label(self.employee_info_data_pane, text=self.employee_notes)

		self.data_student_id.pack()
		self.data_full_name.pack()
		self.data_email.pack()
		self.data_phone_number.pack()
		self.data_job_type.pack()
		self.data_date_hired.pack()
		self.data_date_graduate.pack()
		self.data_shirt_size.pack()
		self.data_notes.pack()


		###################
		# Add tabs and pack
		self.notebook.add(self.schedule_tab, text="Schedule")
		self.notebook.add(self.employee_tab, text="Employees")
		self.notebook.pack(side="top", padx=5, pady=5, expand=True, fill='both')

		###################
		# End of Widgets  #
		###################

	def populate_employee_list_box(self):
		employee_list = self.database_handler.get_employee_list()
		for e in employee_list:
			print(e.personal_information.name_first)
		for employee in employee_list:
			self.employee_list_box.insert(END, employee.personal_information.name_first+" "+employee.personal_information.name_last+" - "+employee.personal_information.student_id)
		# Packed in __init__()

root = tk.Tk()
root.wm_title("Scheduler")
app = MainApp(master=root)
app.mainloop()
