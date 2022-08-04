
import sys
from datetime import datetime
# IMPORT QT CORE
from qt_core import *
from esxi_app.esxi_app import On_off
import json
# IMPORT MAIN WINDOW
from mainwindow import Ui_MainWindow
# MAIN WINDOW
from logger.logger import Logger


class CheckInputDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Проверка")  # check_dialog_window.window_title
        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.check_input)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QVBoxLayout()
        self.message = QLabel("введи 1122")  # check_dialog_window.message
        self.textbox = QLineEdit()
        self.layout.addWidget(self.message)
        self.layout.addWidget(self.textbox)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        # self.textbox.installEventFilter(self)

    # def eventFilter(self, obj, event):
    #     if event.type() == QEvent.KeyPress and obj is self.textbox:
    #         if event.key() == Qt.Key_Return and self.textbox.hasFocus():
    #             print('Enter pressed')
    #     return super().eventFilter(obj, event)

    def check_input(self):
        text = self.textbox.text()
        if text == "1122":
            return self.accept()

        else:
            # check_dialog_window.placeholder
            self.textbox.setPlaceholderText('введи "1122"')
            self.textbox.setPlainText("")
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setStandardButtons(QMessageBox.StandardButton.Yes)
            msg.setWindowTitle("Ошибка")  # check_dialog_window.message_title
            # check_dialog_window.message_text
            msg.setText("Неправильный ввод")
            ret = msg.exec()


class MainWindow(QMainWindow):
    # logsignal = Signal()
    def __init__(self):
        super().__init__()
        # self.translate = json.loads()
        # SETUP MAIN WINDOW

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.esxi = On_off()
        self.fill_in_combo_box()
        self.button_definition()
        self.setWindowTitle("Выключение ВМ")  # main_app.window_title
        self.esxi_defaults()
        Logger().write_log(f"Программа запущена")  # log.app_start
        # self.logsignal.connect(self.logger.write_log)
        
        # self.ui.textBrowser.verticalScrollBar().setValue(
        #     self.ui.textBrowser.verticalScrollBar().maximum())
        self.show()

    def esxi_defaults(self):
        self.esxi.power_off = True
        # self.ui.plainTextEdit

    def fill_in_combo_box(self):
        self.ui.comboBox.setPlaceholderText(
            "Выбрать тег")  # main_app.combo_box_placeholder
        for i in self.esxi.getonofftags:
            self.ui.comboBox.addItem(i['name'])
            pass

    def button_definition(self):
        self.ui.button_power_off.clicked.connect(self.buttonClick)
        self.ui.button_power_on.clicked.connect(self.buttonClick)

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()
        self.fire_up(btnName)

    def fire_up(self, btnName):
        if btnName == "button_power_off":
            self.esxi.power_on = False
            self.esxi.power_off = True
        if btnName == "button_power_on":
            self.esxi.power_off = False
            self.esxi.power_on = True
        combobox_selected = self.ui.comboBox.currentText()
        manual_enter = self.ui.lineEdit.text()
        if combobox_selected == '':
            vms = self.prepare_list_by_tag(self.esxi.default_tag)
        else:
            vms = self.prepare_list_by_tag(combobox_selected)
        # Проверить тег на существование
        for tag in self.esxi.get_all_tags:
            if manual_enter != '' and manual_enter in tag:
                vms = self.prepare_list_by_tag(tag)
        dlg = CheckInputDialog()
        returned_value = dlg.exec()
        # Logger().write_log(returned_value)
        if returned_value:
            self.esxi.power_state_vms(vms)
        else:
            # log.check_cancel
            Logger().write_log("Проверка отменена, Операция включения\\отключения отменена")

    def prepare_list_by_tag(self, selected_tag=None):
        for node in self.esxi.getonofftags:
            if selected_tag in node['name'] or selected_tag in node['id']:
                vms = [x.id for x in node['vms']]
                pass
        return vms

    # def write_log(self, text):
    #     current_text = self.ui.textBrowser.toPlainText()
    #     date_now = datetime.now().strftime("%d-%m-%Y")
    #     time_now = datetime.now().strftime("%H:%M:%S")
    #     # set new text
    #     self.ui.textBrowser.setText(
    #         f'{current_text}\n{date_now}\t{time_now}\t{text}')

    #     self.ui.textBrowser.append()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
