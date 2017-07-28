from tkinter import *
import tkinter
import HoursParser


class UserInterface(tkinter.Frame):

    def __init__(self, master):
        self.master = master
        self.events_list = []

        # Set window size
        master.minsize(width=800, height=600)
        master.maxsize(width=800, height=600)

        # File Parser
        self.parser = HoursParser.FileParser()

        # Filename Label
        self.file_select_text = tkinter.StringVar()
        self.file_select_text.set(" ")

        # Initialize Widgets
        super().__init__(master)
        self.pack()

        # Label for Application
        self.title_label = LabelFrame(master, text="Technical Services - Scheduler (Alpha)")
        self.title_label.pack(fill="both", expand="yes")
        self.inner_label = Label(self.title_label, text="Choose Hours File")
        self.inner_label.pack()

        # Button for File Selection
        self.file_select_button = Button(self.title_label, text="Select File", command=lambda: self.file_button_press())
        self.file_select_button.pack()

        # Label for File Selection Button
        self.file_select_label = Label(self.title_label, textvariable=self.file_select_text)
        self.file_select_label.pack()

        # Button for Parsing File
        self.file_parse_button = Button(self.title_label, state=DISABLED, text="Read File", command=lambda: self.parse_button_pressed())
        self.file_parse_button.pack()

        # List of Events
        self.events_list_box = Listbox(self.title_label)
        self.events_list_box.pack()

        # Show Info Button
        self.show_info_button = Button(self.title_label, state="disabled", command=lambda: self.show_event_info())
        self.show_info_button.pack()

        # Shows information about event
        self.text_area = Text(self.title_label)
        self.text_area.pack()

    # Called when Select File button is pressed.
    def file_button_press(self):
        self.parser.choose_file()
        self.file_select_text.set(self.parser.file_name)
        if self.parser.file_name is not None:
            self.file_parse_button['state'] = 'normal'

    def parse_button_pressed(self):
        self.events_list = self.parser.parse_file()
        self.populate_list_box(self.events_list_box)

    # Puts names of events in a list from parsed file.
    def populate_list_box(self, list_box):
        i = 0
        for event in self.events_list:
            list_box.insert(i, event.get_event_name())
            i += 1
        self.show_info_button['state'] = 'normal'

    def show_event_info(self):
        # Store Active Time Index
        event_list_index = int(self.events_list_box.index(ACTIVE))

        # Clear text box from previous event details
        # if self.text_area.get(END) is not "\n":
        #    self.text_area.delete(0, 'end')

        # Display Formatted Information about Event.
        self.text_area.insert(END, "Event:      " + self.events_list[event_list_index].get_event_name())
        self.text_area.insert(END, '\n')
        self.text_area.insert(END, "Location:   " + self.events_list[event_list_index].get_event_location())
        self.text_area.insert(END, '\n')
        self.text_area.insert(END, "Start Time: " + self.events_list[event_list_index].get_event_start_time())
        self.text_area.insert(END, '\n')
        self.text_area.insert(END, "End Time:   " + self.events_list[event_list_index].get_event_end_time())
        self.text_area.insert(END, '\n')
        self.text_area.insert(END, "# of Staff: " + self.events_list[event_list_index].get_event_number_employees())
        self.text_area.insert(END, '\n')

root = Tk()
root.wm_title("Scheduler (Alpha)")
main_app = UserInterface(master=root)
main_app.mainloop()
