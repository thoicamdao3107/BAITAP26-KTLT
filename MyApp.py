import sys
from PyQt6.QtWidgets import QApplication
from baitap25Ext import SymmetricChecker

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = SymmetricChecker()
    main_window.show()
    sys.exit(app.exec())
