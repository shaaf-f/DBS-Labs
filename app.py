import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6 import uic
from datetime import date

DBSSub = ['ERD','SQL','OLAP', 'Data Mining']
OOPSub = ['C++','Java']
AISub = ['Machine Learning','Robotics','Computer Vision']

class UI(QtWidgets.QMainWindow):
    def __init__(self):
    # Call the inherited classes __init__ method
        super(UI, self).__init__()
        # Load the .ui file
        uic.loadUi('Lab_01_sf08405.ui', self)
        # Show the GUI
        category = self.categories.currentText()
        self.AuthorNames.setReadOnly(True)
        self.categories.activated.connect(self.checkCategory) 
        self.AddAuthor.clicked.connect(self.AuthorsAdd)
        self.OkayButton.clicked.connect(self.Verification)
        self.show()
        # Event handling
    # def updateIssuedFields(self):
    #     if
    def AuthorsAdd(self):
        name = self.AuthorNameEdit.text() 
        self.AuthorNames.append(name)
    def checkCategory(self):
        category = self.categories.currentText()
        print(category)
        if category == 'Database Systems':
            self.subcategories.clear()
            self.subcategories.addItems(DBSSub)
        elif category == 'OOP':
            self.subcategories.clear()
            self.subcategories.addItems(OOPSub)
        elif category == 'Artificial Intelligence':
            self.subcategories.clear()
            self.subcategories.addItems(AISub)
    def Verification(self):
        ISBNlen = len(self.ISBNLine.text())
        message = 'No set msg'
        if ISBNlen > 12 or self.validDate():
            message = "The length of ISBN is greater than 12 or Purchased On Date is greater than today"
        msg_box = QMessageBox()
        msg_box.setText(message)
        msg_box.setWindowTitle('ERROR!')
        msg_box.exec()
    def button_clicked(self):
        self.label.setText('Welcome to QT Designer')
    def validDate(self):
        purchaseDate = self.purchaseDateEdit.date()
        todayDate = date.today()
        return (purchaseDate.year() < todayDate.year or
            (purchaseDate.year() == todayDate.year and
             (purchaseDate.month() < todayDate.month or
              (purchaseDate.month() == todayDate.month and
               purchaseDate.day() < todayDate.day))))
# Create an instance of QtWidgets . QApplication
app = QtWidgets.QApplication(sys.argv)
window = UI() # Create an instance of our class
app.exec() # Start the application