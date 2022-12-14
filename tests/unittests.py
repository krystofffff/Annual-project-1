import sys
import unittest

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget, QLabel, QVBoxLayout, QPushButton, QWidget, QWidgetItem, QFrame
from PyQt5.QtCore import *

import main
from dropController import DropUi
from labelClass import Label
from mainController import MainUi
from editController import EditUi
import dataManager as dm
import graphicOperations
import pytestqt


class MyTestCase(unittest.TestCase):
    app = QtWidgets.QApplication(sys.argv)
    sw = QWidget()
    sw.setWindowTitle("PicScan beta")
    main = MainUi(sw)
    drop = DropUi(sw, main)

    def test_labelDropUi(self):
        labelDragDrop = self.drop.label.text()
        labelTwo = self.drop.label2.text()
        self.assertEqual(labelDragDrop, "Drag & Drop")
        self.assertEqual(labelTwo, "or")

    def test_center(self):
        center = self.main.center.isVisible()
        self.assertEqual(center, False)
        self.assertEqual(self.main.center.objectName(), "outer")
        self.assertEqual(self.main.center.layout(), self.main.mainHLayout)

    def test_labelMainUi(self):
        save = self.main.saveButton.text()
        next = self.main.nextButton.text()
        end = self.main.endButton.text()
        self.assertEqual(save, "SAVE")
        self.assertEqual(next, "NEXT")
        self.assertEqual(end, "QUIT")

    def test_layoutContainsWidgets(self):
        layout = self.drop.layout.layout()
        count = self.drop.layout.count()
        self.assertEqual(count, 3)
        for i in [self.drop.label, self.drop.label2, self.drop.browserButton]:
            self.drop.layout.removeWidget(i)
        countUpdate = self.drop.layout.count()
        self.assertEqual(countUpdate, 0)

    def test_browseButtonConfigDropUi(self):
        button = self.drop.browserButton.text()
        self.assertEqual(self.drop.browserButton.isVisible(), False)
        self.assertEqual(button, "Choose file")
        self.assertEqual(self.drop.browserButton.objectName(), "browserButton")

    # def test_getDistance(self, number, number1):
    #     number[0] = 5.5
    #     number1[0] = 6.7
    #     result = graphicOperations._get_distance(int)(number[0], number1[0])
    #     self.assertEqual(result, 0.51313443543513513513)
    #
    # def test_editBrowseButton(self):
    #     edit = EditUi(self.sw, 1, self.main.fileNameLabel, self.main.canvas)

    def test_isImage(self):
        file_name = "test.jpg"
        file_name = file_name[file_name.rfind(".") + 1:]
        global bool
        if file_name in ["bmp", "jpeg", "jpg", "tiff", "png"]:
            bool = True
        else:
            bool = False
        self.assertEqual(bool,True)

    def test_isEmpty(self):
        global files

    # def test_buildButtonEdit(self):
    #     parent = self.main.scrollArea
    #     label = Label(parent, img, idx)
    #     frame = QFrame()

if __name__ == '__main__':
    unittest.main()
