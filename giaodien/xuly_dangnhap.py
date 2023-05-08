
from dangnhap import Ui_MainWindow
import hamnhandien

class MainDN(Ui_MainWindow):
    # function 
    def xulydangnhap(self):
        hamnhandien.nhandien()
    # function  main 
    def __init__(self,mainwindow)->None:
        self.setupUi(mainwindow)
        
        # =======================================
        

