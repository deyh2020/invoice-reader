# Attempts to import all required modules
try:
  import sys, os, xlsxwriter

  import tkinter as tk
  from tkinter import filedialog

  from PyQt5.QtWidgets import *
  from PyQt5 import QtCore, QtGui

  from readPDF import Read


# Raises exception if modules cannot be imported
except:
  raise Exception ("Cannot Import Required Modules.")
  exit()



class Window(QMainWindow):

  def __init__(self, parent=None):
    super().__init__(parent)

    # Set title of window
    self.setWindowTitle("  Invoice To Spreadsheet 1.0")

    # Set size of window
    self.resize(1280, 720)

    # Set window icon
    self.setWindowIcon(QtGui.QIcon(''))

    #self.fileSelectButton.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    # Creates UI components
    self.createUIComponents()

    # Creates UI layout
    self.initUI()


  def createUIComponents(self):

    buttonWidth = 150
    buttonHeight = 50

    #self.temp = QPushButton('test', self)
    #self.temp.resize(200, 100)


    # Create Tabs
    self.displayFilesTab = self.showActiveFiles()


    # Create buttons
    self.fileSelectButton = QPushButton('File Select', self)
    self.folderSelectButton = QPushButton('Folder Select', self)
    self.startButton = QPushButton('Start', self)
    self.settingsButton = QPushButton('Settings', self)
    self.openCMDButton = QPushButton('Open CMD', self)

    # Resizes buttons
    self.fileSelectButton.resize(buttonWidth, buttonHeight)
    self.folderSelectButton.resize(buttonWidth, buttonHeight)
    self.startButton.resize(buttonWidth, buttonHeight)
    self.settingsButton.resize(buttonWidth, buttonHeight)
    self.openCMDButton.resize(buttonWidth, buttonHeight)

    # Calls functions when buttons are clicked
    self.fileSelectButton.clicked.connect(self.selectFile)
    self.folderSelectButton.clicked.connect(self.selectFolder)
    self.startButton.clicked.connect(self.button3Action)
    self.settingsButton.clicked.connect(self.openSettings)
    self.openCMDButton.clicked.connect(self.openCMD)





  def initUI(self):

    buttonLayout = QVBoxLayout()
    buttonLayout.addWidget(self.fileSelectButton, alignment=QtCore.Qt.AlignRight)
    buttonLayout.addWidget(self.folderSelectButton, alignment=QtCore.Qt.AlignRight)
    buttonLayout.addWidget(self.startButton, alignment=QtCore.Qt.AlignRight)
    buttonLayout.addWidget(self.settingsButton, alignment=QtCore.Qt.AlignRight)
    buttonLayout.addWidget(self.openCMDButton, alignment=QtCore.Qt.AlignRight)

    buttonLayout.addStretch(100)
    buttonLayout.setSpacing(20)


    right_widget = QWidget()
    right_widget.resize(200, 200)
    right_widget.setLayout(buttonLayout)


    self.left_widget = QTabWidget()
    self.left_widget.tabBar().setObjectName("mainTab")

    self.left_widget.addTab(self.displayFilesTab, '')
    #self.left_widget.addTab(self.tab2, '')

    self.left_widget.setCurrentIndex(0)
    self.left_widget.setStyleSheet('''QTabBar::tab{width: 0; \ height: 0; margin: 0; padding: 0; border: none;}''')

    main_layout = QHBoxLayout()
    main_layout.addWidget(right_widget)
    main_layout.addWidget(self.left_widget)
    #main_layout.setStretch(0, 20)
    #main_layout.setStretch(1, 100)
    #main_layout.setStretch()
    main_widget = QWidget()
    main_widget.setLayout(main_layout)
    self.setCentralWidget(main_widget)
    #pass

  # ---- Button Actions ----

  # Open file manager and select either image or pdf file
  def selectFile(self):

    print("Button 1 pressed")
    #self.right_widget.setCurrentIndex(0)

  # Open file manager and select file, should then validate that folder only contains image of pdf files
  def selectFolder(self):

    print("Button 2 pressed")
    #self.right_widget.setCurrentIndex(1)

    # Hides tkinter root window while file manager is open
    root = tk.Tk()
    root.withdraw()
    
    # Opens file manager
    files = filedialog.askopenfilenames()

  # User selects preset and then data gets translated to spreadsheet
  def button3Action(self):

    # Open preset selection menu
    # Either create new preset and enter 'teaching' mode
    # Use existing preset to begin translating data to spreadsheet



    print("Button 3 pressed")
    #self.right_widget.setCurrentIndex(2)
    self.workbook = xlsxwriter.Workbook('test.xlsx')
    self.worksheet = self.workbook.add_worksheet()

    #Read("invoice1.png")
    #worksheet.set_column(1, 3, 25)

    topics = ["Date", "Name", "Invoice", "Price"]
    
    positionX = 'A'
    content = ""
    col = [5, 25, 15, 10]

    for i in range(len(topics)):

      self.worksheet.set_column(i, i, col[i])

      for j in range(1,10):

        positionY = str(j+1)

        if j == 1:

          content = topics[i]
          positionY = str(1)

        else:

          content = "content"

          
        

        position = positionX + positionY

        self.worksheet.write(position, content)

      # Increments character
      char = ord(positionX)
      char += 1
      positionX = chr(char)


    self.workbook.close()
    
    # Opens spreadsheet
    #os.startfile("test.xlsx")

  # Opens settings menu
  def openSettings(self):

    print("Opened settings menu")

  # Opens command prompt at current location
  def openCMD(self):

    print("Opened command prompt")
    os.system("start cmd")



  def showActiveFiles(self):

    layout = QVBoxLayout()
    layout.addWidget(QLabel(''))
    layout.addStretch()
    
    main = QWidget()
    main.setLayout(layout)
    return main

    

if __name__ == "__main__":

  app = QApplication(sys.argv)
  win = Window()
  win.show()
  sys.exit(app.exec_())
