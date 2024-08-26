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
        self.checkCategory()
        self.AuthorNames.setReadOnly(True)
        self.issuedEdit.setEnabled(False)
        self.IssueDate.setEnabled(False)
        self.categories.activated.connect(self.checkCategory) 
        self.issuedCheck.stateChanged.connect(self.updateIssuedFields)
        self.AddAuthor.clicked.connect(self.AuthorsAdd)
        self.OkayButton.clicked.connect(self.Verification)
        self.CloseButton.clicked.connect(self.close)
        self.show()
        # Event handling
    def updateIssuedFields(self):
        if self.issuedCheck.isChecked():
            self.issuedEdit.setEnabled(True)
            self.IssueDate.setEnabled(True)
        else:
            self.issuedEdit.setEnabled(False)
            self.IssueDate.setEnabled(False)
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
        if ISBNlen > 12 or self.validDate(self.purchaseDateEdit.date()):
            message = "The length of ISBN is greater than 12 or Purchased On Date is greater than today"
        elif (self.issuedCheck.isChecked()) and ((self.issuedEdit.text() == '') or (self.validIssueDate(self.IssueDate.date(), self.purchaseDateEdit.date()))):
            message = "Issued to is empty or Issue Date is not between Purchased On and Today's date."
        elif self.AuthorNameEdit.text() != '' and self.Jbutton.isChecked():
            message = "Book of Journal Type should have no authors."
        elif (self.TBbutton.isChecked() or self.RBbutton.isChecked()) and self.AuthorNameEdit.text() == '':
            message = "Reference books or text book should have at least one author."
        else:
            message = "Book added successfully!"
        msg_box = QMessageBox()
        msg_box.setText(message)
        msg_box.setWindowTitle('Message Box')
        msg_box.exec()
    def button_clicked(self):
        self.label.setText('Welcome to QT Designer')
    def validIssueDate(self, toCheck,purchaseDate):
        todayDate = date.today()
        yearValid = purchaseDate.year() < toCheck.year() < todayDate.year
        sameAsPurchaseYear = toCheck.year() == purchaseDate.year()
        sameAsTodayYear = toCheck.year() == todayDate.year 
        monthValid = yearValid or (sameAsPurchaseYear and toCheck.month() > purchaseDate.month()) or (sameAsTodayYear and toCheck.month() < todayDate.month)
        sameAsPurchaseMonth = sameAsPurchaseYear and toCheck.month() == purchaseDate.month()
        sameAsTodayMonth = sameAsTodayYear and toCheck.month() < todayDate.month
        dateValid = monthValid or (sameAsPurchaseMonth and toCheck.day() > purchaseDate.day()) or (sameAsTodayMonth and toCheck.day() < todayDate.day)
        return not dateValid
    def validDate(self,toCheck):
        todayDate = date.today()
        yearValid = toCheck.year() < todayDate.year
        yearSame = toCheck.year() == todayDate.year
        monthValid = yearValid or (yearSame and toCheck.month() < todayDate.month) 
        monthSame = toCheck.month() == todayDate.month
        dateValid = monthValid or (yearSame and monthSame and toCheck.day() < todayDate.day)
        return not dateValid
# Create an instance of QtWidgets . QApplication
app = QtWidgets.QApplication(sys.argv)
window = UI() # Create an instance of our class
app.exec() # Start the application