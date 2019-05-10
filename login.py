from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

from PyQt5.uic import loadUi
import sys


class Login(QWidget):
	def __init__(self, parent=None):
		super(Login, self).__init__(parent)
		loadUi('loginwidget.ui',self)
		self.setWindowTitle("Login:")

		# Verify user button
		self.pushButton.clicked.connect(self.verify_user)

		# Cancel and close login form
		self.pushButton_2.clicked.connect(self.cancel_logging)
		self.show()

	# Verifies the username and password to log user in
	def verify_user(self):
		username = self.lineEdit.text()
		pwd = self.lineEdit_2.text()
		if username == "antonio" and pwd == "12345":
			self.open_window()
		else:
			print('Enter correct Username and Password')

	# Hides login form and show the mainwindow
	def open_window(self):
		self.hide()
		self.main = MainWindow()
		self.main.pushButton.clicked.connect(self.show_login)
		self.main.show()
	
	# Log out mainwindow and show login form
	def show_login(self):
		self.main.close()
		self.lineEdit_2.clear()
		self.show()
			
	# Cancel button, clears lineedit field and also closes the login form
	def cancel_logging(self):
		self.lineEdit.clear()
		self.lineEdit_2.clear()
		self.close()


# Mainwindow class after login is successful
class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		loadUi('main.ui',self)
		self.setWindowTitle("Mainwindow - User: antonio")


	# def log_out(self):
	# 	self.close()
	# 	log_show = Login(self)
	# 	log_show.show()

app = QApplication(sys.argv)
log = Login()
sys.exit(app.exec_())
