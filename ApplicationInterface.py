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
		self.employee_list_box = Listbox(self.employee_pane, selectmode=MULTIPLE, yscrollcommand=self.employee_list_box_scrollbar.set)
		self.employee_list_box.bind('<<ListboxSelect>>', self.listbox_callback)
		# Populate Listbox from Database
		self.populate_employee_list_box()
		self.employee_list_box_scrollbar.config(command=self.employee_list_box.yview)
		self.employee_list_box_scrollbar.pack(side='right', fill=Y)
		self.employee_list_box.pack(fill='both', expand=1)
		# Variables required to have selection order in listbox
		self.old_selection_list = list() # Previously Selected in Listbox
		self.selected_list = list()	# Currently Selected in Listbox

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
		self.label_phone_number = Label(self.employee_info_labels_pane, text="Phone Number", anchor='w', width=16)
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
		# self.employee_id.set("Test")
		# self.employee_id = None
		# self.employee_id.set(self.all_employee_list[self.employee_list_index])
		self.employee_name = StringVar()
		# self.employee_name = None
		self.employee_email = StringVar()
		# self.employee_email = None
		self.employee_phone = StringVar()
		# self.employee_phone = None
		self.employee_job = StringVar()
		# self.employee_job = None
		self.employee_hired = StringVar()
		# self.employee_hired = None
		self.employee_graduate = StringVar()
		# self.employee_graduate = None
		self.employee_size = StringVar()
		# self.employee_size = None
		self.employee_notes = StringVar()
		# self.employee_notes = None

		self.employee_info_data_pane = LabelFrame(self.employee_information_pane)
		self.employee_info_data_pane.pack(fill='x', expand=1, side='right')

		self.data_student_id = Label(self.employee_info_data_pane, text=self.employee_id.get())
		self.data_full_name = Label(self.employee_info_data_pane, text=self.employee_name.get())
		self.data_email = Label(self.employee_info_data_pane, text=self.employee_email.get())
		self.data_phone_number = Label(self.employee_info_data_pane, text=self.employee_phone.get())
		self.data_job_type = Label(self.employee_info_data_pane, text=self.employee_job.get())
		self.data_date_hired = Label(self.employee_info_data_pane, text=self.employee_hired.get())
		self.data_date_graduate = Label(self.employee_info_data_pane, text=self.employee_graduate.get())
		self.data_shirt_size = Label(self.employee_info_data_pane, text=self.employee_size.get())
		self.data_notes = Label(self.employee_info_data_pane, text=self.employee_notes.get())

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
		self.all_employee_list = self.database_handler.get_employee_list()
		for employee in self.all_employee_list:
			self.employee_list_box.insert(END, employee.personal_information.name_first+" "+employee.personal_information.name_last+" - "+employee.personal_information.student_id)
		# Packed in __init__()

	"""
	def listbox_callback(self, event):
		widget = event.widget
		index = int(widget.curselection()[len(widget.curselection())-1])
		value = widget.get(index)
		self.employee_list_index = index
		print("index: "+str(index)+" value: "+value)
	"""

	def listbox_callback(self, event):
		widget = event.widget
		new_selection_list = list()

		for item in widget.curselection():
			# This is the selected item in the list box, mostly used for size comparison
			new_selection_list.append(item)

		# Required for checking addition or removal to/from listbox
		new_selection_size = len(new_selection_list)
		old_selection_size = len(self.old_selection_list) # Starts at 0

		# If new selection
		if new_selection_size > old_selection_size:
			self.addListItem(new_selection_list)
		# If selection removed
		elif new_selection_size < old_selection_size:
			self.removeListItem(new_selection_list)
		# Error
		else:
			print("Error - No change in list selection")

		# Set new to old
		self.old_selection_list = self.selected_list

		# Change Labels on Display
		self.data_student_id.config(text=self.all_employee_list[self.old_selection_list[-1]].personal_information.student_id) # Name of Employee who's index is the last item in selected list.
		self.updateEmployeeLabels()

	def updateEmployeeLabels(self):
		self.data_student_id.config(text=self.all_employee_list[self.old_selection_list[-1]].personal_information.student_id)
		self.data_full_name.config(text=self.all_employee_list[self.old_selection_list[-1]].get_full_name())
		self.data_email.config(text=self.all_employee_list[self.old_selection_list[-1]].personal_information.email)
		self.data_phone_number.config(text=self.all_employee_list[self.old_selection_list[-1]].personal_information.phone_number)
		self.data_job_type.config(text=self.all_employee_list[self.old_selection_list[-1]].work_information.job_type)
		self.data_date_hired.config(text=self.all_employee_list[self.old_selection_list[-1]].work_information.date_hire)
		self.data_date_graduate.config(text=self.all_employee_list[self.old_selection_list[-1]].work_information.date_graduate)
		self.data_shirt_size.config(text=self.all_employee_list[self.old_selection_list[-1]].work_information.shirt_size)
		self.data_notes.config(text=self.all_employee_list[self.old_selection_list[-1]].work_information.notes)

	# When the size of new_selection_list is greater than the size of currently selected.
	def addListItem(self, new_selection_list):
		# Go through items in new list
		for item in new_selection_list:
			# If item is not in old list, it's new. Add it to the list.
			if item not in self.old_selection_list:
				self.selected_list.append(item)
			# Otherwise item is in old list, it was already selected.

	# When the size of new_selection_list is less than the size of currently selected.
	def removeListItem(self, new_selection_list):
		# Go through items in old list
		for item in self.old_selection_list:
			# If item is not in new list, it's been removed.
			if item not in new_selection_list:
				self.selected_list.remove(item)
			# Otherwise item is in new list, it is still selected.


root = tk.Tk()
root.wm_title("Scheduler")
app = MainApp(master=root)
app.mainloop()
