#створи тут фоторедактор Easy Editor!
from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog, 
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)

app = QApplication([])
win = QWidget()       
win.resize(700, 500) 
win.setWindowTitle('Easy Editor')
lb_image = QLabel("Картинка")
btn_dir = QPushButton("Папка")
lw_files = QListWidget()