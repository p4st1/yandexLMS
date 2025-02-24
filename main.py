from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic, QtGui
from random import randint
import io
import sys


class circleWidget(QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        painter = QPainter(self)
        for i in range(randint(1, 50)):
            painter.setBrush(
            QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            )
            radius = randint(10, 200)
            painter.drawEllipse(
                randint(0, 600), randint(0, 600), radius, radius)

class UI_text():
    def __init__(self):
        self.ui = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="button">
    <property name="geometry">
     <rect>
      <x>354</x>
      <y>280</y>
      <width>93</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Нажмите</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>40</y>
      <width>91</width>
      <height>91</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>yellow.png</pixmap>
    </property>
    <property name="scaledContents">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QLabel" name="label_6">
    <property name="geometry">
     <rect>
      <x>620</x>
      <y>270</y>
      <width>111</width>
      <height>111</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>yellow.png</pixmap>
    </property>
    <property name="scaledContents">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QLabel" name="label_1">
    <property name="geometry">
     <rect>
      <x>-60</x>
      <y>370</y>
      <width>241</width>
      <height>241</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>yellow.png</pixmap>
    </property>
    <property name="scaledContents">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>320</x>
      <y>-80</y>
      <width>301</width>
      <height>301</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>yellow.png</pixmap>
    </property>
    <property name="scaledContents">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>420</x>
      <y>330</y>
      <width>51</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>yellow.png</pixmap>
    </property>
    <property name="scaledContents">
     <bool>true</bool>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>410</x>
      <y>360</y>
      <width>321</width>
      <height>331</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="pixmap">
     <pixmap>yellow.png</pixmap>
    </property>
    <property name="scaledContents">
     <bool>true</bool>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(UI_text().ui)
        uic.loadUi(f, self)

        self.button.clicked.connect(self.funcDrawCircles)

    def funcDrawCircles(self):
        self.circle = circleWidget()
        self.setCentralWidget(self.circle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainWindow()
    ex.show()
    sys.exit(app.exec())
