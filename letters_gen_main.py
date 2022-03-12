import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog
from PyQt5.QtWidgets import QLabel, QErrorMessage, QHBoxLayout, QInputDialog, QFileDialog
from PyQt5.QtGui import QPixmap
from letters_gen_ui import Ui_MainWindow
from main import do_things
import shutil
import os.path


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
        fname = QFileDialog.getOpenFileName(ex, 'Open file', '/home', filter='Word files (.docx)')
        self.lineEdit_getTemplate.setText(fname[0])
        self.template = self.lineEdit_getTemplate.text()

    def open_data(self):
        fname = QFileDialog.getOpenFileName(ex, 'Open file', '/home')
        self.lineEdit_getData.setText(fname[0])
        self.data_file = self.lineEdit_getData.text()

    def open_dir(self):
        dir_name = QFileDialog.getExistingDirectory(ex, 'Choose folder', '/home')
        self.lineEdit_chooseDir.setText(dir_name)
        self.letters_dir = self.lineEdit_chooseDir.text()

    def run(self):
        if self.template and self.data_file and self.letters_dir:
            do_things(self.template, self.data_file, self.letters_dir)


app = QApplication(sys.argv)
ex = MainWidget()
ex.show()
sys.exit(app.exec_())
