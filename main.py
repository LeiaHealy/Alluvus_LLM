import sys
from PyQt5.QtWidgets import QApplication
from pr_generator.press_release_gui import PressReleaseGUI
from pr_generator.helper_funcs import gpt_press_release


if __name__ == '__main__':
    sys.path.append('/Users/erika/Documents/Alluvus/GPT_FineTuning')

    app = QApplication(sys.argv)
    window = PressReleaseGUI()
    window.show()
    sys.exit(app.exec_())

#     announcement = 'Jackie Wills is becoming head of the ExxonMobil branch of La Plata, MD'
#     headline = 'Jackie Wills is becoming head of the ExxonMobil branch of La Plata, MD'
#     subheadline = 'This is the subheadline'

#     info = """He has much experience working at other industries of the same type (elaborate on them, fluff it out)
# Come up with something that someone would say if they were Jackie Wills and add a quote of Jackie Wills saying that
# He has been in the business for over 20 years now"""

#     quotes = """Squidward Tentacles congratulated Jackie Wills' promotion.
#                 Mario discussed his Tenure at the ExxonMobil branch while working under Wills"""

#     boilerplate = 'The Wills Group is made up of the Wills family and located in La Plata, MD'

#     filename = 'single_space'

    # gpt_press_release(filename, headline, subheadline, announcement, quotes, info, boilerplate)
