from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
import platform

debug = False
if int(platform.version().split(".")[0]) > 7:
    debug = True


class Status(QtWidgets.QWidget):
    def __init__(self, text):
        super(Status, self).__init__()
        self.layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.layout)
        self.label = QtWidgets.QLabel(text + ": ")
        self.label.setMinimumWidth(80)
        self.layout.addWidget(self.label)
        self.value = QtWidgets.QLabel()
        self.setStyleSheet(
            """
            QLabel{
                qproperty-alignment: AlignCenter;
                font-size: 22px;
                font-family: \"Microsoft Yahei\";
                color: white;
            }
        """
        )
        self.value.setMinimumWidth(150)
        # self.value.setDisabled(True)
        self.layout.addWidget(self.value)

    def set_val(self, val):
        self.value.setText(str(val))


import subprocess

import pdb


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.widget = QtWidgets.QWidget()
        self.setWindowTitle("系统保护")

        self.palette = self.widget.palette()
        self.palette.setColor(self.widget.backgroundRole(), QtGui.QColor("black"))
        self.palette.setColor(self.widget.foregroundRole(), QtGui.QColor("white"))
        self.widget.setPalette(self.palette)
        self.widget.setAutoFillBackground(True)
        layout = QtWidgets.QVBoxLayout()
        self.current = Status("当前系统保护状态")
        # self.next = Status("重启后的系统保护状态")
        layout.addWidget(self.current)
        # layout.addWidget(self.next)
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)
        self.status = None
        self.set_status()
        self.button = QtWidgets.QPushButton()

        self.button.setStyleSheet(
        """
        QPushButton{
            font-size: 22px;
            font-family: \"Microsoft Yahei\";
        }
        
        """
        )
        layout.addWidget(self.button)
        if self.status:
            self.button.setText("关闭保护")
        else:
            self.button.setText("开启保护")
        self.button.clicked.connect(self.switch)

    def set_status(self):
        if debug:
            out = """
            filter state: enabled.
            """
        else:
            p = subprocess.run(["fbwfmgr", "/displayconfig"], capture_output=True)
            out = p.stdout.decode("gbk")
        print(out)
        for line in out.split("\n"):
            if line.strip().startswith("filter state"):
                status = line.strip().split(":")[1][1:-1]
                if status == "disabled":
                    self.status = False
                    self.current.set_val("未保护")
                    self.palette.setColor(
                        self.widget.backgroundRole(), QtGui.QColor("red")
                    )
                    self.widget.setPalette(self.palette)
                elif status == "enabled":
                    self.status = True
                    self.current.set_val("保护中")
                    self.palette.setColor(
                        self.widget.backgroundRole(), QtGui.QColor("green")
                    )
                    self.widget.setPalette(self.palette)
                else:
                    pdb.set_trace()
                    self.current.set_val(out)
                break

    def switch(self):
        if self.status:
            subprocess.call("关闭保护.bat")
        else:
            subprocess.call("开启保护.bat")


if __name__ == "__main__":
    import ctypes, sys

    def is_admin():
        if debug:
            return True
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    if is_admin():
        app = QtWidgets.QApplication(sys.argv)
        window = MainWindow()
        window.show()
        app.exec()

    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
