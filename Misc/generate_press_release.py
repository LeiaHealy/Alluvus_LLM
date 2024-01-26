import sys
import pandas as pd
import numpy as np
import openai
import json
from docx import Document
import os
import requests
from dotenv import load_dotenv
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox, QApplication
from Automated_PressRelease.press_release_gui import PressReleaseGUI
load_dotenv()

# def gpt_press_release(filename, announcement, info_array, boilerplate):
#     #TODO Note that info is now an ARRAY so you need to take that into account in either
#     #     the function, or just manually unpack and add as string.
#     std_press_release_func = {
#             "name": "gen_press_release",
#             "description": "Generate a standard press release.",
#             "parameters": {
#                 "type": "object",
#                 "properties": {
#                     "press_release": {
#                         "type": "string",
#                         "description": "The press release generated from the info given",
#                     },
#                 },
#                 "required": ["press_release"],
#             }
#         }
    
#     info = ""
#     for ln in info_array:
#         info += '\n' + str(ln)
#     content = f"""Generate a press release regarding {announcement}. 
#     Additional info to include: {info}. 
#     Boilerplate: {boilerplate}"""
#     r = openai.ChatCompletion.create(
#         model="gpt-4",
#         temperature=0.0,
#         messages=[{"role": "user", "content": content}],
#         functions=[std_press_release_func],
#     )
#     output_str = r.choices[0]['message']['function_call']['arguments']
#     convert_to_docx(filename, output_str, 0)
#     print(f'Finished generating {filename}')

# def gpt_media_advisory(filename, announcement, what, where, when, event_overview, boilerplate):
#     # print(
#     # f'Filename: {filename}\n'
#     # f'announcement: {announcement}\n'
#     # f'what: {what}\n'
#     # f'where: {where}\n'
#     # f'when: {when}\n'
#     # f'Event Overview: {event_overview}\n'
#     # f'Boilerplate: {boilerplate}'
#     # )
#     when_info = ""

#     media_advisory_func = {
#         "name": "gen_media_advisory",
#         "description": "Generate a document consolidating the given media advisory information",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "consolidated_doc": {
#                     "type": "string",
#                     "description": """Media Advisory is bold and the title. Underneath, also bolded, is the announcement to be made. 
#                     There will then be a "What", "Where", and "When" section, where each will have their own section. 
#                     e.g. What:/t [what is happening]. "When" can have multiple sections. e.g. one event that is 
#                     from 8:00am to 6:00pm, or it can have multiple, overlapping events. Underneath all of this, 
#                     there is the event overview section. Finally, tack on the boilerplate at the end.""",
#                 },
#             },
#             "required": ["consolidated_doc"],
#         }
#     }

#     for ln in when:
#         when_info += '\n' + str(ln)
#     content = f"""Generate a media advisory announcing {announcement}.
#     what:{what}, where:{where}, when:{when_info}.
#     Event overview: {event_overview}
#     Boilerplate: {boilerplate}"""

#     r = openai.ChatCompletion.create(
#         model="gpt-4",
#         temperature=0.0,
#         messages=[{"role": "user", "content": content}],
#         functions=[media_advisory_func],
#     )
#     output_str = r.choices[0]['message']['function_call']['arguments']
#     print(f"AI OUTPUT\n#################################\n {r}\n\n#################################\nOUTPUT STRING: \n#################################\n{output_str}\n######################")
#     convert_to_docx(filename, output_str, 1)
#     print(f'Finished generating {filename}')


# def convert_to_docx(filename, data_str, pr_type):
    
#     # Load the JSON string into a Python dictionary
#     data = json.loads(data_str)
#     if pr_type == 0:
#         # Extract the 'press_release' content and replace escape sequences
#         press_release = data["press_release"].replace("\\n", "\n")
#     elif pr_type == 1:
#         press_release = data["consolidated_doc"].replace("\\n", "\n")
        

#     # Create a new Word document
#     doc = Document()

#     # Add the content to the document. Split by '\n' and add each line as a new paragraph
#     for line in press_release.split('\n'):
#         doc.add_paragraph(line)

#     # Save the document
#     title = filename + '.docx'
#     doc.save(title)
#     # doc.save(f'beep.docx')



# class PressReleaseGUI(QWidget):
#     def __init__(self):
#         super().__init__()

#         # Initialize UI elements
#         self.init_ui()

#     def init_ui(self):
#         # Create layout
#         self.layout = QVBoxLayout()

#         # ComboBox to select between Press Release and Media Advisory
#         self.selection_combo = QComboBox()
#         self.selection_combo.addItems(["Press Release", "Media Advisory"])
#         self.selection_combo.currentTextChanged.connect(self.update_ui)
#         self.layout.addWidget(self.selection_combo)

#         # Initialize common and specific UI elements for both options
#         self.init_press_release_ui()
#         self.init_media_advisory_ui()

#         # Update the UI to show the right elements based on current selection
#         self.update_ui(self.selection_combo.currentText())

#         # Set main layout
#         self.setLayout(self.layout)

#         # Set window title and size
#         self.setWindowTitle("PyQt5 Simple UI")
#         self.resize(300, 600)

#     def init_press_release_ui(self):
#         # Create label and text edit for Announcement
#         self.announcement_label = QLabel("Announcement")
#         self.announcement_input = QTextEdit()

#         # Create label, line edit, and combo box for Info
#         self.info_label = QLabel("Info")
#         self.info_input = QLineEdit()
#         self.info_combo = QComboBox()
#         self.add_info_button = QPushButton("Add")
#         self.add_info_button.clicked.connect(self.add_info)

#         # Create label and text edit for Boilerplate
#         self.boilerplate_label = QLabel("Boilerplate")
#         self.boilerplate_input = QTextEdit()

#         # Create label and line edit for File Name
#         self.filename_label = QLabel("File Name")
#         self.filename_input = QLineEdit()

#         # Button to process inputs
#         self.submit_button = QPushButton("Submit")
#         self.submit_button.clicked.connect(lambda: self.process_inputs(0))

#         # Add widgets to layout
#         self.layout.addWidget(self.announcement_label)
#         self.layout.addWidget(self.announcement_input)
#         self.layout.addWidget(self.info_label)
#         self.layout.addWidget(self.info_input)
#         self.layout.addWidget(self.add_info_button)
#         self.layout.addWidget(self.info_combo)
#         self.layout.addWidget(self.boilerplate_label)
#         self.layout.addWidget(self.boilerplate_input)
#         self.layout.addWidget(self.filename_label)
#         self.layout.addWidget(self.filename_input)
#         self.layout.addWidget(self.submit_button)

#         # Hide all these widgets initially
#         self.hide_press_release_ui()

#     def hide_press_release_ui(self):
#         # Code to hide all the press release specific widgets

#         self.announcement_label.hide()
#         self.announcement_input.hide()
#         self.info_label.hide()
#         self.info_input.hide()
#         self.add_info_button.hide()
#         self.info_combo.hide()
#         self.boilerplate_label.hide()
#         self.boilerplate_input.hide()
#         self.filename_label.hide()
#         self.filename_input.hide()
#         self.submit_button.hide()

#     def init_media_advisory_ui(self):
#         # Create UI elements for Media Advisory

#         self.ma_announcement_label = QLabel("Announcement")
#         self.ma_announcement_input = QTextEdit()

#         self.ma_what_label = QLabel("What")
#         self.ma_what_input = QLineEdit()

#         self.ma_where_label = QLabel("Where")
#         self.ma_where_input = QLineEdit()

#         self.ma_when_label = QLabel("When")
#         self.ma_when_input = QLineEdit()
#         self.ma_when_combo = QComboBox()
#         self.add_when_button = QPushButton("Add")
#         self.add_when_button.clicked.connect(self.add_when)

#         self.ma_event_overview_label = QLabel("Event Overview")
#         self.ma_event_overview_input = QTextEdit()

#         self.ma_boilerplate_label = QLabel("Boilerplate")
#         self.ma_boilerplate_input = QTextEdit()

#         # Create label and line edit for File Name
#         self.ma_filename_label = QLabel("File Name")
#         self.ma_filename_input = QLineEdit()

#         # Button to process inputs
#         self.ma_submit_button = QPushButton("Submit")
#         self.ma_submit_button.clicked.connect(lambda: self.process_inputs(1))

#         # Add these widgets to the main layout
#         self.layout.addWidget(self.ma_announcement_label)
#         self.layout.addWidget(self.ma_announcement_input)
#         self.layout.addWidget(self.ma_what_label)
#         self.layout.addWidget(self.ma_what_input)
#         self.layout.addWidget(self.ma_where_label)
#         self.layout.addWidget(self.ma_where_input)
#         self.layout.addWidget(self.ma_when_label)
#         self.layout.addWidget(self.ma_when_input)
#         self.layout.addWidget(self.add_when_button)
#         self.layout.addWidget(self.ma_when_combo)
#         self.layout.addWidget(self.ma_event_overview_label)
#         self.layout.addWidget(self.ma_event_overview_input)
#         self.layout.addWidget(self.ma_boilerplate_label)
#         self.layout.addWidget(self.ma_boilerplate_input)
#         self.layout.addWidget(self.ma_filename_label)
#         self.layout.addWidget(self.ma_filename_input)
#         self.layout.addWidget(self.ma_submit_button)


#         # Hide all these widgets initially
#         self.hide_media_advisory_ui()

#     def hide_media_advisory_ui(self):
#         # Code to hide all the media advisory specific widgets

#         self.ma_announcement_label.hide()
#         self.ma_announcement_input.hide()
#         self.ma_what_label.hide()
#         self.ma_what_input.hide()
#         self.ma_where_label.hide()
#         self.ma_where_input.hide()
#         self.ma_when_label.hide()
#         self.ma_when_input.hide()
#         self.add_when_button.hide()
#         self.ma_when_combo.hide()
#         self.ma_event_overview_label.hide()
#         self.ma_event_overview_input.hide()
#         self.ma_boilerplate_label.hide()
#         self.ma_boilerplate_input.hide()
#         self.ma_filename_label.hide()
#         self.ma_filename_input.hide()
#         self.ma_submit_button.hide()

#     def add_when(self):
#         when_text = self.ma_when_input.text()
#         if when_text:  # if the text is not empty
#             self.ma_when_combo.addItem(when_text)
#             self.ma_when_input.clear()

#     def update_ui(self, selection):
#         if selection == "Press Release":
#             self.hide_media_advisory_ui()
#             self.show_press_release_ui()
#         else:
#             self.hide_press_release_ui()
#             self.show_media_advisory_ui()

#     def show_press_release_ui(self):
#         # Code to show all the press release specific widgets (same as your previous widgets)

#         self.announcement_label.show()
#         self.announcement_input.show()
#         self.info_label.show()
#         self.info_input.show()
#         self.add_info_button.show()
#         self.info_combo.show()
#         self.boilerplate_label.show()
#         self.boilerplate_input.show()
#         self.filename_label.show()
#         self.filename_input.show()
#         self.submit_button.show()

#     def show_media_advisory_ui(self):
#         # Code to show all the media advisory specific widgets

#         self.ma_announcement_label.show()
#         self.ma_announcement_input.show()
#         self.ma_what_label.show()
#         self.ma_what_input.show()
#         self.ma_where_label.show()
#         self.ma_where_input.show()
#         self.ma_when_label.show()
#         self.ma_when_input.show()
#         self.add_when_button.show()
#         self.ma_when_combo.show()
#         self.ma_event_overview_label.show()
#         self.ma_event_overview_input.show()
#         self.ma_boilerplate_label.show()
#         self.ma_boilerplate_input.show()
#         self.ma_filename_label.show()
#         self.ma_filename_input.show()
#         self.ma_submit_button.show()
    
#     def add_info(self):
#             info_text = self.info_input.text()
#             if info_text:  # if the text is not empty
#                 self.info_combo.addItem(info_text)
#                 self.info_input.clear()

#     def process_inputs(self, pr_type):
#         if pr_type == 0:
#             announcement = self.announcement_input.toPlainText()
#             boilerplate = self.boilerplate_input.toPlainText()
#             filename = self.filename_input.text()
            
#             info_array = [self.info_combo.itemText(i) for i in range(self.info_combo.count())]

#             # Print or process the inputs
#             print('Running!')
#             # print(f"Announcement: {announcement}")
#             # print(f"Info Array: {info_array}")
#             # print(f"Boilerplate: {boilerplate}")
#             # print(f"File Name: {filename}")
#             gpt_press_release(filename, announcement, info_array, boilerplate)
#         elif pr_type == 1:
#             filename = self.ma_filename_input.text()
#             announcement = self.ma_announcement_input.toPlainText()
#             what = self.ma_what_input.text()
#             where = self.ma_where_input.text()
#             when = [self.ma_when_combo.itemText(i) for i in range(self.ma_when_combo.count())]
#             event_overview = self.ma_event_overview_input.toPlainText()
#             boilerplate = self.ma_boilerplate_input.toPlainText()

#             gpt_media_advisory(filename, announcement, what, where, when, event_overview, boilerplate)
#         else:
#             for _ in range(100):
#                 print("SOMETHING WENT WRONG")
#         # Clear all current widgets from layout
#         for i in reversed(range(self.layout.count())): 
#             widget = self.layout.itemAt(i).widget()
#             if widget is not None:
#                 widget.deleteLater()
        

#         # Update the window to say "Submitted"
#         submitted_label = QLabel("Submitted")
#         self.layout.addWidget(submitted_label)

#         # Optionally resize or update the window as needed
#         self.resize(300, 100)

#     # The rest of your functions (add_info, process_inputs) will remain the same. 
#     # But ensure you adjust them to process media advisory inputs when that option is selected.



# class SimpleUI(QWidget):
#     def __init__(self):
#         super().__init__()

#         # Initialize UI elements
#         self.init_ui()

#     def init_ui(self):
#         # Create layout
#         self.layout = QVBoxLayout()

#         # Create label and text edit for Announcement
#         self.announcement_label = QLabel("Announcement")
#         self.announcement_input = QTextEdit()

#         # Create label, line edit, and combo box for Info
#         self.info_label = QLabel("Info")
#         self.info_input = QLineEdit()
#         self.info_combo = QComboBox()
#         self.add_info_button = QPushButton("Add")
#         self.add_info_button.clicked.connect(self.add_info)

#         # Create label and text edit for Boilerplate
#         self.boilerplate_label = QLabel("Boilerplate")
#         self.boilerplate_input = QTextEdit()

#         # Create label and line edit for File Name
#         self.filename_label = QLabel("File Name")
#         self.filename_input = QLineEdit()

#         # Button to process inputs
#         self.submit_button = QPushButton("Submit")
#         self.submit_button.clicked.connect(self.process_inputs)

#         # Add widgets to layout
#         self.layout.addWidget(self.announcement_label)
#         self.layout.addWidget(self.announcement_input)
#         self.layout.addWidget(self.info_label)
#         self.layout.addWidget(self.info_input)
#         self.layout.addWidget(self.add_info_button)
#         self.layout.addWidget(self.info_combo)
#         self.layout.addWidget(self.boilerplate_label)
#         self.layout.addWidget(self.boilerplate_input)
#         self.layout.addWidget(self.filename_label)
#         self.layout.addWidget(self.filename_input)
#         self.layout.addWidget(self.submit_button)

#         # Set main layout
#         self.setLayout(self.layout)

#         # Set window title and size
#         self.setWindowTitle("PyQt5 Simple UI")
#         self.resize(300, 550)

#     def add_info(self):
#         info_text = self.info_input.text()
#         if info_text:  # if the text is not empty
#             self.info_combo.addItem(info_text)
#             self.info_input.clear()

#     def process_inputs(self, pr_type):
#         if pr_type == 0:
#             announcement = self.announcement_input.toPlainText()
#             boilerplate = self.boilerplate_input.toPlainText()
#             filename = self.filename_input.text()
            
#             info_array = [self.info_combo.itemText(i) for i in range(self.info_combo.count())]

#             # Print or process the inputs
#             print('Running!')
#             # print(f"Announcement: {announcement}")
#             # print(f"Info Array: {info_array}")
#             # print(f"Boilerplate: {boilerplate}")
#             # print(f"File Name: {filename}")
#             gpt_press_release(filename, announcement, info_array, boilerplate)
#         if pr_type == 1:
#             announcement = None
#             gpt_media_advisory(filename, announcement, info_array, 0)
#         else:
#             for _ in range(100):
#                 print("SOMETHING WENT WRONG")
#         # Clear all current widgets from layout
#         for i in reversed(range(self.layout.count())): 
#             widget = self.layout.itemAt(i).widget()
#             if widget is not None:
#                 widget.deleteLater()
        

#         # Update the window to say "Submitted"
#         submitted_label = QLabel("Submitted")
#         self.layout.addWidget(submitted_label)

#         # Optionally resize or update the window as needed
#         self.resize(300, 100)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PressReleaseGUI()
    window.show()
    sys.exit(app.exec_())
