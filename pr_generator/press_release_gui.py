import sys, os
sys.path.append('../GPT_FineTuning')

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox, QHBoxLayout
from openai import OpenAI

# client = OpenAI()
import json
from docx import Document
print("SYS PATH", sys.path)

from pr_generator.helper_funcs import gpt_media_advisory, gpt_press_release
# from src.press_release_funcs import gpt_press_release, gpt_media_advisory

class PressReleaseGUI(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize UI elements
        self.init_ui()

    def init_ui(self):
        # Create layout
        self.layout = QVBoxLayout()

        # ComboBox to select between Press Release and Media Advisory
        self.selection_combo = QComboBox()
        self.selection_combo.addItems(["Press Release", "Media Advisory"])
        self.selection_combo.currentTextChanged.connect(self.update_ui)
        self.layout.addWidget(self.selection_combo)

        # Initialize common and specific UI elements for both options
        self.init_press_release_ui()
        self.init_media_advisory_ui()

        # Update the UI to show the right elements based on current selection
        self.update_ui(self.selection_combo.currentText())

        # Set main layout
        self.setLayout(self.layout)

        # Set window title and size
        # self.setWindowTitle("PyQt5 Simple UI")
        self.setWindowTitle("Press Release and Media Advisory Generator")
        # self.resize(800, 600)

    def init_press_release_ui(self):
        # Add headline and subheadline fields
        self.headline_label = QLabel('Headline')
        self.headline_input = QLineEdit()
        self.layout.addWidget(self.headline_label)
        self.layout.addWidget(self.headline_input)

        self.subheadline_label = QLabel('Subheadline')
        self.subheadline_input = QLineEdit()
        self.layout.addWidget(self.subheadline_label)
        self.layout.addWidget(self.subheadline_input)

        # Create label and text edit for Announcement
        self.announcement_label = QLabel("Announcement")
        self.announcement_input = QTextEdit()
        self.layout.addWidget(self.announcement_label)
        self.layout.addWidget(self.announcement_input)

        # Create label and text edit for quotes
        self.quote_label = QLabel("Quote")
        self.quote_input = QTextEdit()
        self.layout.addWidget(self.quote_label)
        self.layout.addWidget(self.quote_input)

        # Create label, line edit, and box for Info
        self.info_label = QLabel("Info")
        self.info_input = QTextEdit()
        # self.info_combo = QComboBox() # Comment out for testing side text box

        self.info_display = QTextEdit() # Attempt text box
        self.info_display.setReadOnly(True) # Make text box read only

        # Adjusting layout: Using QHBoxLayout to place info input and display side by side
        self.info_layout = QHBoxLayout()
        self.info_layout.addWidget(self.info_input)  # Existing QTextEdit for input
        self.info_layout.addWidget(self.info_display)  # New QTextEdit for displaying info

        # Add the horizontal layout to the main layout
        self.layout.addWidget(self.info_label)
        self.layout.addLayout(self.info_layout)

        # Add info button
        self.add_info_button = QPushButton("Add Info")
        self.add_info_button.clicked.connect(self.add_info)
        self.layout.addWidget(self.add_info_button)

        # Create label and text edit for Boilerplate
        self.boilerplate_label = QLabel("Boilerplate")
        self.boilerplate_input = QTextEdit()
        self.boilerplate_input.setMaximumHeight(50)
        self.layout.addWidget(self.boilerplate_label)
        self.layout.addWidget(self.boilerplate_input)

        # Create label and line edit for File Name
        self.filename_label = QLabel("File Name")
        self.filename_input = QLineEdit()
        self.layout.addWidget(self.filename_label)
        self.layout.addWidget(self.filename_input)

        # Button to process inputs
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(lambda: self.process_inputs(0))
        self.layout.addWidget(self.submit_button)
        # self.resize(800, 500)



        # Add widgets to layout
        
        # self.layout.addWidget(self.info_combo)
        
       

        # Hide all these widgets initially
        self.hide_press_release_ui()

    def hide_press_release_ui(self):
        # Code to hide all the press release specific widgets

        self.announcement_label.hide()
        self.announcement_input.hide()
        self.info_label.hide()
        self.info_input.hide()
        self.add_info_button.hide()
        self.info_display.hide()
        # self.info_combo.hide()
        self.boilerplate_label.hide()
        self.boilerplate_input.hide()
        self.filename_label.hide()
        self.filename_input.hide()
        self.submit_button.hide()
        self.headline_input.hide()
        self.headline_label.hide()
        self.subheadline_input.hide()
        self.subheadline_label.hide()
        self.quote_input.hide()
        self.quote_label.hide()

    def init_media_advisory_ui(self):
        # Create UI elements for Media Advisory

         # Add headline and subheadline fields
        self.ma_headline_label = QLabel('Headline')
        self.ma_headline_input = QLineEdit()
        self.layout.addWidget(self.ma_headline_label)
        self.layout.addWidget(self.ma_headline_input)

        self.ma_subheadline_label = QLabel('Subheadline')
        self.ma_subheadline_input = QLineEdit()
        self.layout.addWidget(self.ma_subheadline_label)
        self.layout.addWidget(self.ma_subheadline_input)

        self.ma_announcement_label = QLabel("Announcement")
        self.ma_announcement_input = QTextEdit()
        self.layout.addWidget(self.ma_announcement_label)
        self.layout.addWidget(self.ma_announcement_input)

        self.ma_what_label = QLabel("What")
        self.ma_what_input = QLineEdit()
        self.layout.addWidget(self.ma_what_label)
        self.layout.addWidget(self.ma_what_input)

        self.ma_where_label = QLabel("Where")
        self.ma_where_input = QLineEdit()
        self.layout.addWidget(self.ma_where_label)
        self.layout.addWidget(self.ma_where_input)

        # Create label, text edit, and box for when
        self.ma_when_label = QLabel("When")
        self.ma_when_input = QTextEdit()
        self.layout.addWidget(self.ma_when_label)
        # self.layout.addWidget(self.ma_when_input)

        self.ma_when_display = QTextEdit()
        self.ma_when_display.setReadOnly(True)

         # Add QHbox to place text side by side
        self.ma_when_layout = QHBoxLayout()
        self.ma_when_layout.addWidget(self.ma_when_input)
        self.ma_when_layout.addWidget(self.ma_when_display)
        
        self.layout.addLayout(self.ma_when_layout)

        # self.ma_when_combo = QComboBox()
        self.add_when_button = QPushButton("Add")
        self.add_when_button.clicked.connect(self.add_when)
        self.layout.addWidget(self.add_when_button)
        # self.layout.addWidget(self.ma_when_combo)

        self.ma_event_overview_label = QLabel("Event Overview")
        self.ma_event_overview_input = QTextEdit()
        self.layout.addWidget(self.ma_event_overview_label)
        self.layout.addWidget(self.ma_event_overview_input)

        self.ma_boilerplate_label = QLabel("Boilerplate")
        self.ma_boilerplate_input = QTextEdit()
        self.ma_boilerplate_input.setMaximumHeight(50)
        self.layout.addWidget(self.ma_boilerplate_label)
        self.layout.addWidget(self.ma_boilerplate_input)

        # Create label and line edit for File Name
        self.ma_filename_label = QLabel("File Name")
        self.ma_filename_input = QLineEdit()
        self.layout.addWidget(self.ma_filename_label)
        self.layout.addWidget(self.ma_filename_input)

        # Button to process inputs
        self.ma_submit_button = QPushButton("Submit")
        self.ma_submit_button.clicked.connect(lambda: self.process_inputs(1))
        self.layout.addWidget(self.ma_submit_button)        

        # Hide all these widgets initially
        self.hide_media_advisory_ui()

    def hide_media_advisory_ui(self):
        # Code to hide all the media advisory specific widgets

        self.ma_announcement_label.hide()
        self.ma_announcement_input.hide()
        self.ma_what_label.hide()
        self.ma_what_input.hide()
        self.ma_where_label.hide()
        self.ma_where_input.hide()
        self.ma_when_label.hide()
        self.ma_when_input.hide()
        self.add_when_button.hide()
        self.ma_when_display.hide()
        # self.ma_when_combo.hide()
        self.ma_event_overview_label.hide()
        self.ma_event_overview_input.hide()
        self.ma_boilerplate_label.hide()
        self.ma_boilerplate_input.hide()
        self.ma_filename_label.hide()
        self.ma_filename_input.hide()
        self.ma_submit_button.hide()
        self.ma_headline_input.hide()
        self.ma_headline_label.hide()
        self.ma_subheadline_input.hide()
        self.ma_subheadline_label.hide()
# 
        # self.resize(800, 500)


    def add_when(self):
        when_text = self.ma_when_input.toPlainText()
        if when_text:  # if the text is not empty
            self.ma_when_display.append(when_text)
            # self.ma_when_combo.addItem(when_text)
            self.ma_when_input.clear()

    def update_ui(self, selection):
        if selection == "Press Release":
            self.hide_media_advisory_ui()
            self.show_press_release_ui()
        else:
            self.hide_press_release_ui()
            self.show_media_advisory_ui()

    def show_press_release_ui(self):
        # Code to show all the press release specific widgets (same as your previous widgets)

        self.announcement_label.show()
        self.announcement_input.show()
        self.info_label.show()
        self.info_input.show()
        self.add_info_button.show()
        self.info_display.show()
        # self.info_combo.show()
        self.boilerplate_label.show()
        self.boilerplate_input.show()
        self.filename_label.show()
        self.filename_input.show()
        self.submit_button.show()
        self.headline_input.show()
        self.headline_label.show()
        self.subheadline_input.show()
        self.subheadline_label.show()
        self.quote_input.show()
        self.quote_label.show()

    def show_media_advisory_ui(self):
        # Code to show all the media advisory specific widgets

        self.ma_announcement_label.show()
        self.ma_announcement_input.show()
        self.ma_what_label.show()
        self.ma_what_input.show()
        self.ma_where_label.show()
        self.ma_where_input.show()
        self.ma_when_label.show()
        self.ma_when_input.show()
        self.add_when_button.show()
        self.ma_when_display.show()
        # self.ma_when_combo.show()
        self.ma_event_overview_label.show()
        self.ma_event_overview_input.show()
        self.ma_boilerplate_label.show()
        self.ma_boilerplate_input.show()
        self.ma_filename_label.show()
        self.ma_filename_input.show()
        self.ma_submit_button.show()
        self.ma_headline_input.show()
        self.ma_headline_label.show()
        self.ma_subheadline_input.show()
        self.ma_subheadline_label.show()
    
    def add_info(self):
         # Method to handle adding info to the display text box
        info_text = self.info_input.toPlainText()
        self.info_display.append(info_text)  # Add the text to the QTextEdit
        self.info_input.clear()  # Clear the input field

        # info_text = self.info_input.text()
        # if info_text:  # if the text is not empty
        #     self.info_combo.addItem(info_text)
        #     self.info_input.clear()

    def process_inputs(self, pr_type):
        if pr_type == 0:
            announcement = self.announcement_input.toPlainText()
            quotes = self.quote_input.toPlainText()
            boilerplate = self.boilerplate_input.toPlainText()
            filename = self.filename_input.text()
            headline = self.headline_input.text()
            subheadline = self.subheadline_input.text()
            info_text = self.info_display.toPlainText()
            print(f"INFO_TEXT\n{info_text}")
            

            # Print or process the inputs
            print('Running!')
            # print(f"Announcement: {announcement}")
            # print(f"Info Array: {info_array}")
            # print(f"Boilerplate: {boilerplate}")
            # print(f"File Name: {filename}")
            gpt_press_release(filename, headline, subheadline, announcement, quotes, info_text, boilerplate)
        elif pr_type == 1:
            filename = self.ma_filename_input.text()
            announcement = self.ma_announcement_input.toPlainText()
            what = self.ma_what_input.text()
            where = self.ma_where_input.text()
            #TODO FIX THIS
            # when = [self.ma_when_combo.itemText(i) for i in range(self.ma_when_combo.count())]
            when = self.ma_when_display.toPlainText()
            print(f"WHEN TEXT\n{when}")
            event_overview = self.ma_event_overview_input.toPlainText()
            boilerplate = self.ma_boilerplate_input.toPlainText()

            gpt_media_advisory(filename, announcement, what, where, when, event_overview, boilerplate)
        else:
            for _ in range(100):
                print("SOMETHING WENT WRONG")
        # Clear all current widgets from layout
        for i in reversed(range(self.layout.count())): 
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        

        # Update the window to say "Submitted"
        submitted_label = QLabel("Done!")
        self.layout.addWidget(submitted_label)

        # Optionally resize or update the window as needed
        # self.resize(300, 100)

    # The rest of your functions (add_info, process_inputs) will remain the same. 
    # But ensure you adjust them to process media advisory inputs when that option is selected.



