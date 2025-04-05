import sys
sys.path.append("..")
from time import sleep
from PIL import ImageGrab
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QDesktopWidget, QLabel, QPushButton,QVBoxLayout, QWidget, QHBoxLayout
from PyQt5.QtGui import QPainter, QPen, QColor, QFont
from PyQt5.QtCore import Qt, QPoint, QRect
from SDGUI.startdetect import StartDetect

class StartWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.font = QFont()
        self.font.setFamily("Microsoft YaHei")
        self.font.setBold(True)

        self.setGeometry(0, 35, 880, 660)
        self.setWindowTitle('Start Window')


        self.background = QLabel(self)

        self.background.setGeometry(0, 0, 400, 400)

        layout = QVBoxLayout()
        self.label = QLabel('Dangerous Item Auto Detection', self)

        self.label.setStyleSheet(
            'font: 48px "Microsoft JhengHei"; color: black;font-weight: bold;')
        self.label.setGeometry(0, 0, self.width(), self.height())
        self.label.setAlignment(Qt.AlignCenter)

        self.Startbutton = QPushButton("Select Detection Area",self)
        self.Startbutton.setFont(self.font)

        self.Startbutton.setFixedSize(300, 80)
        self.Startbutton.setStyleSheet(
            "QPushButton {"
            "background-color: #2e6b2e;"
            "border: 5px soild #90EE90;"
            "border-radius: 25px;"
            "color:white;"
            "font-size: 24px;"
            "font-weight: bold;"
            "padding: 8px 8px;"
            "text-align: center;"
            "}"
            "QPushButton:hover {"
            "background-color: green;"
            "}"
            "QPushButton:pressed {"
            "background-color: #2e6b2e;"
            "border: 2px solid #2e6b2e;"
            "}"
        )

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.label)
        vlayout.addWidget(self.Startbutton)

        self.label.setAlignment(Qt.AlignHCenter)

        hlayout = QHBoxLayout()
        hlayout.addStretch()
        hlayout.addLayout(vlayout)
        hlayout.addStretch()

        hlayout.setAlignment(Qt.AlignCenter)
        vlayout.setAlignment(Qt.AlignCenter)

        self.setLayout(hlayout)

        self.Startbutton.clicked.connect(self.open_new_window)

    def open_new_window(self):

        self.hide()
        sleep(1)
        CurrentImage = ImageGrab.grab()  # 获得当前屏幕
        CurrentImage.save("ScreenShot.jpg")
        selectwindow.setStyleSheet(
            'background-image: url(ScreenShot.jpg); background-repeat: no-repeat; background-position: center;}')
        selectwindow.show()

    def open_start_detect_window(self, x1, y1, x2, y2):
        self.start_detect_window = StartDetect(x1, y1, x2, y2)
        self.start_detect_window.show()
        self.hide()

class FrameRange(QMainWindow):
    def __init__(self, start_window):
        super().__init__()
        self.start_window = start_window
        self.title = 'Dangerous Item Automatically Detection'
        self.left = 10
        self.top = 10
        self.width = screen_w
        self.height = screen_h
        self.begin = QPoint()
        self.end = QPoint()
        self.image_path = 'ScreenShot.jpg'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        # self.setStyleSheet('background-image: url(ScreenShot.jpg); background-repeat: no-repeat; background-position: center;')
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.center()
        # self.toolbar = self.addToolBar('Tools')
        self.background = QLabel(self)
        # self.background.setPixmap(QPixmap('ScreenShot.jpg'))
        # self.background.setGeometry(0, 0, self.background.pixmap().width(), self.background.pixmap().height())
        self.save_action = QAction('Save', self)
        self.save_action.setShortcut('Ctrl+S')
        self.save_action.triggered.connect(self.confirm)
        # confirmbutton
        self.Confirmbutton = QPushButton(self)
        self.Confirmbutton.move(0,0)
        self.Confirmbutton.setFixedSize(150, 80)
        self.Confirmbutton.clicked.connect(self.confirm)
        self.Confirmbutton.setStyleSheet("""
                          QPushButton {
                              background-image: url(Confirm.svg);
                              color: green;
                              border-style: solid;
                          }
                          QPushButton:hover {
                              background-image: url(Confirm.svg);
                              border-color: green;
                          }
                      """)
        #exitbutton
        self.Exitbutton=QPushButton(self)
        self.Exitbutton.move(150,0)
        self.Exitbutton.setFixedSize(150, 80)
        self.Exitbutton.clicked.connect(self.Exit)
        self.Exitbutton.setStyleSheet("""
                    QPushButton {
                        background-image: url(Exit.svg);
                        color: white;
                        border-style: solid;
                    }
                    QPushButton:hover {
                         background-image: url(Exit.svg);
                         border-color: red;
                    }
                """)
        self.show()
    def center(self):
        frame_geometry = self.frameGeometry()
        center_position = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center_position)
        self.move(frame_geometry.topLeft())

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        # painter.setWindowFlags(Qt.WindowStaysOnTopHint)
        painter.setPen(QPen(QColor(61, 145, 64, 200), 5, Qt.DotLine))
        painter.setBrush(QColor(61, 145, 64, 0))
        painter.drawRect(QRect(self.begin, self.end))
        self.Confirmbutton.move(self.begin.x(),self.end.y())
        self.Exitbutton.move(self.begin.x()-90,self.end.y())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.begin = event.pos()
            self.end = self.begin
            self.update()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.end = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.end = event.pos()
            self.update()

    def confirm(self):
        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())
        print(f"Selected Range: ({x1}, {y1}), ({x2}, {y2})")
        self.close()
        self.start_window.open_start_detect_window(x1, y1, x2, y2)

    def Exit(self):
        self.close()
if __name__ == '__main__':
    p = ImageGrab.grab()
    screen_w, screen_h = p.size
    app = QApplication(sys.argv)
    startwindow = StartWindow()
    startwindow.show()
    selectwindow = FrameRange(startwindow)
    selectwindow.hide()
    sys.exit(app.exec_())