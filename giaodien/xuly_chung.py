from PyQt5.QtWidgets import QApplication,QMainWindow
from xuly_dangky import MainDK
from xuly_dangkyload import MainDK_load
from xuly_dangnhap import MainDN
from xuly_main import Main
from xuly_giaodienchinh import Main_chinh
import hamchupanh,hamtrain,hamnhandien
import time
import MyVirtualAssistant
a = []
class UI():
    # chuyen slide index -> dang  ky
    def getuiDangky(self):
        self.mainUI.hide()
        self.dkUI.show()
    # chuyen slide index -> dang  nhap
    def getuiDangnhap(self):
        global a
        self.mainUI.hide()
        self.dnUI.show()
        a = hamnhandien.nhandien()
        time.sleep(5)
        self.dnUI.hide()
        self.main_chinhUI.show()
    # chuyen slide dang ky -> index
    def getuiindex(self):
        self.dkUI.hide()
        self.mainUI.show()
    # xu ly dang ky chup anh va train -> cho dang ky -> giao dien chinh
    def xulydangky(self):
        self.dkUI.hide()
        self.dkUI_load.show()
        ten = self.main_Dangky.input_name.toPlainText()
        hamchupanh.chupanh(ten)
        hamtrain.train()
        time.sleep(5)
        self.dkUI_load.hide()
        self.main_chinhUI.show()
    # bat dau chuong trinh 
    def batdau(self):
        global a
        MyVirtualAssistant.ai(a)
        app = QApplication([])
        app.closeAllWindows()
    def __init__(self):
        # xu ly giao dien index
        self.mainUI = QMainWindow()
        self.main_index = Main(self.mainUI)
        self.mainUI.show()
        # di den giao dien dang ky
        self.main_index.ptn_nhandien_dangky.clicked.connect(lambda: self.getuiDangky())
        #di den giao dien dang nhap
        self.main_index.ptn_nhandien_dangnhap.clicked.connect(lambda: self.getuiDangnhap())


 

        # xu ly giao dien dang ky 
        self.dkUI = QMainWindow()
        self.main_Dangky = MainDK(self.dkUI)

        self.dkUI_load = QMainWindow()
        self.main_Dangky_load = MainDK_load(self.dkUI_load)
        # di den giao dien chinh - giao dien bot ao
        self.main_Dangky.ptn_dangky.clicked.connect(lambda: self.xulydangky())
        # tro ve giao dien index
        self.main_Dangky.ptn_pre.clicked.connect(lambda: self.getuiindex())
        
        # xu ly giao dien dang nhap
        self.dnUI = QMainWindow()
        self.main_Dangnhap = MainDN(self.dnUI)


        # xu ly giao dien chinh
        self.main_chinhUI = QMainWindow()
        self.main_chinh = Main_chinh(self.main_chinhUI)
        self.main_chinh.pushButton.clicked.connect(lambda: self.batdau())

        
if __name__ =="__main__":
    app = QApplication([])
    ui = UI()
    app.exec_()