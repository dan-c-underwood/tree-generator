# coding=utf-8
"""
File mostly generated from generator.ui and pyuic4. Initialises and manages the GUI for the tree generator.
"""
from builtins import str
from builtins import range
import configparser
import tempfile
import re
import os
import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog, QApplication

import tree_gen


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(QtGui.QMainWindow):
    designs = []

    def setupUi(self, MainWindow):
        self.directory = os.path.realpath(".")
        design_files = [f for f in os.listdir('./designs') if re.match(r'[a-zA-Z0-9_]+\.ini', f)]
        for design_file in design_files:
            if design_file != 'default.ini':
                design_file = "./designs/" + design_file
                try:
                    config = configparser.RawConfigParser()
                    config.read(design_file)
                    listing = config.get("details", "design_name"), design_file
                    self.designs.append(listing)
                except configparser.NoSectionError:
                    print("Warning: design file " + design_file + " does not contain name for design", file=sys.stderr)

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(961, 523)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(250, 40, 331, 423))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.randomBox = QtGui.QCheckBox(self.layoutWidget)
        self.randomBox.setObjectName(_fromUtf8("randomBox"))
        self.verticalLayout_4.addWidget(self.randomBox)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.treeParaLabel = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.treeParaLabel.setFont(font)
        self.treeParaLabel.setObjectName(_fromUtf8("treeParaLabel"))
        self.verticalLayout_3.addWidget(self.treeParaLabel)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.radiusLabel = QtGui.QLabel(self.splitter)
        self.radiusLabel.setObjectName(_fromUtf8("radiusLabel"))
        self.radiusSpinBox = QtGui.QDoubleSpinBox(self.splitter)
        self.radiusSpinBox.setEnabled(True)
        self.radiusSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.radiusSpinBox.setDecimals(1)
        self.radiusSpinBox.setSingleStep(0.1)
        self.radiusSpinBox.setProperty("value", 1.0)
        self.radiusSpinBox.setObjectName(_fromUtf8("radiusSpinBox"))
        self.verticalLayout.addWidget(self.splitter)
        self.splitter_3 = QtGui.QSplitter(self.layoutWidget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.lengthLabel = QtGui.QLabel(self.splitter_3)
        self.lengthLabel.setObjectName(_fromUtf8("lengthLabel"))
        self.lengthSpinBox = QtGui.QDoubleSpinBox(self.splitter_3)
        self.lengthSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.lengthSpinBox.setDecimals(1)
        self.lengthSpinBox.setSingleStep(0.1)
        self.lengthSpinBox.setProperty("value", 10.0)
        self.lengthSpinBox.setObjectName(_fromUtf8("lengthSpinBox"))
        self.verticalLayout.addWidget(self.splitter_3)
        self.splitter_4 = QtGui.QSplitter(self.layoutWidget)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName(_fromUtf8("splitter_4"))
        self.angleLabel = QtGui.QLabel(self.splitter_4)
        self.angleLabel.setObjectName(_fromUtf8("angleLabel"))
        self.angleSpinBox = QtGui.QSpinBox(self.splitter_4)
        self.angleSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.angleSpinBox.setMinimum(1)
        self.angleSpinBox.setMaximum(90)
        self.angleSpinBox.setProperty("value", 30)
        self.angleSpinBox.setObjectName(_fromUtf8("angleSpinBox"))
        self.verticalLayout.addWidget(self.splitter_4)
        self.splitter_5 = QtGui.QSplitter(self.layoutWidget)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName(_fromUtf8("splitter_5"))
        self.bRatioLabel = QtGui.QLabel(self.splitter_5)
        self.bRatioLabel.setObjectName(_fromUtf8("bRatioLabel"))
        self.bRatioSpinBox = QtGui.QDoubleSpinBox(self.splitter_5)
        self.bRatioSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.bRatioSpinBox.setDecimals(1)
        self.bRatioSpinBox.setMinimum(0.1)
        self.bRatioSpinBox.setMaximum(1.0)
        self.bRatioSpinBox.setSingleStep(0.1)
        self.bRatioSpinBox.setProperty("value", 0.5)
        self.bRatioSpinBox.setObjectName(_fromUtf8("bRatioSpinBox"))
        self.verticalLayout.addWidget(self.splitter_5)
        self.splitter_6 = QtGui.QSplitter(self.layoutWidget)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName(_fromUtf8("splitter_6"))
        self.sRatiolabel = QtGui.QLabel(self.splitter_6)
        self.sRatiolabel.setObjectName(_fromUtf8("sRatiolabel"))
        self.sRatioSpinBox = QtGui.QDoubleSpinBox(self.splitter_6)
        self.sRatioSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.sRatioSpinBox.setDecimals(1)
        self.sRatioSpinBox.setMinimum(0.1)
        self.sRatioSpinBox.setMaximum(1.0)
        self.sRatioSpinBox.setSingleStep(0.1)
        self.sRatioSpinBox.setProperty("value", 0.7)
        self.sRatioSpinBox.setObjectName(_fromUtf8("sRatioSpinBox"))
        self.verticalLayout.addWidget(self.splitter_6)
        self.splitter_7 = QtGui.QSplitter(self.layoutWidget)
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setObjectName(_fromUtf8("splitter_7"))
        self.branchesLabel = QtGui.QLabel(self.splitter_7)
        self.branchesLabel.setObjectName(_fromUtf8("branchesLabel"))
        self.branchesSpinBox = QtGui.QSpinBox(self.splitter_7)
        self.branchesSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.branchesSpinBox.setMaximum(10)
        self.branchesSpinBox.setProperty("value", 3)
        self.branchesSpinBox.setObjectName(_fromUtf8("branchesSpinBox"))
        self.verticalLayout.addWidget(self.splitter_7)
        self.splitter_8 = QtGui.QSplitter(self.layoutWidget)
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setObjectName(_fromUtf8("splitter_8"))
        self.depthLabel = QtGui.QLabel(self.splitter_8)
        self.depthLabel.setObjectName(_fromUtf8("depthLabel"))
        self.depthSpinBox = QtGui.QSpinBox(self.splitter_8)
        self.depthSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.depthSpinBox.setMinimum(1)
        self.depthSpinBox.setMaximum(7)
        self.depthSpinBox.setProperty("value", 4)
        self.depthSpinBox.setObjectName(_fromUtf8("depthSpinBox"))
        self.verticalLayout.addWidget(self.splitter_8)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.line = QtGui.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_3.addWidget(self.line)
        self.leafParaLabel = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.leafParaLabel.setFont(font)
        self.leafParaLabel.setObjectName(_fromUtf8("leafParaLabel"))
        self.verticalLayout_3.addWidget(self.leafParaLabel)
        self.splitter_9 = QtGui.QSplitter(self.layoutWidget)
        self.splitter_9.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_9.setObjectName(_fromUtf8("splitter_9"))
        self.lLengthLabel = QtGui.QLabel(self.splitter_9)
        self.lLengthLabel.setObjectName(_fromUtf8("lLengthLabel"))
        self.lLengthSpinBox = QtGui.QDoubleSpinBox(self.splitter_9)
        self.lLengthSpinBox.setEnabled(True)
        self.lLengthSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.lLengthSpinBox.setSingleStep(0.01)
        self.lLengthSpinBox.setProperty("value", 0.5)
        self.lLengthSpinBox.setObjectName(_fromUtf8("lLengthSpinBox"))
        self.verticalLayout_3.addWidget(self.splitter_9)
        self.splitter_10 = QtGui.QSplitter(self.layoutWidget)
        self.splitter_10.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_10.setObjectName(_fromUtf8("splitter_10"))
        self.lWidthLabel = QtGui.QLabel(self.splitter_10)
        self.lWidthLabel.setObjectName(_fromUtf8("lWidthLabel"))
        self.lWidthSpinBox = QtGui.QDoubleSpinBox(self.splitter_10)
        self.lWidthSpinBox.setEnabled(True)
        self.lWidthSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.lWidthSpinBox.setSingleStep(0.01)
        self.lWidthSpinBox.setProperty("value", 0.25)
        self.lWidthSpinBox.setObjectName(_fromUtf8("lWidthSpinBox"))
        self.verticalLayout_3.addWidget(self.splitter_10)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(590, 40, 20, 411))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.logoBox = QtGui.QLabel(self.centralwidget)
        self.logoBox.setGeometry(QtCore.QRect(20, 40, 218, 411))
        self.logoBox.setText(_fromUtf8(""))
        self.logoBox.setObjectName(_fromUtf8("logoBox"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 480, 901, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.generateButton = QtGui.QPushButton(self.centralwidget)
        self.generateButton.setEnabled(True)
        self.generateButton.setGeometry(QtCore.QRect(650, 310, 261, 131))
        self.generateButton.setAutoDefault(False)
        self.generateButton.setDefault(False)
        self.generateButton.setFlat(False)
        self.generateButton.setObjectName(_fromUtf8("generateButton"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(620, 280, 321, 20))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(620, 40, 311, 219))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.defaultBox = QtGui.QCheckBox(self.layoutWidget1)
        self.defaultBox.setObjectName(_fromUtf8("defaultBox"))
        self.verticalLayout_5.addWidget(self.defaultBox)
        self.existingBox = QtGui.QCheckBox(self.layoutWidget1)
        self.existingBox.setObjectName(_fromUtf8("existingBox"))
        self.verticalLayout_5.addWidget(self.existingBox)
        self.designList = QtGui.QComboBox(self.layoutWidget1)
        self.designList.setObjectName(_fromUtf8("designList"))
        self.verticalLayout_5.addWidget(self.designList)
        self.splitter_11 = QtGui.QSplitter(self.layoutWidget1)
        self.splitter_11.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_11.setObjectName(_fromUtf8("splitter_11"))
        self.directoryLabel = QtGui.QLabel(self.splitter_11)
        self.directoryLabel.setObjectName(_fromUtf8("directoryLabel"))
        self.directoryButton = QtGui.QPushButton(self.splitter_11)
        self.directoryButton.setObjectName(_fromUtf8("directoryButton"))
        self.verticalLayout_5.addWidget(self.splitter_11)
        self.sciptParaLabel = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.sciptParaLabel.setFont(font)
        self.sciptParaLabel.setObjectName(_fromUtf8("sciptParaLabel"))
        self.verticalLayout_5.addWidget(self.sciptParaLabel)
        self.line_3 = QtGui.QFrame(self.layoutWidget1)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_5.addWidget(self.line_3)
        self.splitter_2 = QtGui.QSplitter(self.layoutWidget1)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.facesLabel = QtGui.QLabel(self.splitter_2)
        self.facesLabel.setObjectName(_fromUtf8("facesLabel"))
        self.facesSpinBox = QtGui.QSpinBox(self.splitter_2)
        self.facesSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.facesSpinBox.setMinimum(3)
        self.facesSpinBox.setMaximum(20)
        self.facesSpinBox.setProperty("value", 6)
        self.facesSpinBox.setObjectName(_fromUtf8("facesSpinBox"))
        self.verticalLayout_5.addWidget(self.splitter_2)
        self.splitter_12 = QtGui.QSplitter(self.layoutWidget1)
        self.splitter_12.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_12.setObjectName(_fromUtf8("splitter_12"))
        self.treesLabel = QtGui.QLabel(self.splitter_12)
        self.treesLabel.setObjectName(_fromUtf8("treesLabel"))
        self.treesSpinBox = QtGui.QSpinBox(self.splitter_12)
        self.treesSpinBox.setMinimum(1)
        self.treesSpinBox.setObjectName(_fromUtf8("treesSpinBox"))
        self.verticalLayout_5.addWidget(self.splitter_12)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        logo = QtGui.QPixmap("logo.png")
        self.logoBox.setPixmap(logo)
        self.statusbar.showMessage("Models will be saved in: " + self.directory)
        self.designList.clear()
        self.designList.addItems([item[0] for item in self.designs])
        self.designList.setDisabled(True)

        self.generateButton.clicked.connect(self._generate)
        self.directoryButton.clicked.connect(self._get_directory)
        self.defaultBox.toggled.connect(self._toggle_default)
        self.existingBox.toggled.connect(self._toggle_existing)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Tree Builder", None))
        self.randomBox.setToolTip(_translate("MainWindow",
                                             "<html><head/><body><p>Turns on randomness for some parts of the tree generation process. This uses a normal distribution centred around the values given.</p></body></html>",
                                             None))
        self.randomBox.setText(_translate("MainWindow", "Enable randomness?", None))
        self.treeParaLabel.setText(_translate("MainWindow", "Tree Parameters", None))
        self.splitter.setToolTip(_translate("MainWindow",
                                            "<html><head/><body><p>Sets the initial width of the trunk at the base of the tree. The rate at which the width decreases is set by the stem ratio.</p></body></html>",
                                            None))
        self.radiusLabel.setText(_translate("MainWindow", "Initial Trunk Radius", None))
        self.radiusSpinBox.setSuffix(_translate("MainWindow", "m", None))
        self.splitter_3.setToolTip(_translate("MainWindow",
                                              "<html><head/><body><p>Sets the length of the initial segment of trunk. If this value is increased then the tree will be taller, the amount the height of a segment of trunk decreases is set by the stem ratio.</p></body></html>",
                                              None))
        self.lengthLabel.setText(_translate("MainWindow", "Initial Trunk Length", None))
        self.lengthSpinBox.setSuffix(_translate("MainWindow", "m", None))
        self.splitter_4.setToolTip(_translate("MainWindow",
                                              "<html><head/><body><p>Sets the angle between the trunk and a branch.</p></body></html>",
                                              None))
        self.angleLabel.setText(_translate("MainWindow", "Branch Angle", None))
        self.angleSpinBox.setSuffix(_translate("MainWindow", "°", None))
        self.splitter_5.setToolTip(_translate("MainWindow",
                                              "<html><head/><body><p>Controls the ratio between the size of the trunk and the branches going off of it. A higher ratio value will give larger branches.</p></body></html>",
                                              None))
        self.bRatioLabel.setText(_translate("MainWindow", "Branch Size Ratio", None))
        self.splitter_6.setToolTip(_translate("MainWindow",
                                              "<html><head/><body><p>Controls the ratio between segments of trunk (and branches). A lower value will mean the tree \'tapers\' off more quickly.</p></body></html>",
                                              None))
        self.sRatiolabel.setText(_translate("MainWindow", "Stem Size Ratio", None))
        self.splitter_7.setToolTip(_translate("MainWindow",
                                              "<html><head/><body><p>This sets how many branches will appear at each trunk segment.</p></body></html>",
                                              None))
        self.branchesLabel.setText(_translate("MainWindow", "No. of Branches Per Level", None))
        self.splitter_8.setToolTip(_translate("MainWindow",
                                              "<html><head/><body><p>This value controls the maximum depth of <span style=\" font-weight:600;\">recursion</span> that the generator will go to. The effect of this value being increase is that the tree will appear to be more grown.</p></body></html>",
                                              None))
        self.depthLabel.setText(_translate("MainWindow", "Level of Growth", None))
        self.leafParaLabel.setText(_translate("MainWindow", "Leaf Parameters", None))
        self.splitter_9.setToolTip(_translate("MainWindow",
                                              "<html><head/><body><p>Sets the width of the leaves on the tree.</p></body></html>",
                                              None))
        self.lLengthLabel.setText(_translate("MainWindow", "Length", None))
        self.lLengthSpinBox.setSuffix(_translate("MainWindow", "m", None))
        self.splitter_10.setToolTip(_translate("MainWindow",
                                               "<html><head/><body><p>Sets the length of the leaves on the tree.</p></body></html>",
                                               None))
        self.lWidthLabel.setText(_translate("MainWindow", "Width", None))
        self.lWidthSpinBox.setSuffix(_translate("MainWindow", "m", None))
        self.generateButton.setText(_translate("MainWindow", "Generate Tree(s)", None))
        self.defaultBox.setToolTip(_translate("MainWindow",
                                              "<html><head/><body><p>Use the default settings provided, guaranteed to produce a &quot;tree-like&quot; model</p></body></html>",
                                              None))
        self.defaultBox.setText(_translate("MainWindow", "Use default settings?", None))
        self.existingBox.setToolTip(_translate("MainWindow",
                                               "<html><head/><body><p>Choose a design from a premade set of preferences.</p></body></html>",
                                               None))
        self.existingBox.setText(_translate("MainWindow", "Use an existing design?", None))
        self.designList.setToolTip(
            _translate("MainWindow", "<html><head/><body><p>List of usable designs.</p></body></html>", None))
        self.splitter_11.setToolTip(_translate("MainWindow",
                                               "<html><head/><body><p>Set the directory that the generated models will be placed in.</p></body></html>",
                                               None))
        self.directoryLabel.setText(_translate("MainWindow", "Choose directory for models:", None))
        self.directoryButton.setText(_translate("MainWindow", "Select", None))
        self.sciptParaLabel.setText(_translate("MainWindow", "Script Parameters", None))
        self.splitter_2.setToolTip(_translate("MainWindow",
                                              "<html><head/><body><p>Set the number of faces per segment of trunk. This makes the final file size larger but the model will appear more natural.</p></body></html>",
                                              None))
        self.facesLabel.setText(_translate("MainWindow", "Faces per Segment", None))
        self.splitter_12.setToolTip(_translate("MainWindow",
                                               "<html><head/><body><p>Set the number of trees to make when the &quot;Generate Tree(s)!&quot; button is pressed.</p></body></html>",
                                               None))
        self.treesLabel.setText(_translate("MainWindow", "How many trees?", None))

    def _toggle_default(self, enabled):
        self._toggle_fields(enabled)
        if enabled:
            self.existingBox.setDisabled(True)
        else:
            self.existingBox.setDisabled(False)

    def _toggle_existing(self, enabled):
        self._toggle_fields(enabled)
        if enabled:
            self.defaultBox.setDisabled(True)
            self.designList.setDisabled(False)
        else:
            self.defaultBox.setDisabled(False)
            self.designList.setDisabled(True)

    def _toggle_fields(self, enabled):
        if enabled:
            self.radiusSpinBox.setDisabled(True)
            self.lengthSpinBox.setDisabled(True)
            self.angleSpinBox.setDisabled(True)
            self.bRatioSpinBox.setDisabled(True)
            self.sRatioSpinBox.setDisabled(True)
            self.branchesSpinBox.setDisabled(True)
            self.depthSpinBox.setDisabled(True)
            self.lLengthSpinBox.setDisabled(True)
            self.lWidthSpinBox.setDisabled(True)
            self.facesSpinBox.setDisabled(True)
        else:
            self.radiusSpinBox.setDisabled(False)
            self.lengthSpinBox.setDisabled(False)
            self.angleSpinBox.setDisabled(False)
            self.bRatioSpinBox.setDisabled(False)
            self.sRatioSpinBox.setDisabled(False)
            self.branchesSpinBox.setDisabled(False)
            self.depthSpinBox.setDisabled(False)
            self.lLengthSpinBox.setDisabled(False)
            self.lWidthSpinBox.setDisabled(False)
            self.facesSpinBox.setDisabled(False)

    def _generate(self):
        self.progressBar.setValue(0)
        QApplication.processEvents()
        self.generateButton.setDisabled(True)
        progress_interval = 100 / self.treesSpinBox.value()
        randomness_en = not self.defaultBox.isChecked() and self.randomBox.isChecked()
        file_num_offset = 0
        for tree_num in range(self.treesSpinBox.value()):
            path = os.path.join(self.directory, "tree_" + str(tree_num + file_num_offset) + ".obj")
            while os.path.exists(path):
                file_num_offset += 1
                path = os.path.join(self.directory, "tree_" + str(tree_num + file_num_offset) + ".obj")
            self.statusbar.showMessage("Generating: tree_" + str(tree_num + file_num_offset) + ".obj")
            QApplication.processEvents()

            try:
                tree_gen.generate(self._get_pref_file(), randomness_en, path)
            except configparser.NoSectionError:
                self.statusbar.showMessage(
                    "Warning: design file " + self._get_pref_file() + " does not contain parameters", 5000)
                QApplication.processEvents()
            self.progressBar.setValue(self.progressBar.value() + progress_interval)
            QApplication.processEvents()
        self.progressBar.setValue(100)
        QApplication.processEvents()
        self.statusbar.showMessage("Models will be saved in: " + self.directory)
        QApplication.processEvents()
        self.generateButton.setDisabled(False)

    def _get_directory(self):
        self.directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.statusbar.showMessage("Models will be saved in: " + self.directory)

    def _get_pref_file(self):
        if self.defaultBox.isChecked():
            return 'designs/default.ini'
        if self.existingBox.isChecked():
            return self.designs[self.designList.currentIndex()][1]
        else:
            config = configparser.ConfigParser()
            config.add_section('params')
            config.set('params', 'radius', str(self.radiusSpinBox.value()))
            config.set('params', 'faces', str(self.facesSpinBox.value()))
            config.set('params', 'length', str(self.lengthSpinBox.value()))
            config.set('params', 'branch_angle', str(self.angleSpinBox.value()))
            config.set('params', 'branch_ratio', str(self.bRatioSpinBox.value()))
            config.set('params', 'stem_ratio', str(self.sRatioSpinBox.value()))
            config.set('params', 'branch_per_stem', str(self.branchesSpinBox.value()))
            config.set('params', 'max_depth', str(self.depthSpinBox.value()))
            config.set('params', 'leaf_length', str(self.lLengthSpinBox.value()))
            config.set('params', 'leaf_width', str(self.lWidthSpinBox.value()))

            with open(tempfile.NamedTemporaryFile(delete=False).name, 'w') as pref_file:
                config.write(pref_file)
                pref_file.flush()
                pref_file.close()
                return pref_file.name