from PySide6.QtWidgets import QApplication, QMainWindow
from main_ui import Ui_MainWindow
import sys

class MusicPlayer(QMainWindow):
    def __init__(self):
        super(MusicPlayer, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MusicPlayer()
    window.show()
    
    sys.exit(app.exec())