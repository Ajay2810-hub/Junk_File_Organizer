import shutil
import os
import sys
from PyQt5 import QtWidgets, QtGui, QtCore

#Creating Application
app=QtWidgets.QApplication(sys.argv)

#Creating Window
win=QtWidgets.QWidget()
win.setWindowTitle("Junk File Organizer")
win.setGeometry(400,130,500,500)
p=win.palette()
p.setColor(win.backgroundRole(),QtCore.Qt.black)
win.setPalette(p)

#Heading Label
head=QtWidgets.QLabel(win)
head.setText("Junk File Organizer")
head.move(0,0)
head.setFixedWidth(500)
head.setAlignment(QtCore.Qt.AlignCenter)
head.setFont(QtGui.QFont("Arial",20))
head.setStyleSheet("background-color : orange; color : #fff; font-weight : bold;")

#Path Entry Label
path_=QtWidgets.QLabel(win)
path_.setText("Folder Path")
path_.move(45,140)
path_.setFont(QtGui.QFont("Arial",20))
path_.setStyleSheet("color : orange;")

#Path Entry Widget
ent=QtWidgets.QLineEdit(win)
ent.move(200,140)
ent.setFixedWidth(250)
ent.setFont(QtGui.QFont("Arial",20))
ent.setStyleSheet("background-color : #000; color : orange; border : 1px solid orange;")

#Function For calling The Organizing Function
def fun():
    fun1()

#Button Binded to Organizing Function
btn=QtWidgets.QPushButton(win)
btn.setText("Organize")
btn.setStyleSheet("background-color : #000; color : orange; border : 1px solid orange;")
btn.move(120,280)
btn.setFont(QtGui.QFont("Arial",20))
btn.setFixedWidth(300)
btn.setFixedHeight(50)
btn.clicked.connect(fun)

#Organizing Function
def fun1():

    #Folders and File Extensions
    Folders={
        "Shell":['.sh'],
        "Executable":['.exe'],
        "Html":['.html','.htm','.html5','.xhtml'],
        "Java":['.js','.java'],
        "Images":['.jpeg','.jpg','.tiff','.gif','.bmp','.png','.bpg','.svg','.heif','.psd'],
        "Videos":['.avi','.flv','.wmv','.mov','.mp4','.webm','.vob','.mng','.qt','.mpg','.mpeg','.3gp'],
        "Audios":['.aac','.aa','.dvf','.m4a','.m4p','.m4b','.mp3','.msv','.ogg','.oga','.raw','.vox','.wav','.wma'],
        "PDFs":['.pdf'],
        "Documents":['.oxps','.epub','.pages','.csv','.docx','.doc','.fdf','.ods','.odt','.pwi','.xsn','.xps','.dotx','.docm','.dox','.rvg','.rtf','.rtfd','.wpd','.xls','.xlsx','.ppt','.pptx'],
        "Archives":['.a','.ar','.cpio','.iso','.tar','.gz','.rz','.7z','.dmg','.rar','.xar','.zip'],
        "Text":['.txt','.in','out'],
        "Python":['.py'],
        "XML":['.xml'],
        #"Desktop ShortCuts":['.lnk'],
        "Database":['.db','.db-journal']
        }
    a=ent.text()
    if not a :
       QtWidgets.QMessageBox.warning(win,"Junk File Organizer","Please Enter The Directory Path!",QtWidgets.QMessageBox.Ok)
    else:
       if os.path.exists(a):
           try:
              for i in os.listdir(a):
                  for k in Folders:
                      for l in Folders[k]:
                          if str(i).endswith(l):
                             try:
                               if k[-1]=='s':
                                  os.mkdir(f'{a}\{k}')
                                  shutil.move(f'{a}\{i}',f'{a}\{k}')
                               else:
                                  os.mkdir(f'{a}\{k} Files')
                                  shutil.move(f'{a}\{i}',f'{a}\{k} Files')
                             except FileExistsError:
                               if k[-1]=='s':
                                  shutil.move(f'{a}\{i}',f'{a}\{k}')
                               else:
                                  shutil.move(f'{a}\{i}',f'{a}\{k} Files')
              QtWidgets.QMessageBox.warning(win,"Junk File Organizer","Folder Has Been Organized",QtWidgets.QMessageBox.Ok)
           except:
               QtWidgets.QMessageBox.warning(win,"Junk File Organizer","Path You Entered, Is not a Directory!",QtWidgets.QMessageBox.Ok)
       else:
          QtWidgets.QMessageBox.warning(win,"Junk File Organizer","Path You Entered, Doesn't Exists!",QtWidgets.QMessageBox.Ok)

#Used For Displaying The Window
win.show()
sys.exit(app.exec_())
