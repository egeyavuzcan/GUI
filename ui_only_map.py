from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import datetime
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtGui import QTransform
from PyQt5.QtWidgets import QApplication
from numpy import random
from PyQt5 import QtCore, QtGui, QtWidgets
import dronekit
from dronekit import connect, VehicleMode, LocationGlobal, LocationGlobalRelative, Command ,Vehicle
import time
import math
from pymavlink import mavutil
import numpy
from PyQt5 import QtCore, QtGui, QtWidgets
vehicle = connect('127.0.0.1:14550', wait_ready=True)
class Ui_Form(QtWidgets.QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1618, 936)
        self.map = QtWidgets.QLabel(Form)
        self.map.setGeometry(QtCore.QRect(280, 90, 1281, 611))
        self.map.setText("")
        self.map.setPixmap(QtGui.QPixmap("/home/ege/Pictures/uçuş_alanı_yarışma_3.png"))
        self.map.setObjectName("map")
        self.ucak = QtWidgets.QLabel(Form)
        self.ucak.setGeometry(QtCore.QRect(260, 820, 31, 21))
        self.ucak.setText("")
        self.ucak.setPixmap(QtGui.QPixmap("/home/ege/Downloads/airliner_v3.png"))
        self.ucak.setObjectName("ucak")
        self.ucak_alt = QtWidgets.QLabel(Form)
        self.ucak_alt.setGeometry(QtCore.QRect(290, 820, 21, 21))
        self.ucak_alt.setObjectName("ucak_alt")
        self.ucak_alt_2 = QtWidgets.QLabel(Form)
        self.ucak_alt_2.setGeometry(QtCore.QRect(360, 820, 21, 21))
        self.ucak_alt_2.setObjectName("ucak_alt_2")
        self.ucak_2 = QtWidgets.QLabel(Form)
        self.ucak_2.setGeometry(QtCore.QRect(320, 820, 31, 21))
        self.ucak_2.setText("")
        self.ucak_2.setPixmap(QtGui.QPixmap("/home/ege/Downloads/airliner_v3.png"))
        self.ucak_2.setObjectName("ucak_2")
        self.ucak_alt_3 = QtWidgets.QLabel(Form)
        self.ucak_alt_3.setGeometry(QtCore.QRect(420, 820, 21, 21))
        self.ucak_alt_3.setObjectName("ucak_alt_3")
        self.ucak_3 = QtWidgets.QLabel(Form)
        self.ucak_3.setGeometry(QtCore.QRect(390, 820, 31, 21))
        self.ucak_3.setText("")
        self.ucak_3.setPixmap(QtGui.QPixmap("/home/ege/Downloads/airliner_v3.png"))
        self.ucak_3.setObjectName("ucak_3")
        self.ucak_alt_4 = QtWidgets.QLabel(Form)
        self.ucak_alt_4.setGeometry(QtCore.QRect(490, 820, 21, 21))
        self.ucak_alt_4.setObjectName("ucak_alt_4")
        self.ucak_4 = QtWidgets.QLabel(Form)
        self.ucak_4.setGeometry(QtCore.QRect(460, 820, 31, 21))
        self.ucak_4.setText("")
        self.ucak_4.setPixmap(QtGui.QPixmap("/home/ege/Downloads/airliner_v3.png"))
        self.ucak_4.setObjectName("ucak_4")
        self.ucak_alt_5 = QtWidgets.QLabel(Form)
        self.ucak_alt_5.setGeometry(QtCore.QRect(550, 820, 21, 21))
        self.ucak_alt_5.setObjectName("ucak_alt_5")
        self.ucak_5 = QtWidgets.QLabel(Form)
        self.ucak_5.setGeometry(QtCore.QRect(520, 820, 31, 21))
        self.ucak_5.setText("")
        self.ucak_5.setPixmap(QtGui.QPixmap("/home/ege/Downloads/airliner_v3.png"))
        self.ucak_5.setObjectName("ucak_5")
        self.ucak_alt_6 = QtWidgets.QLabel(Form)
        self.ucak_alt_6.setGeometry(QtCore.QRect(610, 820, 21, 21))
        self.ucak_alt_6.setObjectName("ucak_alt_6")
        self.ucak_6 = QtWidgets.QLabel(Form)
        self.ucak_6.setGeometry(QtCore.QRect(580, 820, 31, 21))
        self.ucak_6.setText("")
        self.ucak_6.setPixmap(QtGui.QPixmap("/home/ege/Downloads/airliner_v3.png"))
        self.ucak_6.setObjectName("ucak_6")
        self.ucak_alt_7 = QtWidgets.QLabel(Form)
        self.ucak_alt_7.setGeometry(QtCore.QRect(670, 820, 21, 21))
        self.ucak_alt_7.setObjectName("ucak_alt_7")
        self.ucak_7 = QtWidgets.QLabel(Form)
        self.ucak_7.setGeometry(QtCore.QRect(640, 820, 31, 21))
        self.ucak_7.setText("")
        self.ucak_7.setPixmap(QtGui.QPixmap("/home/ege/Downloads/airliner_v3.png"))
        self.ucak_7.setObjectName("ucak_7")
        self.ucak_alt_8 = QtWidgets.QLabel(Form)
        self.ucak_alt_8.setGeometry(QtCore.QRect(730, 820, 21, 21))
        self.ucak_alt_8.setObjectName("ucak_alt_8")
        self.ucak_8 = QtWidgets.QLabel(Form)
        self.ucak_8.setGeometry(QtCore.QRect(700, 820, 31, 21))
        self.ucak_8.setText("")
        self.ucak_8.setPixmap(QtGui.QPixmap("/home/ege/Downloads/airliner_v3.png"))
        self.ucak_8.setObjectName("ucak_8")
        self.ucak_alt_9 = QtWidgets.QLabel(Form)
        self.ucak_alt_9.setGeometry(QtCore.QRect(790, 820, 21, 21))
        self.ucak_alt_9.setObjectName("ucak_alt_9")
        self.ucak_9 = QtWidgets.QLabel(Form)
        self.ucak_9.setGeometry(QtCore.QRect(760, 820, 31, 21))
        self.ucak_9.setText("")
        self.ucak_9.setPixmap(QtGui.QPixmap("/home/ege/Downloads/airliner_v3.png"))
        self.ucak_9.setObjectName("ucak_9")
        self.ucak_alt_10 = QtWidgets.QLabel(Form)
        self.ucak_alt_10.setGeometry(QtCore.QRect(850, 820, 21, 21))
        self.ucak_alt_10.setObjectName("ucak_alt_10")
        self.ucak_10 = QtWidgets.QLabel(Form)
        self.ucak_10.setGeometry(QtCore.QRect(820, 820, 31, 21))
        self.ucak_10.setText("")
        self.ucak_10.setPixmap(QtGui.QPixmap("/home/ege/Downloads/airliner_v3.png"))
        self.ucak_10.setObjectName("ucak_10")
        self.ucak_alt_11 = QtWidgets.QLabel(Form)
        self.ucak_alt_11.setGeometry(QtCore.QRect(910, 820, 21, 21))
        self.ucak_alt_11.setObjectName("ucak_alt_11")
        self.ucak_11 = QtWidgets.QLabel(Form)
        self.ucak_11.setGeometry(QtCore.QRect(880, 820, 31, 21))
        self.ucak_11.setText("")
        self.ucak_11.setPixmap(QtGui.QPixmap("/home/ege/Downloads/airliner_v3.png"))
        self.ucak_11.setObjectName("ucak_11")
        self.ucak_alt_12 = QtWidgets.QLabel(Form)
        self.ucak_alt_12.setGeometry(QtCore.QRect(970, 820, 21, 21))
        self.ucak_alt_12.setObjectName("ucak_alt_12")
        self.ucak_12 = QtWidgets.QLabel(Form)
        self.ucak_12.setGeometry(QtCore.QRect(940, 820, 31, 21))
        self.ucak_12.setText("")
        self.ucak_12.setPixmap(QtGui.QPixmap("/home/ege/Downloads/airliner_v3.png"))
        self.ucak_12.setObjectName("ucak_12")
        self.ucak_alt_13 = QtWidgets.QLabel(Form)
        self.ucak_alt_13.setGeometry(QtCore.QRect(1040, 820, 21, 21))
        self.ucak_alt_13.setObjectName("ucak_alt_13")
        self.ucak_13 = QtWidgets.QLabel(Form)
        self.ucak_13.setGeometry(QtCore.QRect(1010, 820, 31, 21))
        self.ucak_13.setText("")
        self.ucak_13.setPixmap(QtGui.QPixmap("/home/ege/Downloads/airliner_v3.png"))
        self.ucak_13.setObjectName("ucak_13")
        self.ucak_alt_14 = QtWidgets.QLabel(Form)
        self.ucak_alt_14.setGeometry(QtCore.QRect(1110, 820, 21, 21))
        self.ucak_alt_14.setObjectName("ucak_alt_14")
        self.ucak_14 = QtWidgets.QLabel(Form)
        self.ucak_14.setGeometry(QtCore.QRect(1080, 820, 31, 21))
        self.ucak_14.setText("")
        self.ucak_14.setPixmap(QtGui.QPixmap("/home/ege/Downloads/airliner_v3.png"))
        self.ucak_14.setObjectName("ucak_14")
        self.ucak_alt_15 = QtWidgets.QLabel(Form)
        self.ucak_alt_15.setGeometry(QtCore.QRect(1170, 820, 21, 21))
        self.ucak_alt_15.setObjectName("ucak_alt_15")
        self.ucak_15 = QtWidgets.QLabel(Form)
        self.ucak_15.setGeometry(QtCore.QRect(1140, 820, 31, 21))
        self.ucak_15.setText("")
        self.ucak_15.setPixmap(QtGui.QPixmap("/home/ege/Downloads/airliner_v3.png"))
        self.ucak_15.setObjectName("ucak_15")
        self.bizim_ucak = QtWidgets.QLabel(Form)
        self.bizim_ucak.setGeometry(QtCore.QRect(260, 850, 41, 41))
        self.bizim_ucak.setText("")
        self.bizim_ucak.setPixmap(QtGui.QPixmap("/home/ege/Downloads/bizim_ucak.png"))
        self.bizim_ucak.setObjectName("bizim_ucak")
        self.bizim_yukseklik = QtWidgets.QLabel(Form)
        self.bizim_yukseklik.setGeometry(QtCore.QRect(310, 860, 21, 21))
        self.bizim_yukseklik.setObjectName("bizim_yukseklik")
        self.qr = QtWidgets.QLabel(Form)
        self.qr.setGeometry(QtCore.QRect(630, 410, 30, 30))
        self.qr.setText("")
        self.qr.setPixmap(QtGui.QPixmap("/home/ege/Downloads/qr.png"))
        self.qr.setObjectName("qr")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("SUFAIYER KONTROL ISTASYONU", "SUFAI YER KONTROL İSTASYONU ARAYÜZÜ "))
        self.ucak_alt.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#cc0000;\">50</span></p></body></html>"))
        self.ucak_alt_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#cc0000;\">50</span></p></body></html>"))
        self.ucak_alt_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#cc0000;\">50</span></p></body></html>"))
        self.ucak_alt_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#cc0000;\">50</span></p></body></html>"))
        self.ucak_alt_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#cc0000;\">50</span></p></body></html>"))
        self.ucak_alt_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#cc0000;\">50</span></p></body></html>"))
        self.ucak_alt_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#cc0000;\">50</span></p></body></html>"))
        self.ucak_alt_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#cc0000;\">50</span></p></body></html>"))
        self.ucak_alt_9.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#cc0000;\">50</span></p></body></html>"))
        self.ucak_alt_10.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#cc0000;\">50</span></p></body></html>"))
        self.ucak_alt_11.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#cc0000;\">50</span></p></body></html>"))
        self.ucak_alt_12.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#cc0000;\">50</span></p></body></html>"))
        self.ucak_alt_13.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#cc0000;\">50</span></p></body></html>"))
        self.ucak_alt_14.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#cc0000;\">50</span></p></body></html>"))
        self.ucak_alt_15.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#cc0000;\">50</span></p></body></html>"))
        self.bizim_yukseklik.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#3465a4;\">50</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = Ui_Form()
    win.setupUi(win)
    win.show()


    def update_label():
        global x, y, sol_ust_x, sol_ust_y, sol_alt_x, sol_alt_y, sag_ust_x, sag_ust_y, sag_alt_x, sag_alt_y, map_sol_ust_x, map_sol_ust_y, map_sol_alt_x, map_sol_alt_y, map_sag_ust_x, map_sag_ust_y, map_sag_alt_x, map_sag_alt_y
        global heading_bizim, heading1, heading2, heading3, heading4, heading5, heading6, heading7, heading8, heading9, heading10, heading11, heading12, heading13, heading14, heading15, heading16, heading17, heading18, heading19, heading20
        global en_kucuk_x, en_kucuk_y, en_kucuk_map_x, en_kucuk_map_y, en_buyuk_x, en_buyuk_y, en_buyuk_map_x, en_buyuk_map_y
        global x_vehicle, y_vehicle
        heading_bizim = vehicle.heading
        x = vehicle.location.global_frame.lat  # x_vehicle
        y = vehicle.location.global_frame.lon  # y_vehicle
        x = 41.507629
        y = 36.119118

        x_numpy = numpy.random.uniform(38.367536, 38.373399)
        y_numpy = numpy.random.uniform(27.196755, 27.20463)


        sol_ust_x = 41.515130
        sol_ust_y = 36.123122
        sol_alt_x = 41.515530
        sol_alt_y = 36.116077
        sag_ust_x = 41.504375
        sag_ust_y = 36.123110
        sag_alt_x = 41.504608
        sag_alt_y = 36.115760

        """
        sol_ust_x = 41.513700
        sol_ust_y = 36.122264
        sol_alt_x = 41.513595
        sol_alt_y = 36.117146
        sag_ust_x = 41.506903
        sag_ust_y = 36.121749
        sag_alt_x = 41.506951
        sag_alt_y = 36.116991
        
        sol_ust_x = 41.513700
        sol_ust_y = 36.122264
        sol_alt_x = 41.513595
        sol_alt_y = 36.117146
        sag_ust_x = 41.506903
        sag_ust_y = 36.121749
        sag_alt_x = 41.506951
        sag_alt_y = 36.122264
        """

        """
        sol_ust_x = 41.517757
        sol_ust_y = 36.113688
        sol_alt_x = 41.506116
        sol_alt_y = 36.113742
        sag_ust_x = 41.517444
        sag_ust_y = 36.125748
        sag_alt_x = 41.505554
        sag_alt_y = 36.126703
        
        sol_ust_x = 41.5177575
        sol_ust_y = 36.1136885
        sol_alt_x = 41.5061165
        sol_alt_y = 36.1136885
        sag_ust_x = 41.5177575
        sag_ust_y = 36.1257485
        sag_alt_x = 41.5061165
        sag_alt_y = 36.1257485

        sol_ust_x = 41.518138
        sol_ust_y = 36.113847
        sol_alt_x = 41.506489
        sol_alt_y = 36.113879
        sag_ust_x = 41.517463
        sag_ust_y = 36.125885
        sag_alt_x = 41.506175
        sag_alt_y = 36.125660
        
        map_sol_ust_x = 900
        map_sol_ust_y = 80
        map_sol_alt_x = 900
        map_sol_alt_y = 970
        map_sag_ust_x = 1600
        map_sag_ust_y = 80
        map_sag_alt_x = 1600
        map_sag_alt_y = 970
        """
        map_sol_ust_x = 280
        map_sol_ust_y = 90
        map_sol_alt_x = 280
        map_sol_alt_y = 700
        map_sag_ust_x = 1560
        map_sag_ust_y = 90
        map_sag_alt_x = 1560
        map_sag_alt_y = 700
        x_lists = [sol_ust_x, sol_alt_x, sag_ust_x, sag_alt_x]
        y_lists = [sol_ust_y, sol_alt_y, sag_ust_y, sag_alt_y]
        x_map_lists = [map_sol_ust_x, map_sol_alt_x, map_sag_ust_x, map_sag_alt_x]
        y_map_lists = [map_sol_ust_y, map_sol_alt_y, map_sag_ust_y, map_sag_alt_y]
        en_kucuk_x = sol_ust_x
        en_buyuk_x = sol_ust_x
        en_kucuk_y = sol_ust_y
        en_buyuk_y = sol_ust_y
        en_kucuk_map_x = map_sol_ust_x
        en_buyuk_map_x = map_sol_ust_x
        en_kucuk_map_y = map_sol_ust_y
        en_buyuk_map_y = map_sol_ust_x
        for i in x_lists:
            if (i < en_kucuk_x):
                en_kucuk_x = i
            if (i > en_buyuk_x):
                en_buyuk_x = i
        for i in y_lists:
            if (i < en_kucuk_y):
                en_kucuk_y = i
            if (i > en_buyuk_y):
                en_buyuk_y = i
        for i in x_map_lists:
            if (i < en_kucuk_map_x):
                en_kucuk_map_x = i
            if (i > en_buyuk_map_x):
                en_buyuk_map_x = i
        for i in y_map_lists:
            if (i < en_kucuk_map_y):
                en_kucuk_map_y = i
            if (i > en_buyuk_map_y):
                en_buyuk_map_y = i

        # SUNUCU VERİSİ ALMA YERİ EN BÜYÜK VE ÖNEMLİ
        a = b"{'sunucusaati': {'gun': 10, 'saat': 8, 'dakika': 8, 'saniye': 28, 'milisaniye': 840}, 'konumBilgileri':
            [{'takim_numarasi': 1, 'iha_enlem': 41.5105362, 'iha_boylam': 36.118885, 'iha_irtifa': 97.609,
              'iha_dikilme': 0.464, 'iha_yonelme': 39.303, 'iha_yatis': 52.894, 'iha_hizi': 22.5511627,
              'zaman_farki': -41579476},
             {'takim_numarasi': 4, 'iha_enlem': 41.085083, 'iha_boylam': 28.9982147, 'iha_irtifa': 188.578,
              'iha_dikilme': -5.14558172, 'iha_yonelme': 304.197571, 'iha_yatis': -0.0280653648, 'iha_hizi': 12.2547474,
              'zaman_farki': -51218236},
             {'takim_numarasi': 8, 'iha_enlem': 40.7130127, 'iha_boylam': 30.0283928, 'iha_irtifa': 49.858,
              'iha_dikilme': 0.0, 'iha_yonelme': -100.0, 'iha_yatis': 58.0, 'iha_hizi': 25.0, 'zaman_farki': -56813556},
             {'takim_numarasi': 9, 'iha_enlem': 43.5765457, 'iha_boylam': 22.3854218, 'iha_irtifa': 100.0,
              'iha_dikilme': 5.0, 'iha_yonelme': 256.0, 'iha_yatis': 0.0, 'iha_hizi': 223.0, 'zaman_farki': -39174667},
             {'takim_numarasi': 14, 'iha_enlem': 43.5765457, 'iha_boylam': 22.3854218, 'iha_irtifa': 100.0,
              'iha_dikilme': 5.0, 'iha_yonelme': 256.0, 'iha_yatis': 0.0, 'iha_hizi': 223.0, 'zaman_farki': -39174667},
             {'takim_numarasi': 21, 'iha_enlem': 43.5765457, 'iha_boylam': 22.3854218, 'iha_irtifa': 100.0,
              'iha_dikilme': 5.0, 'iha_yonelme': 256.0, 'iha_yatis': 0.0, 'iha_hizi': 223.0, 'zaman_farki': -39174667},
             {'takim_numarasi': 23, 'iha_enlem': 41.512, 'iha_boylam': 36.12, 'iha_irtifa': 0.0, 'iha_dikilme': 14.0,
              'iha_yonelme': 0.0, 'iha_yatis': 25.0, 'iha_hizi': 15.0, 'zaman_farki': -11548367},
             {'takim_numarasi': 24, 'iha_enlem': 40.2318, 'iha_boylam': 29.0048828, 'iha_irtifa': 40.0,
              'iha_dikilme': 5.0, 'iha_yonelme': 256.0, 'iha_yatis': 10.0, 'iha_hizi': 15.0, 'zaman_farki': -45431724}]}"
        # print(a['iha_enlem'])
        str(a,"UTF-8")
        win.pixmap2 = QtGui.QPixmap(
            "/home/ege/Downloads/bizim_ucak.png")  # BİZİM UÇAK
        win.pixmap = QtGui.QPixmap("/home/ege/Downloads/airliner_v3.png")  # RAKİP UÇAKLAR


        list_enlem = []
        list_boylam = []
        list_irtifa = []
        list_yonelme = []
        i = 0
        while i < 20:
            try:
                print(a['konumBilgileri'][i]['iha_enlem'], a['konumBilgileri'][i]['iha_boylam'])
                takim_enlem = a['konumBilgileri'][i]['iha_enlem']
                takim_boylam = a['konumBilgileri'][i]['iha_boylam']
                takim_irtifa = a['konumBilgileri'][i]['iha_irtifa']
                takim_yonelme = a['konumBilgileri'][i]['iha_yonelme']
                # takim_enlem = round(takim_enlem,3)
                # takim_boylam = round(takim_boylam,3)
                print(takim_enlem)
                print(takim_boylam)
                list_enlem.append(takim_enlem)
                list_boylam.append(takim_boylam)
                list_irtifa.append(takim_irtifa)
                list_yonelme.append(takim_yonelme)
                i += 1
            except:
                print("Takım sayısı = ", i)

                # LİSTE BİTTİ VE TEXTLERİ GÜNCELLEME
                try:
                    heading1 = list_yonelme[0]
                    pixmap_rotated1 = win.pixmap.transformed(QTransform().rotate(heading1),
                                                             QtCore.Qt.SmoothTransformation)
                    win.ucak.setPixmap(pixmap_rotated1)
                except:
                    print("birinci rakip verileri alınamadı")
                    break
                try:

                    heading2 = list_yonelme[1]
                    pixmap_rotated2 = win.pixmap.transformed(QTransform().rotate(heading2),
                                                             QtCore.Qt.SmoothTransformation)
                    win.ucak_2.setPixmap(pixmap_rotated2)
                except:
                    print("ikinci rakip verileri alınamadı")
                    break

                try:
                    heading3 = list_yonelme[2]
                    pixmap_rotated3 = win.pixmap.transformed(QTransform().rotate(heading3),
                                                             QtCore.Qt.SmoothTransformation)
                    win.ucak_3.setPixmap(pixmap_rotated3)
                except:
                    print("üçüncü takım verileri alınamadı")
                    break

                try:
                    heading4 = list_yonelme[3]
                    pixmap_rotated4 = win.pixmap.transformed(QTransform().rotate(heading4),
                                                             QtCore.Qt.SmoothTransformation)
                    win.ucak_4.setPixmap(pixmap_rotated4)
                except:
                    print("dördüncü takım verileri alınamadı")
                    break

                try:
                    heading5 = list_yonelme[4]
                    pixmap_rotated5 = win.pixmap.transformed(QTransform().rotate(heading5),
                                                             QtCore.Qt.SmoothTransformation)
                    win.ucak_5.setPixmap(pixmap_rotated5)
                except:
                    print("Beşinci takım verileri alınamadı")
                    break

                try:
                    heading6 = list_yonelme[5]
                    pixmap_rotated6 = win.pixmap.transformed(QTransform().rotate(heading6),
                                                             QtCore.Qt.SmoothTransformation)
                    win.ucak_6.setPixmap(pixmap_rotated6)
                except:
                    print("Altıncı takım verileri alınamadı")
                    break

                try:
                    heading7 = list_yonelme[6]
                    pixmap_rotated7 = win.pixmap.transformed(QTransform().rotate(heading7),
                                                             QtCore.Qt.SmoothTransformation)
                    win.ucak_7.setPixmap(pixmap_rotated7)
                except:
                    print("Yedinci takım verileri alınamadı")
                    break

                try:
                    heading8 = list_yonelme[7]
                    pixmap_rotated8 = win.pixmap.transformed(QTransform().rotate(heading8),
                                                             QtCore.Qt.SmoothTransformation)
                    win.ucak_8.setPixmap(pixmap_rotated8)
                except:
                    print("Sekizinci takım verileri alınamadı")
                    break
                try:
                    heading9 = list_yonelme[8]
                    pixmap_rotated9 = win.pixmap.transformed(QTransform().rotate(heading9),
                                                             QtCore.Qt.SmoothTransformation)
                    win.ucak_9.setPixmap(pixmap_rotated9)
                except:
                    print("dokuzuncu takım verileri alınamadı")
                    break

                try:
                    heading10 = list_yonelme[9]
                    pixmap_rotated10 = win.pixmap.transformed(QTransform().rotate(heading10),
                                                              QtCore.Qt.SmoothTransformation)
                    win.ucak_10.setPixmap(pixmap_rotated10)
                except:
                    print("Onuncu Takım verileri alınamadı")
                    break

                try:
                    heading11 = list_yonelme[10]
                    pixmap_rotated11 = win.pixmap.transformed(QTransform().rotate(heading11),
                                                              QtCore.Qt.SmoothTransformation)
                    win.ucak_11.setPixmap(pixmap_rotated11)
                except:
                    print("Onbirinci Takım verileri alınamadı")
                    break

                try:
                    heading12 = list_yonelme[11]
                    pixmap_rotated12 = win.pixmap.transformed(QTransform().rotate(heading12),
                                                              QtCore.Qt.SmoothTransformation)
                    win.ucak_12.setPixmap(pixmap_rotated12)
                except:
                    print("Onikinci Takım verileri alınamadı")
                    break

                try:
                    heading13 = list_yonelme[12]
                    pixmap_rotated13 = win.pixmap.transformed(QTransform().rotate(heading13),
                                                              QtCore.Qt.SmoothTransformation)
                    win.ucak_13setPixmap(pixmap_rotated13)
                except:
                    print("Onüçüncü Takım verileri alınamadı")
                    break

                try:
                    heading14 = list_yonelme[13]
                    pixmap_rotated14 = win.pixmap.transformed(QTransform().rotate(heading14),
                                                              QtCore.Qt.SmoothTransformation)
                    win.ucak_14.setPixmap(pixmap_rotated14)
                except:
                    print("Ondördüncü Takım verileri alınamadı")
                    break

                try:
                    heading15 = list_yonelme[14]
                    pixmap_rotated15 = win.pixmap.transformed(QTransform().rotate(heading15),
                                                              QtCore.Qt.SmoothTransformation)
                    win.ucak_15.setPixmap(pixmap_rotated15)

                except:
                    print("Onbeşinci Takım verileri alınamadı")
                    break

                try:
                    heading16 = list_yonelme[15]
                    pixmap_rotated16 = win.pixmap.transformed(QTransform().rotate(heading16),
                                                              QtCore.Qt.SmoothTransformation)
                    win.ucak_16.setPixmap(pixmap_rotated16)
                except:
                    print("Onaltıncı Takım verileri alınamadı")
                    break

                try:
                    heading17 = list_yonelme[16]
                    pixmap_rotated17 = win.pixmap.transformed(QTransform().rotate(heading17),
                                                              QtCore.Qt.SmoothTransformation)
                    win.ucak_17.setPixmap(pixmap_rotated17)
                except:
                    print("Onyedinci Takım verileri alınamadı")
                    break

                try:
                    heading18 = list_yonelme[17]
                    pixmap_rotated18 = win.pixmap.transformed(QTransform().rotate(heading18),
                                                              QtCore.Qt.SmoothTransformation)
                    win.ucak_18.setPixmap(pixmap_rotated18)
                except:
                    print("Onsekizinci Takım verileri alınamadı")
                    break

                try:
                    heading19 = list_yonelme[18]
                    pixmap_rotated19 = win.pixmap.transformed(QTransform().rotate(heading19),
                                                              QtCore.Qt.SmoothTransformation)
                    win.ucak_19.setPixmap(pixmap_rotated19)
                except:
                    print("Ondokuzuncu Takım verileri alınamadı")
                    break

                try:
                    heading20 = list_yonelme[19]
                    pixmap_rotated20 = win.pixmap.transformed(QTransform().rotate(heading20),
                                                              QtCore.Qt.SmoothTransformation)
                    win.ucak_20.setPixmap(pixmap_rotated20)
                except:
                    print("Yirminci Takım verileri alınamadı")
                    break

                i = 0
                break
        enlemler = []
        boylamlar = []
        print("RAKİP UÇAKLARIN KONUM HESAPLAMASI YAPILIYOR")

        # RAKİP UÇAKLAR KONUM HESAPLAMASI
        for i, j in zip(list_enlem, list_boylam):
            """
            x_1 = en_buyuk_x - i
            oran_x = (en_buyuk_map_x - en_kucuk_map_x) / (en_buyuk_x - en_kucuk_x)
            x_2 = x_1 * (oran_x)
            x_3 = en_buyuk_map_x - int(x_2)
            y_1 = en_buyuk_y - j
            oran_y = (en_buyuk_map_y - en_kucuk_map_y) / (en_buyuk_y - en_kucuk_y)
            y_2 = y_1 * (oran_y)
            y_3 = en_buyuk_map_y - int(y_2)
            y_3 = en_buyuk_map_y - y_3
            enlemler.append(x_3)
            boylamlar.append(y_3)"""
            y_3 = (abs((en_buyuk_map_y - en_kucuk_map_y )) * abs(en_kucuk_y - j)) / abs(en_kucuk_y-en_buyuk_y)
            y_3 = 700 - y_3
            x_3 = (abs((en_buyuk_map_x - en_kucuk_map_x )) * abs(en_kucuk_x - i)) / abs(en_kucuk_x-en_buyuk_x)
            x_3 = 1560-x_3
            #y_3 = y_3 + 8
            x_3 = x_3 - 10
            enlemler.append(x_3)
            boylamlar.append(y_3)

            """
            y_3 = (((j - en_kucuk_y) /  (en_buyuk_y-en_kucuk_y) ) * (en_buyuk_map_y- en_kucuk_map_y) ) + en_kucuk_map_y
            x_3 = (((i - en_kucuk_x) /  (en_buyuk_x-en_kucuk_x) ) * (en_buyuk_map_x- en_kucuk_map_x) ) + en_kucuk_map_x
            enlemler.append(x_3)
            boylamlar.append(y_3)"""

        # SAFDER KONUM HESAPLAMASI
        """
        x_1 = en_buyuk_x - x
        oran_x = (en_buyuk_map_y - en_kucuk_map_y) / (en_buyuk_x - en_kucuk_x)
        x_2 = x_1 * (oran_x)
        x_3 = en_kucuk_map_y + int(x_2)
        y_1 = en_buyuk_y - y
        oran_y = (en_buyuk_map_x - en_kucuk_map_x) / (en_buyuk_y - en_kucuk_y)
        y_2 = y_1 * (oran_y)
        y_3 = en_buyuk_map_x - int(y_2)
        """
        y_3 = (abs((en_buyuk_map_y - en_kucuk_map_y)) * abs(en_kucuk_y - y)) / abs(en_kucuk_y - en_buyuk_y)
        y_3 = 700 - y_3
        x_3 = (abs((en_buyuk_map_x - en_kucuk_map_x)) * abs(en_kucuk_x - x)) / abs(en_kucuk_x - en_buyuk_x)
        x_3 = 1560 - x_3
        y_3 = y_3 - 20
        x_3 = x_3 - 10

        # image for your label
        print("UÇAK ŞUAN BURADA {},{}".format(x_3, y_3))

        # ROTATELERİ HESAPLA
        pixmap_rotated_bizim = win.pixmap2.transformed(QTransform().rotate(vehicle.heading),
                                                       QtCore.Qt.SmoothTransformation)
        win.bizim_ucak.setPixmap(pixmap_rotated_bizim)
        # pixmap_rotated1 = win.pixmap.transformed(QTransform().rotate(heading1), QtCore.Qt.SmoothTransformation) #RAKİP 1 ROTATE
        """
        pixmap_rotated2 = win.pixmap.transformed(QTransform().rotate(heading2), QtCore.Qt.SmoothTransformation)
        pixmap_rotated3 = win.pixmap.transformed(QTransform().rotate(heading3), QtCore.Qt.SmoothTransformation)
        pixmap_rotated4 = win.pixmap.transformed(QTransform().rotate(heading4), QtCore.Qt.SmoothTransformation)
        pixmap_rotated6 = win.pixmap.transformed(QTransform().rotate(heading6), QtCore.Qt.SmoothTransformation)
        pixmap_rotated7 = win.pixmap.transformed(QTransform().rotate(heading7), QtCore.Qt.SmoothTransformation)
        pixmap_rotated8 = win.pixmap.transformed(QTransform().rotate(heading8), QtCore.Qt.SmoothTransformation)
        pixmap_rotated9 = win.pixmap.transformed(QTransform().rotate(heading9), QtCore.Qt.SmoothTransformation)
        pixmap_rotated10 = win.pixmap.transformed(QTransform().rotate(heading10), QtCore.Qt.SmoothTransformation)
        pixmap_rotated11 = win.pixmap.transformed(QTransform().rotate(heading11), QtCore.Qt.SmoothTransformation)
        pixmap_rotated12 = win.pixmap.transformed(QTransform().rotate(heading12), QtCore.Qt.SmoothTransformation)
        pixmap_rotated13 = win.pixmap.transformed(QTransform().rotate(heading13), QtCore.Qt.SmoothTransformation)
        pixmap_rotated14 = win.pixmap.transformed(QTransform().rotate(heading14), QtCore.Qt.SmoothTransformation)
        pixmap_rotated15 = win.pixmap.transformed(QTransform().rotate(heading15), QtCore.Qt.SmoothTransformation)
        pixmap_rotated16 = win.pixmap.transformed(QTransform().rotate(heading16), QtCore.Qt.SmoothTransformation)
        pixmap_rotated17 = win.pixmap.transformed(QTransform().rotate(heading17), QtCore.Qt.SmoothTransformation)
        pixmap_rotated18 = win.pixmap.transformed(QTransform().rotate(heading18), QtCore.Qt.SmoothTransformation)
        pixmap_rotated19 = win.pixmap.transformed(QTransform().rotate(heading19), QtCore.Qt.SmoothTransformation)
        pixmap_rotated20 = win.pixmap.transformed(QTransform().rotate(heading20), QtCore.Qt.SmoothTransformation)
        """

        # KONUM UPDATELE

        try:
            win.ucak.setGeometry(QtCore.QRect(enlemler[0], boylamlar[0], 30, 30))
            win.ucak_alt.setGeometry(QtCore.QRect(enlemler[0] + 20, boylamlar[0] + 20, 30, 30))
            win.ucak_alt.setText(str(list_irtifa[0]))
        except:
            print("birinci uçak haritada görselleştirilemedi")
        try:
            win.ucak_2.setGeometry(QtCore.QRect(enlemler[1], boylamlar[1], 30, 30))
            win.ucak_alt_2.setGeometry(QtCore.QRect(enlemler[1] + 20, boylamlar[1] + 20, 30, 30))
            win.ucak_alt2.setText(str(list_irtifa[1]))
        except:
            print("ikinci uçak haritada görselleştirilemedi")

        try:
            win.ucak_3.setGeometry(QtCore.QRect(enlemler[2], boylamlar[2], 30, 30))
            win.ucak_alt_3.setGeometry(QtCore.QRect(enlemler[2] + 20, boylamlar[2] + 20, 30, 30))
            win.ucak_alt_3.setText(str(list_irtifa[2]))
        except:
            print("üçüncü uçak haritada görselleştirilemedi")

        try:
            win.ucak_4.setGeometry(QtCore.QRect(enlemler[3], boylamlar[3], 30, 30))
            win.ucak_alt_4.setGeometry(QtCore.QRect(enlemler[3] + 20, boylamlar[3] + 20, 30, 30))
            win.ucak_alt_4.setText(str(list_irtifa[3]))
        except:
            print("dördüncü uçak haritada görselleştirilemedi")

        try:
            win.ucak_5.setGeometry(QtCore.QRect(enlemler[4], boylamlar[4], 30, 30))
            win.ucak_alt_5.setGeometry(QtCore.QRect(enlemler[4] + 20, boylamlar[4] + 20, 30, 30))
            win.ucak_alt_5.setText(str(list_irtifa[4]))
        except:
            print("beşinci uçak haritada görselleştirilemedi")

        try:
            win.ucak_6.setGeometry(QtCore.QRect(enlemler[5], boylamlar[5], 30, 30))
            win.ucak_alt_6.setGeometry(QtCore.QRect(enlemler[5] + 20, boylamlar[5] + 20, 30, 30))
            win.ucak_alt_6.setText(str(list_irtifa[5]))
        except:
            print("altıncı uçak haritada görselleştirilemedi")

        try:
            win.ucak_7.setGeometry(QtCore.QRect(enlemler[6], boylamlar[6], 30, 30))
            win.ucak_alt_7.setGeometry(QtCore.QRect(enlemler[6] + 20, boylamlar[6] + 20, 30, 30))
            win.ucak_alt_7.setText(str(list_irtifa[6]))
        except:
            print("yedinci uçak haritada görselleştirilemedi")

        try:
            win.ucak_8.setGeometry(QtCore.QRect(enlemler[7], boylamlar[7], 30, 30))
            win.ucak_alt_8.setGeometry(QtCore.QRect(enlemler[7] + 20, boylamlar[7] + 20, 30, 30))
            win.ucak_alt_8.setText(str(list_irtifa[7]))
        except:
            print(" sekizinci uçak haritada görselleştirilemedi")

        try:
            win.ucak_9.setGeometry(QtCore.QRect(enlemler[8], boylamlar[8], 30, 30))
            win.ucak_alt_9.setGeometry(QtCore.QRect(enlemler[8] + 20, boylamlar[8] + 20, 30, 30))
            win.ucak_alt_9.setText(str(list_irtifa[8]))
        except:
            print("dokuzuncu uçak haritada görselleştirilemedi")

        try:
            win.ucak_10.setGeometry(QtCore.QRect(enlemler[9], boylamlar[9], 30, 30))
            win.ucak_alt_10.setGeometry(QtCore.QRect(enlemler[9] + 20, boylamlar[9] + 20, 30, 30))
            win.ucak_alt_10.setText(str(list_irtifa[9]))
        except:
            print("onuncu uçak haritada görselleştirilemedi")

        try:
            win.ucak_11.setGeometry(QtCore.QRect(enlemler[10], boylamlar[10], 30, 30))
            win.ucak_alt_11.setGeometry(QtCore.QRect(enlemler[10] + 20, boylamlar[10] + 20, 30, 30))
            win.ucak_alt_11.setText(str(list_irtifa[10]))
        except:
            print("onbirinci uçak haritada görselleştirilemedi")

        try:
            win.ucak_12.setGeometry(QtCore.QRect(enlemler[11], boylamlar[11], 30, 30))
            win.ucak_alt_12.setGeometry(QtCore.QRect(enlemler[11] + 20, boylamlar[11] + 20, 30, 30))
            win.ucak_alt_12.setText(str(list_irtifa[11]))
        except:
            print("onikinci uçak haritada görselleştirilemedi")

        try:
            win.ucak_13.setGeometry(QtCore.QRect(enlemler[12], boylamlar[12], 30, 30))
            win.ucak_alt_13.setGeometry(QtCore.QRect(enlemler[12] + 20, boylamlar[12] + 20, 30, 30))
            win.ucak_alt_13.setText(str(list_irtifa[12]))
        except:
            print("onüçüncü uçak haritada görselleştirilemedi")

        win.bizim_ucak.setGeometry(QtCore.QRect(x_3, y_3, 40, 40))
        win.bizim_yukseklik.setGeometry(QtCore.QRect(x_3+ 30, y_3 + 30, 30, 30))
        win.bizim_yukseklik.setText(str(vehicle.location.global_relative_frame.alt))
        win.bizim_ucak.setPixmap(pixmap_rotated_bizim)

        #win.label_130.setGeometry(QtCore.QRect(1270, 420, 21, 21))  # QR COORDİNATES
        print("enlemler", enlemler)
        print("boylamlar", boylamlar)
        list_enlem.clear()
        list_boylam.clear()
        list_irtifa.clear()
        list_yonelme.clear()
        enlemler.clear()
        boylamlar.clear()
        """
        # SAFDER SETTEXLERİ
        win.label_14.setText(("Lat:" + str(vehicle.location.global_frame.lat)))
        win.label_15.setText(("Lon:" + str(vehicle.location.global_frame.lon)))  # vehicle.location.global_frame.lon
        win.label_16.setText(str(vehicle.location.global_relative_frame.alt))
        win.label_13.setText(str(vehicle.groundspeed))
        win.label_12.setText(str(vehicle.mode))
        win.label_24.setText(str(x))  # Safder konumun yanı
        win.label_62.setText(str(y))
        win.label_79.setText(str(vehicle.location.global_relative_frame.alt))  # 1
        win.label_49.setText(str(vehicle.attitude.pitch))
        win.label_50.setText(str(vehicle.attitude.yaw))
        win.label_51.setText(str(vehicle.attitude.roll))
        win.label_52.setText(str(vehicle.battery.voltage))

        """
        """
        win.label_26.setText((("Lat:" + str(x_rand2) + "-" + "Lon: " + str(y_rand2))))
        win.label_27.setText((("Lat:" + str(x_rand3) + "-" + "Lon:" + str(y_rand3))))
        win.label_25.setText((("Lat:" + str(x_rand4) + "-" + "Lon:" + str(y_rand4))))
        win.label_24.setText((("Lat:" + str(x_rand5) + "-" + "Lon:" + str(y_rand5)))) 
        """
    timer = QtCore.QTimer()
    timer.timeout.connect(update_label)
    timer.start(1000)  # every 10,000 millisecond
    sys.exit(app.exec())
