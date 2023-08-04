from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

Form, Window = uic.loadUiType("untitled.ui")

app = QApplication([])
window = Window()
window.setObjectName("MainWindow")
window.setStyleSheet("#MainWindow{border-image:url(jpg1.jpg)}")
form = Form()
form.setupUi(window)
window.showFullScreen()


def clicked_button():
    text_need1 = form.lineEdit.text()
    text_need2 = form.lineEdit_2.text()
    text_need1 = list(text_need1)
    text_need2 = list(text_need2)
    print(text_need1, text_need2)
    n1 = len(text_need1)
    n2 = len(text_need2)
    c = 0
    if n2 == 0 and n1 == 0:
        return 0
    elif n2 != n1:
        form.label_4.setText('Недостаточно или слишком много символов')
        form.lineEdit_2.setStyleSheet("background-color: rgb(204, 0, 51);")
    else:
        form.lineEdit_2.setStyleSheet("background-color: rgb(51, 255, 102);")
        form.label_4.setText('')
        for i in range(n1):
            if text_need1[i] == text_need2[i]:
                c += 1
        form.progressBar.setProperty("value", c / n1 * 100)
        if form.progressBar.value() < 50:
            form.progressBar.setStyleSheet("QProgressBar::chunk "
                                           "{"
                                           "background-color: red;"
                                           "}")
        elif form.progressBar.value() >= 50 and form.progressBar.value() < 67:
            form.progressBar.setStyleSheet("QProgressBar::chunk "
                                           "{"
                                           "background-color: orange;"
                                           "}")
        elif form.progressBar.value() >= 67 and form.progressBar.value() < 90:
            form.progressBar.setStyleSheet("QProgressBar::chunk "
                                           "{"
                                           "background-color: yellow;"
                                           "}")
        else:
            form.progressBar.setStyleSheet("QProgressBar::chunk "
                                           "{"
                                           "background-color: green;"
                                           "}")


def changeTitle(state):
    if state == Qt.Checked:
        form.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
    else:
        form.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)


form.lineEdit.setStyleSheet("background-color: rgb(51, 255, 102);")
form.lineEdit_2.setStyleSheet("background-color: rgb(51, 255, 102);")
form.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
form.pushButton.clicked.connect(clicked_button)
form.checkBox.toggle()
form.checkBox.stateChanged.connect(changeTitle)
form.pushButton.setAutoDefault(True)
form.lineEdit_2.returnPressed.connect(form.pushButton.click)

app.exec()
