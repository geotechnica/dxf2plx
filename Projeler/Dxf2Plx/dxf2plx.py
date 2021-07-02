from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Dxf to Plaxis 2D")
        Form.resize(500, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 80, 213, 32))
        self.pushButton.setStyleSheet("background-color:blue;\n"
                                      "color: white;\n"
                                      "border-style: outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius:10px;\n"
                                      "border-color:black;\n"
                                      "font:bold 14px;\n"
                                      "padding :6px;\n"
                                      "min-width:10px;\n"
                                      "\n"
                                      "\n"
                                      "")
        self.pushButton.setObjectName("pushButton")

        self.pushButton1 = QtWidgets.QPushButton(Form)
        self.pushButton1.setGeometry(QtCore.QRect(150, 200, 213, 32))
        self.pushButton1.setStyleSheet("background-color:blue;\n"
                                      "color: white;\n"
                                      "border-style: outset;\n"
                                      "border-width:2px;\n"
                                      "border-radius:10px;\n"
                                      "border-color:black;\n"
                                      "font:bold 14px;\n"
                                      "padding :6px;\n"
                                      "min-width:10px;\n"
                                      "\n"
                                      "\n"
                                      "")
        self.pushButton1.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Dxf to Plaxis 2D"))
        self.pushButton.setText(_translate("Form", "Dxf Oku"))
        self.pushButton.clicked.connect(self.pushButton_handler)

        self.pushButton1.setText(_translate("Form", "Txt Dosyasını Yaz"))
        self.pushButton1.clicked.connect(self.pushButton1_handler)

    def pushButton_handler(self):
        print("Button pressed")
        self.open_dialog_box()

    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName(None, "name", "", "Dxf (*.dxf)")
        self.path = filename[0]
        print(self.path)

    def pushButton1_handler(self):
        savename = QtWidgets.QFileDialog.getSaveFileName(None, "name", "", "Text files (*.txt)")
        print("Button1 pressed")
        self.path1 = savename[0]
        self.oku()

    def oku(self):

        import ezdxf
        doc = ezdxf.readfile(self.path)
        msp = doc.modelspace()

        doc1 = ezdxf.new('R2007',setup=True)
        msp1 = doc1.modelspace()

        poly = msp.query('LWPOLYLINE')
        for i in range(0,poly.__len__()):

            polylines = msp.query('LWPOLYLINE')[i]
            t=open(self.path1, "a")
            t.write("line")
            t.close()
            for polyline in polylines:
                listex=list()
                listey=list()
                a=polylines.__len__()
                sayac = 0

                for i in range(0,a):
                    pl = (polylines.__getitem__(i))
                    listex.append(round(pl[0],2))
                    listey.append(round(pl[1],2))
            pl0=list(zip(listex,listey))
            print(len(pl0))

            for c in pl0:
                sayac = sayac+1
                print(sayac)
                if sayac == len(pl0):
                    with open(self.path1, "a") as text_file:
                        print(" ({} {})\n".format(c[0],c[1]),file=text_file)
                else:
                    with open(self.path1, "a") as text_file:
                        text_file.write(" ({} {})".format(c[0],c[1]))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())