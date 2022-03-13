import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from letters_gen_ui import Ui_MainWindow
from pathlib import Path
from main import do_things

HOME = str(Path.home())


class MainWidget(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_run.clicked.connect(self.run)
        self.pushButton_getTemplate.clicked.connect(self.open_template)
        self.pushButton_getData.clicked.connect(self.open_data)
        self.pushButton_chooseDir.clicked.connect(self.open_dir)

        self.lineEdit_getTemplate.setReadOnly(True)
        self.lineEdit_getData.setReadOnly(True)
        self.lineEdit_chooseDir.setReadOnly(True)

        self.template = ''
        self.data_file = ''
        self.letters_dir = ''

    def open_template(self):
        fname = QFileDialog.getOpenFileName(ex, 'Open template file', HOME, filter='Word files (*.docx)')
        self.lineEdit_getTemplate.setText(fname[0])
        self.template = self.lineEdit_getTemplate.text()

    def open_data(self):
        fname = QFileDialog.getOpenFileName(ex, 'Open data file', HOME, filter='Excel files (*.xlsx)')
        self.lineEdit_getData.setText(fname[0])
        self.data_file = self.lineEdit_getData.text()

    def open_dir(self):
        dir_name = QFileDialog.getExistingDirectory(ex, 'Choose folder', HOME)
        self.lineEdit_chooseDir.setText(dir_name)
        self.letters_dir = self.lineEdit_chooseDir.text()

    def run(self):
        self.progressBar.setMinimum(0)
        self.progressBar.setValue(0)
        if self.template and self.data_file and self.letters_dir:
            try:
                for step in do_things(self.template, self.data_file, self.letters_dir):
                    self.progressBar.setMaximum(step[1])
                    self.progressBar.setValue(step[0])
            except Exception as e:
                self.message('error', str(e))
            else:
                self.message('info', 'Письма сгенерированы успешно!')
        else:
            self.message('warning', 'Вы заполнили не все поля. \nТак, быстро кабанчиком метнулся и заполнил!!!')

    @staticmethod
    def message(status, text):
        msg = QMessageBox()
        msg.setWindowTitle(status)
        msg.setText(text)
        if status == 'warning':
            msg.setIcon(QMessageBox.Warning)
        elif status == 'info':
            msg.setIcon(QMessageBox.Information)
        elif status == 'error':
            msg.setIcon(QMessageBox.Critical)

        msg.exec_()


app = QApplication(sys.argv)
ex = MainWidget()
ex.show()
sys.exit(app.exec_())
