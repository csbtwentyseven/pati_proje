# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(824, 477)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Mama_Sekmesi = QtWidgets.QTabWidget(self.centralwidget)
        self.Mama_Sekmesi.setGeometry(QtCore.QRect(560, 30, 251, 121))
        self.Mama_Sekmesi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Mama_Sekmesi.setIconSize(QtCore.QSize(16, 16))
        self.Mama_Sekmesi.setObjectName("Mama_Sekmesi")
        self.Mama_Kabi_Sekme = QtWidgets.QWidget()
        self.Mama_Kabi_Sekme.setObjectName("Mama_Kabi_Sekme")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Mama_Kabi_Sekme)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 251, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Mamakap_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lato Heavy")
        font.setBold(True)
        font.setWeight(75)
        self.Mamakap_label.setFont(font)
        self.Mamakap_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Mamakap_label.setObjectName("Mamakap_label")
        self.verticalLayout.addWidget(self.Mamakap_label)
        self.mamakap_data = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mamakap_data.setFont(font)
        self.mamakap_data.setAlignment(QtCore.Qt.AlignCenter)
        self.mamakap_data.setObjectName("mamakap_data")
        self.verticalLayout.addWidget(self.mamakap_data)
        self.Mama_Sekmesi.addTab(self.Mama_Kabi_Sekme, "")
        self.Mama_Depo_Sekme = QtWidgets.QWidget()
        self.Mama_Depo_Sekme.setObjectName("Mama_Depo_Sekme")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Mama_Depo_Sekme)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 251, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mamadepo_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Lato Heavy")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.mamadepo_label.setFont(font)
        self.mamadepo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mamadepo_label.setObjectName("mamadepo_label")
        self.verticalLayout_2.addWidget(self.mamadepo_label)
        self.mamadepo_data = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Lato")
        self.mamadepo_data.setFont(font)
        self.mamadepo_data.setAlignment(QtCore.Qt.AlignCenter)
        self.mamadepo_data.setObjectName("mamadepo_data")
        self.verticalLayout_2.addWidget(self.mamadepo_data)
        self.Mama_Sekmesi.addTab(self.Mama_Depo_Sekme, "")
        self.Su_Sekmesi = QtWidgets.QTabWidget(self.centralwidget)
        self.Su_Sekmesi.setGeometry(QtCore.QRect(30, 20, 251, 121))
        self.Su_Sekmesi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Su_Sekmesi.setIconSize(QtCore.QSize(16, 16))
        self.Su_Sekmesi.setObjectName("Su_Sekmesi")
        self.Su_Kabi_Sekme = QtWidgets.QWidget()
        self.Su_Kabi_Sekme.setObjectName("Su_Kabi_Sekme")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.Su_Kabi_Sekme)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 251, 81))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.sukap_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Lato Heavy")
        font.setBold(True)
        font.setWeight(75)
        self.sukap_label.setFont(font)
        self.sukap_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sukap_label.setObjectName("sukap_label")
        self.verticalLayout_5.addWidget(self.sukap_label)
        self.sukap_data = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.sukap_data.setFont(font)
        self.sukap_data.setAccessibleName("")
        self.sukap_data.setAlignment(QtCore.Qt.AlignCenter)
        self.sukap_data.setObjectName("sukap_data")
        self.verticalLayout_5.addWidget(self.sukap_data)
        self.Su_Sekmesi.addTab(self.Su_Kabi_Sekme, "")
        self.Su_Deposu_Sekme = QtWidgets.QWidget()
        self.Su_Deposu_Sekme.setObjectName("Su_Deposu_Sekme")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.Su_Deposu_Sekme)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(0, 0, 251, 81))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.sudepo_label = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Lato Heavy")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.sudepo_label.setFont(font)
        self.sudepo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sudepo_label.setObjectName("sudepo_label")
        self.verticalLayout_6.addWidget(self.sudepo_label)
        self.sudepo_data = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Lato")
        self.sudepo_data.setFont(font)
        self.sudepo_data.setAlignment(QtCore.Qt.AlignCenter)
        self.sudepo_data.setObjectName("sudepo_data")
        self.verticalLayout_6.addWidget(self.sudepo_data)
        self.Su_Sekmesi.addTab(self.Su_Deposu_Sekme, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Mama_Sekmesi.setCurrentIndex(0)
        self.Su_Sekmesi.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Mamakap_label.setText(_translate("MainWindow", "Mama Kabının Durumu:"))
        self.mamakap_data.setText(_translate("MainWindow", "Veri Bulunamadı"))
        self.Mama_Sekmesi.setTabText(self.Mama_Sekmesi.indexOf(self.Mama_Kabi_Sekme), _translate("MainWindow", "Mama Kabı"))
        self.mamadepo_label.setText(_translate("MainWindow", "Mama Deposunun Durumu:"))
        self.mamadepo_data.setText(_translate("MainWindow", "Veri Bulunamadı"))
        self.Mama_Sekmesi.setTabText(self.Mama_Sekmesi.indexOf(self.Mama_Depo_Sekme), _translate("MainWindow", "Mama Deposu"))
        self.sukap_label.setText(_translate("MainWindow", "Su Kabının Durumu:"))
        self.sukap_data.setText(_translate("MainWindow", "Veri Bulunamadı"))
        self.Su_Sekmesi.setTabText(self.Su_Sekmesi.indexOf(self.Su_Kabi_Sekme), _translate("MainWindow", "Su Kabı"))
        self.sudepo_label.setText(_translate("MainWindow", "Su Deposunun Durumu:"))
        self.sudepo_data.setText(_translate("MainWindow", "Veri Bulunamadı"))
        self.Su_Sekmesi.setTabText(self.Su_Sekmesi.indexOf(self.Su_Deposu_Sekme), _translate("MainWindow", "Su Deposu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
