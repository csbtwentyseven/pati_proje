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
        MainWindow.resize(849, 685)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 10, 831, 681))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(20, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.info_layout = QtWidgets.QHBoxLayout()
        self.info_layout.setContentsMargins(0, 0, 0, 0)
        self.info_layout.setObjectName("info_layout")
        self.Su_Sekmesi = QtWidgets.QTabWidget(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Su_Sekmesi.sizePolicy().hasHeightForWidth())
        self.Su_Sekmesi.setSizePolicy(sizePolicy)
        self.Su_Sekmesi.setMinimumSize(QtCore.QSize(250, 200))
        self.Su_Sekmesi.setMaximumSize(QtCore.QSize(250, 200))
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
        self.info_layout.addWidget(self.Su_Sekmesi)
        self.Kum_Sekmesi = QtWidgets.QTabWidget(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Kum_Sekmesi.sizePolicy().hasHeightForWidth())
        self.Kum_Sekmesi.setSizePolicy(sizePolicy)
        self.Kum_Sekmesi.setMinimumSize(QtCore.QSize(250, 200))
        self.Kum_Sekmesi.setMaximumSize(QtCore.QSize(250, 200))
        self.Kum_Sekmesi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Kum_Sekmesi.setIconSize(QtCore.QSize(16, 16))
        self.Kum_Sekmesi.setObjectName("Kum_Sekmesi")
        self.Kum_Kabi_Sekme = QtWidgets.QWidget()
        self.Kum_Kabi_Sekme.setObjectName("Kum_Kabi_Sekme")
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.Kum_Kabi_Sekme)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(0, 0, 251, 81))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.kumkap_label = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Lato Heavy")
        font.setBold(True)
        font.setWeight(75)
        self.kumkap_label.setFont(font)
        self.kumkap_label.setAlignment(QtCore.Qt.AlignCenter)
        self.kumkap_label.setObjectName("kumkap_label")
        self.verticalLayout_9.addWidget(self.kumkap_label)
        self.kumkap_data = QtWidgets.QLabel(self.verticalLayoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.kumkap_data.setFont(font)
        self.kumkap_data.setAccessibleName("")
        self.kumkap_data.setAlignment(QtCore.Qt.AlignCenter)
        self.kumkap_data.setObjectName("kumkap_data")
        self.verticalLayout_9.addWidget(self.kumkap_data)
        self.verticalLayoutWidget_9.raise_()
        self.Kum_Sekmesi.addTab(self.Kum_Kabi_Sekme, "")
        self.Kum_Deposu_Sekme = QtWidgets.QWidget()
        self.Kum_Deposu_Sekme.setObjectName("Kum_Deposu_Sekme")
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.Kum_Deposu_Sekme)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(0, 0, 251, 81))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.kumdepo_label = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        font = QtGui.QFont()
        font.setFamily("Lato Heavy")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.kumdepo_label.setFont(font)
        self.kumdepo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.kumdepo_label.setObjectName("kumdepo_label")
        self.verticalLayout_10.addWidget(self.kumdepo_label)
        self.kumdepo_data = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        font = QtGui.QFont()
        font.setFamily("Lato")
        self.kumdepo_data.setFont(font)
        self.kumdepo_data.setAlignment(QtCore.Qt.AlignCenter)
        self.kumdepo_data.setObjectName("kumdepo_data")
        self.verticalLayout_10.addWidget(self.kumdepo_data)
        self.Kum_Sekmesi.addTab(self.Kum_Deposu_Sekme, "")
        self.info_layout.addWidget(self.Kum_Sekmesi)
        self.Mama_Sekmesi = QtWidgets.QTabWidget(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Mama_Sekmesi.sizePolicy().hasHeightForWidth())
        self.Mama_Sekmesi.setSizePolicy(sizePolicy)
        self.Mama_Sekmesi.setMinimumSize(QtCore.QSize(250, 200))
        self.Mama_Sekmesi.setMaximumSize(QtCore.QSize(250, 200))
        self.Mama_Sekmesi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Mama_Sekmesi.setTabShape(QtWidgets.QTabWidget.Rounded)
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
        self.info_layout.addWidget(self.Mama_Sekmesi)
        self.verticalLayout_3.addLayout(self.info_layout)
        self.InternetveKameraSekmesi = QtWidgets.QTabWidget(self.verticalLayoutWidget_3)
        self.InternetveKameraSekmesi.setMinimumSize(QtCore.QSize(0, 150))
        self.InternetveKameraSekmesi.setObjectName("InternetveKameraSekmesi")
        self.Tarayici_tab = QtWidgets.QWidget()
        self.Tarayici_tab.setObjectName("Tarayici_tab")
        self.Tarayici = QtWebKitWidgets.QWebView(self.Tarayici_tab)
        self.Tarayici.setGeometry(QtCore.QRect(0, 0, 801, 1000))
        self.Tarayici.setMinimumSize(QtCore.QSize(0, 150))
        self.Tarayici.setUrl(QtCore.QUrl("https://www.google.com.tr/"))
        self.Tarayici.setZoomFactor(0.850000023841858)
        self.Tarayici.setObjectName("Tarayici")
        self.InternetveKameraSekmesi.addTab(self.Tarayici_tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.CanliGoruntu = QtWebKitWidgets.QWebView(self.tab_2)
        self.CanliGoruntu.setGeometry(QtCore.QRect(0, 0, 801, 4100))
        self.CanliGoruntu.setMinimumSize(QtCore.QSize(0, 100))
        self.CanliGoruntu.setUrl(QtCore.QUrl("http://localhost/"))
        self.CanliGoruntu.setObjectName("CanliGoruntu")
        self.CanliGoruntu.raise_()
        self.InternetveKameraSekmesi.addTab(self.tab_2, "")
        self.verticalLayout_3.addWidget(self.InternetveKameraSekmesi)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Su_Sekmesi.setCurrentIndex(0)
        self.Kum_Sekmesi.setCurrentIndex(0)
        self.Mama_Sekmesi.setCurrentIndex(0)
        self.InternetveKameraSekmesi.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sukap_label.setText(_translate("MainWindow", "Su Kabının Durumu:"))
        self.sukap_data.setText(_translate("MainWindow", "Veri Bulunamadı"))
        self.Su_Sekmesi.setTabText(self.Su_Sekmesi.indexOf(self.Su_Kabi_Sekme), _translate("MainWindow", "Su Kabı"))
        self.sudepo_label.setText(_translate("MainWindow", "Su Deposunun Durumu:"))
        self.sudepo_data.setText(_translate("MainWindow", "Veri Bulunamadı"))
        self.Su_Sekmesi.setTabText(self.Su_Sekmesi.indexOf(self.Su_Deposu_Sekme), _translate("MainWindow", "Su Deposu"))
        self.kumkap_label.setText(_translate("MainWindow", "Kum Kabının Durumu:"))
        self.kumkap_data.setText(_translate("MainWindow", "Veri Bulunamadı"))
        self.Kum_Sekmesi.setTabText(self.Kum_Sekmesi.indexOf(self.Kum_Kabi_Sekme), _translate("MainWindow", "Kum Kabı"))
        self.kumdepo_label.setText(_translate("MainWindow", "Kum Deposunun Durumu:"))
        self.kumdepo_data.setText(_translate("MainWindow", "Veri Bulunamadı"))
        self.Kum_Sekmesi.setTabText(self.Kum_Sekmesi.indexOf(self.Kum_Deposu_Sekme), _translate("MainWindow", "Kum Deposu"))
        self.Mamakap_label.setText(_translate("MainWindow", "Mama Kabının Durumu:"))
        self.mamakap_data.setText(_translate("MainWindow", "Veri Bulunamadı"))
        self.Mama_Sekmesi.setTabText(self.Mama_Sekmesi.indexOf(self.Mama_Kabi_Sekme), _translate("MainWindow", "Mama Kabı"))
        self.mamadepo_label.setText(_translate("MainWindow", "Mama Deposunun Durumu:"))
        self.mamadepo_data.setText(_translate("MainWindow", "Veri Bulunamadı"))
        self.Mama_Sekmesi.setTabText(self.Mama_Sekmesi.indexOf(self.Mama_Depo_Sekme), _translate("MainWindow", "Mama Deposu"))
        self.InternetveKameraSekmesi.setTabText(self.InternetveKameraSekmesi.indexOf(self.Tarayici_tab), _translate("MainWindow", "İnternet Tarayıcısı"))
        self.InternetveKameraSekmesi.setTabText(self.InternetveKameraSekmesi.indexOf(self.tab_2), _translate("MainWindow", "Kulube İçi Canlı Görüntü"))

from PyQt5 import QtWebKitWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

