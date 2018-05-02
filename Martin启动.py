import sys, os
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QPalette, QIcon, QBrush, QPixmap, QColor


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        kuan = 200
        path = '/home/martin/桌面/code/fast_open/'
        btn1 = QPushButton("开启ssr", self)
        btn1.move(kuan, 50)
        btn1.setIcon(QIcon(path + '葡萄.png'))
        btn2 = QPushButton("关闭ssr", self)
        btn2.setIcon(QIcon(path + '樱桃.png'))
        btn2.move(kuan, 100)

        btn3 = QPushButton("pycharm", self)
        btn3.setIcon(QIcon(path + '菠萝.png'))
        btn3.move(kuan, 150)

        btn4 = QPushButton("退出", self)
        btn4.setIcon(QIcon(path + '火龙果.png'))
        btn4.move(kuan, 250)

        btn5 = QPushButton("网易云音乐", self)
        btn5.setIcon(QIcon(path + '石榴.png'))
        btn5.move(kuan, 200)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked1)
        btn3.clicked.connect(self.buttonPyCharm)
        btn4.clicked.connect(QCoreApplication.instance().quit)
        btn5.clicked.connect(self.buttonMusic)
        self.statusBar()

        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Martin')
        self.setIcon()
        self.show()

    def buttonClicked(self):
        # sender = self.sender()
        order = 'sslocal -c /home/martin/ssr.json'
        os.popen(order)
        text = "启动ssr成功！"
        self.statusBar().showMessage(text)

    def buttonClicked1(self):
        order = 'killall sslocal'
        os.popen(order)
        text = "关闭ssr成功！"
        self.statusBar().showMessage(text)

    def buttonPyCharm(self):
        order = 'sh /home/martin/桌面/pycharm-2018.1.2/bin/pycharm.sh'
        os.popen(order)
        text = "启动pycharm成功！"
        self.statusBar().showMessage(text)

    def buttonMusic(self):
        order = 'sh /home/martin/shell/cloudmusic.sh'
        os.popen(order)
        text = '网易云音乐'
        self.statusBar().showMessage(text)

    def setIcon(self):
        path = '/home/martin/桌面/code/fast_open/'
        palette1 = QPalette()
        # palette1.setColor(self.backgroundRole(), QColor(192,253,123))   # 设置背景颜色
        palette1.setBrush(self.backgroundRole(), QBrush(QPixmap(path + 'b.png')))  # 设置背景图片
        self.setPalette(palette1)
        self.setWindowIcon(QIcon(path + '青柠.png'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
