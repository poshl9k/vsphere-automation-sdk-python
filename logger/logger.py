
from qt_core import *
from datetime import datetime

import typing
class Logger(object):
    def __init__(self):
        super().__init__()
        self.main_ui = self.findMainWindow()
        pass

    def findMainWindow(self) -> typing.Union[QMainWindow, None]:
        # Global function to find the (open) QMainWindow in application
        app = QApplication.instance()
        for widget in app.topLevelWidgets():
            if isinstance(widget, QMainWindow):
                return widget
        return None
    def write_log(self, text):
        # current_text = self.main_ui.ui.textBrowser.toPlainText()
        date_now = datetime.now().strftime("%d-%m-%Y")
        time_now = datetime.now().strftime("%H:%M:%S")
        # set new text
        print(text)
        self.main_ui.ui.textBrowser.append(
            f'{date_now}\t{time_now}\t{text}')
        self.main_ui.ui.textBrowser.ensureCursorVisible()
        self.main_ui.ui.textBrowser.update()