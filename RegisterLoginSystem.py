import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
)
from PyQt5.QtCore import Qt

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Page")
        self.setGeometry(600, 300, 300, 150)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.label_username = QLabel("Username:")
        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText("Enter your username")

        self.label_password = QLabel("Password:")
        self.input_password = QLineEdit()
        self.input_password.setPlaceholderText("Enter your password")
        self.input_password.setEchoMode(QLineEdit.Password)

        self.btn_login = QPushButton("Login")
        self.btn_login.clicked.connect(self.check_login)

        self.message_label = QLabel("")
        self.message_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label_username)
        layout.addWidget(self.input_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(self.btn_login)
        layout.addWidget(self.message_label)

        self.setLayout(layout)

    def check_login(self):
        username = self.input_username.text()
        password = self.input_password.text()

        # Simple hardcoded check for demo
        if username == "admin" and password == "password123":
            self.message_label.setText("Login successful!")
            self.message_label.setStyleSheet("color: green;")
            QMessageBox.information(self, "Success", "You have logged in successfully.")
        else:
            self.message_label.setText("Invalid username or password.")
            self.message_label.setStyleSheet("color: red;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
