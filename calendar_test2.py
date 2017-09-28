# Calendar Testing
from tkinter import *
from TechTypes import Event


class MyApp:

	def __init__(self, master=None):
		self.master = master

		self.master.minsize(width=0, height=900)
		self.master.maxsize(width=1600, height=900)

		# MainFrame
		self.master_frame = Frame().pack()

		# Canvas and Scroll bar for said Canvas
		self.vscrollbar = Scrollbar(self.master_frame, orient="vertical")
		self.vscrollbar.pack(fill='y', side="right", expand=False)
		self.master_canvas = Canvas(self.master_frame, bd=0, highlightthickness=0, yscrollcommand=self.vscrollbar.set)
		self.master_canvas.pack(fill="both", side="left", expand=True)
		self.vscrollbar.config(command=self.master_canvas.yview)

		# Create window for weekly view
			# Reset View
		self.master_canvas.xview_moveto(0)
		self.master_canvas.yview_moveto(0)

		""" 
			Following Two Lines and two functions from EugeneBakin on github 
		https://gist.github.com/EugeneBakin/76c8f9bcec5b390e45df#file-scrframe-py-L49
		"""
		self.weekly_view_frame = interior = Frame(self.master_canvas)
		interior_id = self.master_canvas.create_window(0, 0, window=interior, anchor="nw")
		
		def config_interior(event):
			#update scrollbars
			size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
			self.master_canvas.config(scrollregion="0 0 %s %s"%size)
			if interior.winfo_reqwidth() != self.master_canvas.winfo_width():
				#update width to fit frame
				self.master_canvas.config(width=interior.winfo_reqwidth())
		interior.bind('<Configure>', config_interior)

		def config_canvas(event):
			if interior.winfo_reqwidth() != self.master_canvas.winfo_width():
				# update width to fill canvas
				self.master_canvas.itemconfigure(interior_id, width=self.master_canvas.winfo_width())
		self.master_canvas.bind('<Configure>', config_canvas)

		#~~~~~~~~~
		# Scrollwheel Functionality
		def on_mousewheel(event):
			self.master_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

		self.master_canvas.bind_all('<MouseWheel>', on_mousewheel)
		self.master_canvas.bind_all('<Button-4>', on_mousewheel)
		self.master_canvas.bind_all('<Button-5>', on_mousewheel)

		# Width Variables
		self.widget_height = 2
		self.label_width = 24
		self.button_width = 24
		self.half_button_width = 12
		self.third_button_width = 8
		self.quarter_button_width = 6

		tuple_list = list()
		event_list = list()

		# How it would be created from hours parser.
		test_event0 = Event("Test Event", "Woodlands", "April 20 2017", "09:00", "23:00", "4", False)
		test_event1 = Event("CIE Shift", "CIE", "April 19 2017", "07:30", "13:00", "1", False)
		test_event2 = Event("Makeup Accepted Students Day", "Aud", "April 19 2017", "09:30", "15:00", "1", False)
		test_event3 = Event("Sigma Xi", "Living Room", "April 19 2017", "14:00", "16:00", "2", False)
		test_event4 = Event("Poetry Reading", "UClub", "April 19 2017", "15:30", "17:30", "2", False)
		test_event5 = Event("Cathy Plourde", "CCB 149", "April 19 2017", "17:30", "21:00", "1", False)
		test_event6 = Event("Sigma Xi Reception", "GRR", "April 19 2017", "17:30", "20:00", "1", False)
		test_event7 = Event("Dean and Cabinet Meeting", "GRR", "April 20 2017", "08:00", "13:00", "2", False)
		test_event8 = Event("Sigma Xi", "Living Room", "April 20 2017", "11:00", "13:00", "1", False)
		test_event9 = Event("Honors Dinner", "Woodlands", "April 20 2017", "15:00", "20:00", "1", False)
		test_event10 = Event("Awards and ODE Honors - Economics", "UClub", "April 20 2017", "16:00", "18:30", "1", False)
		test_event11 = Event("Civic Leadership Awards Ceremony", "Star Store", "April 20 2017", "16:00", "21:00", "1", False)
		test_event12 = Event("Shake the Ship", "GRR", "April 20 2017", "16:30", "19:30", "1", False)
		test_event13 = Event("Engineering Scholarship Day", "Woodlands", "April 21 2017", "14:30", "17:00", "1", False)
		test_event14 = Event("Pi Sigma Alpha Honors Induction", "GRR", "April 21 2017", "15:30", "18:00", "1", False)
		test_event15 = Event("Relay for Life", "Quad", "April 22 2017", "09:00", "17:30", "5", False)
		test_event16 = Event("Relay for Life", "Quad", "April 22 2017", "17:30", "02:00", "5", False)
		test_event17 = Event("Psi Chi Induction Ceremony", "GRR", "April 23 2017", "13:30", "16:00", "1", False)
		test_event18 = Event("2 Woodlands Events", "Woodlands", "April 24 2017", "15:30", "18:00", "1", False)
		test_event19 = Event("Arnie Talks", "GRR", "April 24 2017", "15:30", "17:30", "1", False)
		test_event20 = Event("Navitas End of Term Gala Rehearsal", "Aud", "April 24 2017", "17:00", "21:00", "4", False)
		test_event21 = Event("Promise of Religious Environmentalism", "Aud", "April 25 2017", "13:00", "15:30", "1", False)
		test_event22 = Event("3 Minute Thesis", "Woodlands", "April 25 2017", "13:00", "14:00", "1", False)
		test_event23 = Event("Sister Madeline Award Ceremony", "GRR", "April 25 2017", "14:30", "19:00", "1", False)
		test_event24 = Event("Bingo Night", "CC", "April 25 2017", "16:30", "22:00", "1", False)
		test_event25 = Event("Navitas End of Term Gala Show", "Aud", "April 25 2017", "17:00", "21:00", "4", False)
		event_list = [test_event0, test_event1, test_event2, test_event3, test_event4, test_event5, test_event6, test_event7,
					  test_event8, test_event9, test_event10, test_event11, test_event12, test_event13, test_event14, test_event15,
					  test_event16, test_event17, test_event18, test_event19, test_event20, test_event21, test_event22, test_event23,
					  test_event24, test_event25]

		days = {1:"Sunday", 2:"Monday", 3:"Tuesday", 4:"Wednesday", 5:"Thursday", 6:"Friday", 7:"Saturday"}

		times = {0:"00:00",  1:"00:30",  2:"01:00",  3:"01:30",  4:"02:00",  5:"02:30",  6:"03:00",  7:"03:30",
				 8:"04:00",  9:"04:30", 10:"05:00", 11:"05:30", 12:"06:00", 13:"06:30", 14:"07:00", 15:"07:30", 
				16:"08:00", 17:"08:30", 18:"09:00", 19:"09:30",	20:"10:00", 21:"10:30", 22:"11:00", 23:"11:30", 
				24:"12:00", 25:"12:30", 26:"13:00", 27:"13:30",	28:"14:00", 29:"14:30", 30:"15:00", 31:"15:30", 
				32:"16:00", 33:"16:30", 34:"17:00", 35:"17:30",	36:"18:00", 37:"18:30", 38:"19:00", 39:"19:30", 
				40:"20:00", 41:"20:30", 42:"21:00", 43:"21:30",	44:"22:00", 45:"22:30", 46:"23:00", 47:"23:30"}


		# Create tuple_list of start and end coordinate for each event as a single tuple of two tuples.
		# tuple_list = [((r_start1, c_start1), (r_end1, c_end1)), ...]
		for event in event_list:
			tuple_list.append(self.findCoordinateRange(event, times))
		print(tuple_list)
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

		############
		# Handle two events occupying the same space.
		#################### Information should be able to be found from tuple_list

		# print(tuple_list)

		r_min = 1					# Minimum Time
		r_max = len(times)			# Maximum Time
		# Genenerate inital weekly calendar layout (only Labels), this may later need to have a scroll bar. 
				# Second thought, it will definitely need a scrollbar for final product.


		for column in range(len(days)+1): # Days of the Week
			for row in range(len(times)): # Time Slots
				if column is 0:
					if row is 0: # Top Left Corner - No Label or Button
						# print(times[row])
						continue
					#print("R:%s, C:%s"%(row, column))
					#print("Times[row]: ", times[row])
					#Label(self.weekly_view_frame, text=times[row], width=16, borderwidth=2).grid(row=row, column=column)			
				
				# Create Labels for Days
				if row is 0:
					Label(self.weekly_view_frame, text=days[column], width=self.label_width, height=self.widget_height, borderwidth=0).grid(row=row, column=column)	
				# Create Buttons for everything else.
				else:
					# Label Times in Leftmost Column
					if column is 0:
						Label(self.weekly_view_frame, text=times[row], width=self.label_width, height=self.widget_height, borderwidth=0).grid(row=row, column=column)
					# Label Grid Location from (1, 1) to (47, 7)
					else:
						#Frame(self.weekly_view_frame, width=self.label_width, borderwidth=2, background="red").grid(row=row, column=column)
						Label(self.weekly_view_frame, text="R-%s, C-%s"%(row, column), width=self.label_width, height=self.widget_height, borderwidth=0).grid(row=row, column=column)
															#, command=lambda r=row, c=column: print("%s, %s"%(r, c))

		# Generate list of slaves from newly created calendar view.
		slaves = self.weekly_view_frame.grid_slaves()

		# Removed Labels and Create Event Buttons
		for column in range(len(days)+1):
			for row in range(len(times)):
				# Thought: Create list of tuple of tuples, [((starting1), (end1)), ((start), (end2))]
				# In order to not create elements on calendar, check to see if an event is already in that range
				#	Raises issue of multiple events at the same time.
				for outer_tuple in tuple_list:
					start_tuple, end_tuple = outer_tuple # Runs once for each outer_tuple
					# Precheck that touples have the same column || Raises issue of events spanning past midnight.
					r_start, c_start = start_tuple	# Runs once per start_tuple

					#print("Tl", tuple_list.index(outer_tuple))
					#print("s/e", start_tuple, end_tuple)
					#print("s/e I", r_start, c_start)

					if row == r_start and column == c_start:
						# There is an event that starts here, we want to find out how long it is (rowspan)
						r_end, c_end = end_tuple	# Runs once per end_tuple
						if r_end - r_start < 1:
							# Range is 0 or negative, event takes no time or goes back in time
							# This might be where multi day events are handled
								# Check Columns, maybe create label here for such events
								# Create r_start to r_max for c_start,
									# Then create r_min to r_end for c_start+1

							# IE ((35, 7), (4, 7)) - 17:30(p) - 02:00(a)

							rowspan_first_day = r_max - r_start
							rowspan_second_day = r_end


							# Remove widgets from start to end of day.
							slaves = self.weekly_view_frame.grid_slaves()
							self.removeWidgets(r_start, r_max, c_start, rowspan_first_day, slaves)

							# Remove widgets from start of day to end of event.
							slaves = self.weekly_view_frame.grid_slaves()
							self.removeWidgets(r_min, r_end, c_end, rowspan_second_day, slaves)

							# print(slaves)


							Button(self.weekly_view_frame, text=event_list[tuple_list.index(outer_tuple)].event_name, width=self.button_width, wraplength=128, justify="left", command=lambda t=event_list[tuple_list.index(outer_tuple)].event_name: print(t)).grid(row=r_start, column=c_start, rowspan=rowspan_first_day, sticky="NS")
							Button(self.weekly_view_frame, text=event_list[tuple_list.index(outer_tuple)].event_name+" cont.", width=self.button_width, wraplength=128, justify="left", command=lambda t=event_list[tuple_list.index(outer_tuple)].event_name: print(t)).grid(row=r_min, column=c_end, rowspan=rowspan_second_day, sticky="NS")
							# RE-Generate list of slaves from newly created calendar view.
							slaves = self.weekly_view_frame.grid_slaves()

							print("Placed Overnight Button starting at ({0}, {1}) [to the end of the day] and ending at ({2}, {3}) [from the start of the (next) day]".format(r_start, c_start, r_end, c_end))

							print("~~~~~")
						
						# Event takes a valid ammount of time
								# 		if row == r_start and column == c_start:		#
						else: 


							"""
							rowspan = r_end - r_start # At least 1 (30 minutes)

							# Remove Widgets in locations event button will be placed
							slaves = self.weekly_view_frame.grid_slaves()
							self.removeWidgets(r_start, r_end, column, rowspan, slaves)

							# There is an event here, we want to create a Button using rowspan
							Button(self.weekly_view_frame, text=event_list[tuple_list.index(outer_tuple)].event_name, width=self.button_width, wraplength=128, justify="left", command=lambda t=event_list[tuple_list.index(outer_tuple)].event_name: print(t)).grid(row=r_start, column=c_start, rowspan=rowspan, sticky="NS")
							print("Placed Button for {3:.16} at: ({0}, {1}) with a span of: {2}".format(row, column, rowspan, event_list[tuple_list.index(outer_tuple)].event_name))
							# RE-Generate list of slaves from newly created calendar view.
							slaves = self.weekly_view_frame.grid_slaves()
							"""



							#print("############### r_start: {0}, r_end: {1}, c_start: {2} ###############".format(r_start, r_end, c_start))
							# This is starting at the beginning of button to be placed.
							# So if there is a button, that already exists, where this button is about to be placed
							# We need to create the frame from the button that already exists or the one being place, which ever is ealier.
							for this_object in slaves:
								# Check to see if there is a frame with multiple buttons first, 			
								#																			(|           Frame          |)
								# if there's multiple buttons,												(|   Frame     |   Frame    |)
									# put that two button frame AND a frame for the button into a new frame (| Event| Event|   Event    |)
								#
								# otherwise keep going with this code.
								if type(this_object) is Frame:
									print("#####Frame")

								if type(this_object) is Button:	# this_object is a Button that already exists, we're about to place another.
									print("##Button")
									old_button = this_object
									old_button_info = old_button.grid_info()
									# If button exists where this other button already is is
									if old_button_info['row'] in range(r_start, r_end):
										print("\t", old_button_info)
										print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
										print("New Button Row Start/End: {0}/{1}".format(r_start, r_end))
										print("New Button:", event_list[tuple_list.index(outer_tuple)].event_name)
										print("Old Button: ", end='')
										old_button.invoke()
										print("Old Button Row Start/End: {0}/{1}".format(old_button_info['row'], old_button_info['row']+old_button_info['rowspan']))
										# Find out which one starts earlier.
										# New Event Starts Earlier (r_start is new button's start)
										if r_start <= old_button_info['row']:
											print("\t\tNew Event Starts Ealier")
											# Find out which one ends later, use this to create a frame of rowspan of difference
											new_frame_start = r_start # Friendly Name for frame that will be created.

											# New Event ends ealier (shorter) - Use Old Event ending
											if r_end < old_button_info['row']+old_button_info['rowspan']:
												new_frame_end = old_button_info['row']+old_button_info['rowspan']
												print("Old longer")
											
											# New Event ends later or equal (longer, or same length)
											else:
												new_frame_end = r_end
												print("New Longer")

											# Calculate Frame Span
											new_frame_rowspan = new_frame_end - new_frame_start

											# Create Frame to put both event in and Remove widgets from spaces where
											print("CREATING NEW FRAME from: r - {0} to r - {1} @ c - {2}".format(new_frame_start, new_frame_end, c_start))
											print("c_start", c_start)
											self.removeWidgets(new_frame_start, new_frame_end, c_start, new_frame_rowspan, slaves)
											# Create Frame where widgets were removed from
											self.two_event_frame = Frame(self.weekly_view_frame, width=self.button_width-2, borderwidth=1, relief="groove")# .grid(row=new_frame_start, column=c_start, rowspan=new_frame_rowspan)
											# Old Event
											first_button = Button(self.two_event_frame, text="testing left", width=self.half_button_width-1).grid(row=old_button_info['row'], column=c_start, rowspan=old_button_info['rowspan'], sticky="NS")
											# New Event
											second_button = Button(self.two_event_frame, text="testing right", width=self.half_button_width-1).grid(row=new_frame_start, column=c_start+1, rowspan=new_frame_rowspan, sticky="NS")

																			# Commenting out this grid call prints buttons to window.
											self.two_event_frame.grid(row=new_frame_start, column=c_start, rowspan=new_frame_rowspan, sticky="ns")

											# Remake slaves now that it's changed.
											slaves = self.weekly_view_frame.grid_slaves()
											
											# Break out of slaves loop.
											#break

										# Old Event Starts Earlier
										elif r_start > old_button_info['row']: # Never Happens because we're looping by day then by time.
											print("\t\tOld Event Starts Ealier")


										print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
								
							
							rowspan = r_end - r_start # At least 1 (30 minutes)

							# Remove Widgets in locations event button will be placed
							slaves = self.weekly_view_frame.grid_slaves()
							self.removeWidgets(r_start, r_end, column, rowspan, slaves)

							# There is an event here, we want to create a Button using rowspan
							Button(self.weekly_view_frame, text=event_list[tuple_list.index(outer_tuple)].event_name, width=self.button_width, wraplength=128, justify="left", command=lambda t=event_list[tuple_list.index(outer_tuple)].event_name: print(t)).grid(row=r_start, column=c_start, rowspan=rowspan, sticky="NS")
							print("Placed Button for {3:.16} at: ({0}, {1}) with a span of: {2}".format(row, column, rowspan, event_list[tuple_list.index(outer_tuple)].event_name))
							# RE-Generate list of slaves from newly created calendar view.
							slaves = self.weekly_view_frame.grid_slaves()
							
					
					# There is no event here, we want to create an empty label.				
					else:
						# Do existing logic for creating calendar view
						continue # Runs start tuple once, moved on to next outer_tuple
						# May want to use break to ensure this ends the start_tuple loop


		# Whole function may need to be run after all labels are created 
		# in order to overwrite labels, and not be overwriten by them.

	def findCoordinateRange(self, event, times):
		# Take in event (provides date [needs to be turned into Day of the Week] and Start-time and End-time)

		# Find out day of week based on date
		import datetime
		event_datetime = datetime.datetime.strptime(event.event_date, "%B %d %Y")
		weekday = event_datetime.weekday() # 0 is for Monday
		# Adjust weekday value for calendar grid
		weekday = weekday + 2 # 2 is NOW for Monday, 1 is NOW for Sunday
		
		# Set (fixed) weekday index to readable variable.
		grid_column_start = weekday	# For Placement on Calendar

		#~~~~~~~~~~~~~~~~~~~#

		# Find out start and end times, map those to dictionary <times>
		grid_row_start = event.event_start_time		# e.g. 06:00
		grid_row_end = event.event_end_time

		# Get values of time dictionary, indecies will line up.
		times_values = list(times.values())

		# Get Row Start and End Positions (Times)
		grid_row_start_index = times_values.index(grid_row_start)
		grid_row_end_index = times_values.index(grid_row_end)

		# Check for event that goes past midnight
		if grid_row_end_index <= grid_row_start_index: # End is smaller than or equal to start
			grid_column_end = grid_column_start+1
		else: # Otherwise event should end in same column
			grid_column_end = grid_column_start

		# Ensure that (overnight) events wrap properly on calendar
		if grid_column_start%8 is 0:
			grid_column_start = 1
		if grid_column_end%8 is 0:
			grid_column_end = 1

		# Create tuples for start and end of event
		start_tuple = (grid_row_start_index, grid_column_start)
		end_tuple = (grid_row_end_index, grid_column_end)

		# Create Tuple to describe the entire event
		event_tuple = (start_tuple, end_tuple)

		return event_tuple

	def removeWidgets(self, r_start, r_end, column, rowspan, slaves):
		# print("r_start: {0}, r_end: {1}".format(r_start, r_end))
		for obj in slaves:
			if int(obj.grid_info()["row"]) >= r_start and int(obj.grid_info()["row"]) < r_end and int(obj.grid_info()["column"]) == column:
				if type(obj) is Button:
					print("Obj (is Button) Row: {0}, Obj Col: {1}".format(obj.grid_info()['row'], obj.grid_info()['column']))
					row = obj.grid_info()["row"]
				print("Removed widget at ({0}, {1}) of type {2}.".format(obj.grid_info()['row'], column, type(obj)))
				obj.grid_forget()


root = Tk()
my_app = MyApp(root)
root.mainloop()