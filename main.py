import sys, os
from PyQt5.QtWidgets import QApplication
from pr_generator.press_release_gui import PressReleaseGUI
from dotenv import load_dotenv
import openai

# load_dotenv()
# openai.api_key=os.getenv("OPENAI_API_KEY")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PressReleaseGUI()
    window.show()
    sys.exit(app.exec_())
