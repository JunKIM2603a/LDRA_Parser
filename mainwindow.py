# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QListView,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(804, 883)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(109, 10, 311, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_src_folder = QPushButton(self.horizontalLayoutWidget_2)
        self.btn_src_folder.setObjectName(u"btn_src_folder")

        self.horizontalLayout_2.addWidget(self.btn_src_folder)

        self.label_src_folder_path = QLabel(self.horizontalLayoutWidget_2)
        self.label_src_folder_path.setObjectName(u"label_src_folder_path")

        self.horizontalLayout_2.addWidget(self.label_src_folder_path)

        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(110, 60, 481, 41))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_htm_folder = QPushButton(self.horizontalLayoutWidget_3)
        self.btn_htm_folder.setObjectName(u"btn_htm_folder")

        self.horizontalLayout_4.addWidget(self.btn_htm_folder)

        self.label_htm_folder_path = QLabel(self.horizontalLayoutWidget_3)
        self.label_htm_folder_path.setObjectName(u"label_htm_folder_path")
        self.label_htm_folder_path.setTextFormat(Qt.TextFormat.AutoText)

        self.horizontalLayout_4.addWidget(self.label_htm_folder_path)

        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(610, 10, 171, 41))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_start = QPushButton(self.horizontalLayoutWidget_4)
        self.btn_start.setObjectName(u"btn_start")

        self.horizontalLayout_5.addWidget(self.btn_start)

        self.label_Status = QLabel(self.horizontalLayoutWidget_4)
        self.label_Status.setObjectName(u"label_Status")

        self.horizontalLayout_5.addWidget(self.label_Status)

        self.horizontalLayoutWidget_5 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(610, 60, 171, 41))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_Restore = QPushButton(self.horizontalLayoutWidget_5)
        self.btn_Restore.setObjectName(u"btn_Restore")

        self.horizontalLayout_6.addWidget(self.btn_Restore)

        self.label_Result = QLabel(self.horizontalLayoutWidget_5)
        self.label_Result.setObjectName(u"label_Result")

        self.horizontalLayout_6.addWidget(self.label_Result)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 110, 171, 711))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_src_files = QLabel(self.verticalLayoutWidget)
        self.label_src_files.setObjectName(u"label_src_files")
        self.label_src_files.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout.addWidget(self.label_src_files)

        self.listView_src_files = QListView(self.verticalLayoutWidget)
        self.listView_src_files.setObjectName(u"listView_src_files")

        self.verticalLayout.addWidget(self.listView_src_files)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(220, 110, 171, 711))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_result_files = QLabel(self.verticalLayoutWidget_2)
        self.label_result_files.setObjectName(u"label_result_files")
        self.label_result_files.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout_2.addWidget(self.label_result_files)

        self.listView_result_files = QListView(self.verticalLayoutWidget_2)
        self.listView_result_files.setObjectName(u"listView_result_files")

        self.verticalLayout_2.addWidget(self.listView_result_files)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(420, 110, 171, 711))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_result_rules = QLabel(self.verticalLayoutWidget_3)
        self.label_result_rules.setObjectName(u"label_result_rules")
        self.label_result_rules.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout_3.addWidget(self.label_result_rules)

        self.listView_result_rules = QListView(self.verticalLayoutWidget_3)
        self.listView_result_rules.setObjectName(u"listView_result_rules")

        self.verticalLayout_3.addWidget(self.listView_result_rules)

        self.verticalLayoutWidget_4 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(610, 110, 171, 711))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_result_sel_file = QLabel(self.verticalLayoutWidget_4)
        self.label_result_sel_file.setObjectName(u"label_result_sel_file")
        self.label_result_sel_file.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout_4.addWidget(self.label_result_sel_file)

        self.treeWidget_result = QTreeWidget(self.verticalLayoutWidget_4)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget_result.setHeaderItem(__qtreewidgetitem)
        self.treeWidget_result.setObjectName(u"treeWidget_result")

        self.verticalLayout_4.addWidget(self.treeWidget_result)

        self.verticalLayoutWidget_5 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(20, 9, 82, 91))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.comboBox_Stage = QComboBox(self.verticalLayoutWidget_5)
        self.comboBox_Stage.addItem("")
        self.comboBox_Stage.addItem("")
        self.comboBox_Stage.setObjectName(u"comboBox_Stage")

        self.verticalLayout_5.addWidget(self.comboBox_Stage)

        self.comboBox_Rule = QComboBox(self.verticalLayoutWidget_5)
        self.comboBox_Rule.addItem("")
        self.comboBox_Rule.addItem("")
        self.comboBox_Rule.setObjectName(u"comboBox_Rule")

        self.verticalLayout_5.addWidget(self.comboBox_Rule)

        self.btn_extract_data = QPushButton(self.centralwidget)
        self.btn_extract_data.setObjectName(u"btn_extract_data")
        self.btn_extract_data.setGeometry(QRect(430, 20, 156, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 804, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_src_folder.setText(QCoreApplication.translate("MainWindow", u"\uc18c\uc2a4\ucf54\ub4dc \ud3f4\ub354 \uc5f4\uae30", None))
        self.label_src_folder_path.setText(QCoreApplication.translate("MainWindow", u"\uc18c\uc2a4\ucf54\ub4dc \ud3f4\ub354 \uc8fc\uc18c", None))
        self.btn_htm_folder.setText(QCoreApplication.translate("MainWindow", u"LDRA htm \ud3f4\ub354 \uc5f4\uae30", None))
        self.label_htm_folder_path.setText(QCoreApplication.translate("MainWindow", u"LDRA htm \ud3f4\ub354 \uc8fc\uc18c(ex> SDI_Vpx3C3_MISRA_tbwrkfls)", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791", None))
        self.label_Status.setText(QCoreApplication.translate("MainWindow", u"\uc0c1\ud0dc", None))
        self.btn_Restore.setText(QCoreApplication.translate("MainWindow", u"Restore", None))
        self.label_Result.setText(QCoreApplication.translate("MainWindow", u"default", None))
        self.label_src_files.setText(QCoreApplication.translate("MainWindow", u"\uac80\ucd9c\ub300\uc0c1 \ud30c\uc77c(\uc18c\uc2a4\ucf54\ub4dc)", None))
        self.label_result_files.setText(QCoreApplication.translate("MainWindow", u"\uac80\ucd9c\ub41c \ud30c\uc77c \ub9ac\uc2a4\ud2b8", None))
        self.label_result_rules.setText(QCoreApplication.translate("MainWindow", u"Rule \ubcc4 \uac80\ucd9c \uac1c\uc218", None))
        self.label_result_sel_file.setText(QCoreApplication.translate("MainWindow", u"\uc120\ud0dd\ub41c \ud30c\uc77c\uc758 \uac80\ucd9c\ub0b4\uc6a9", None))
        self.comboBox_Stage.setItemText(0, QCoreApplication.translate("MainWindow", u"DT", None))
        self.comboBox_Stage.setItemText(1, QCoreApplication.translate("MainWindow", u"OT", None))

        self.comboBox_Rule.setItemText(0, QCoreApplication.translate("MainWindow", u"MISRA", None))
        self.comboBox_Rule.setItemText(1, QCoreApplication.translate("MainWindow", u"CWE", None))

        self.btn_extract_data.setText(QCoreApplication.translate("MainWindow", u"Extract Detection Lines", None))
    # retranslateUi

