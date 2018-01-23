import sys
import visualization as visutil
from PIL import Image, ImageFont, ImageDraw
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize
from PIL.ImageQt import ImageQt

class Visualizer(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(640, 480))
        self.setWindowTitle('Agent View')
        #
        # Create central widget + layout.
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        gridLayout = QGridLayout(centralWidget)
        centralWidget.setLayout(gridLayout)
        #
        # Data structures for generating visualization.
        self.rgbTable = visutil.rtobTable()
        #
        # Rest of the GUI.
        self.lab = QLabel('Image', self)
        self.image = QLabel('', self)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        gridLayout.addWidget(self.lab, 0, 0)
        gridLayout.addWidget(self.image, 1, 0)
        self.show()

    def visualize(self, obs, action, agent):
        #
        # Generate image.
        img = Image.fromarray(obs['img'].decompressPNG()[:,:,0:3])
        draw = ImageDraw.Draw(img)
        print(action.meta['activations'])
        visutil.drawTrajectoryDots(0, 0, 7, img.size, self.rgbTable, draw, agent.nnconf, action.meta['activations'])
        #
        # Convert to Qt for presentation.
        imgqt = ImageQt(img)
        pix = QtGui.QPixmap.fromImage(imgqt)
        self.image.setPixmap(pix)
        # self.title.setText('index: %s'%idx.val)
        QApplication.processEvents()
