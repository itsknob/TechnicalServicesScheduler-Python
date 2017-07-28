from TechStuff import Event
import re

class FileParser:

    file_name = None

    def choose_file(self):
        from tkinter import Tk
        from tkinter.filedialog import askopenfilename

        Tk().withdraw()
        self.file_name = askopenfilename()

    def parse_file(self):
        # Read all lines into a list
        file = open(self.file_name)
        lines = file.readlines()
        file.close()

        event_flag = False
        event_list = []
        new_event = []

        for line in lines:
            # print(line)
            if re.search('^[A-Z][a-z]{5,8},.*', line) is not None:
                date = line
                event_flag = True
                # print(date)
            elif line.startswith("Scott"):
                break
            elif len(line) > 3 and event_flag:
                # Split line on Colon
                tag, content = line.split(sep=':', maxsplit=1)

                # Strip New Line from content
                content = content[:-1]
                # print("|" + tag + "| - |" + content[:-1] + "|")

                if tag == "Title":
                    name = content
                    new_event.append(content)
                    new_event_flag = True
                    # print(name)
                elif tag == "Venue":
                    location = content
                    new_event.append(content)
                    # print(location)
                elif tag == "Time":
                    # Split into separate times.
                    start_time, end_time = content.split(sep='â€“', maxsplit=1)

                    # Format Each String
                    start_string = str(start_time)
                    space, start_string1, start_string2 = start_string.split(" ", maxsplit=2)

                    end_string = str(end_time)
                    space, end_string1, end_string2 = end_string.split(" ", maxsplit=2)

                    new_event.append(start_string1)
                    new_event.append(end_string1)
                elif tag == "Staff":
                    num_employees = content[:-6]
                    # print(num_employees)
                    new_event.append(content[:-6])

                    '''
                    e = Event(name, location, date, start_string1, end_string1, num_employees, False)
                    # print("Event Name: " + temp.get_event_name())
                    event_list.append(e)
                    '''
                """
                # Fix this
                if new_event[0] is not None:
                    print(new_event[0])
                    for item in new_event:
                        print(item)
                        print(len(new_event))
                """

            else:
                continue

        # Clean up formatting
        for i in range(len(new_event)):
            # Remove Space at beginning of lines
            if new_event[i][0] == " ":
                new_event[i] = new_event[i][1:]

        # Create Events and place into an array
        while len(new_event) >= 5:
            e = Event(new_event[0], new_event[1], None, new_event[2], new_event[3], new_event[4], False)
            new_event = new_event[5:]
            event_list.append(e)

        # Event Object List
        return event_list
