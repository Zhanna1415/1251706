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

right_btn  = QPushButton("Вправо")
left_btn = QPushButton("Вліво")
sharp_btn  = QPushButton("Різкість")
flip_btn  = QPushButton("Дзеркало")
bw_btn  = QPushButton("Ч/Б")

row = QHBoxLayout()         
col1 = QVBoxLayout()         
col2 = QVBoxLayout()
col1.addWidget(btn_dir)      
col1.addWidget(lw_files)     
col2.addWidget(lb_image, 95) 
row_tools = QHBoxLayout()    
row_tools.addWidget(left_btn)
row_tools.addWidget(right_btn)
row_tools.addWidget(flip_btn)
row_tools.addWidget(bw_btn)
row_tools.addWidget(sharp_btn)
col2.addLayout(row_tools)

row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)

win.show()
app.exec(),
