from core.Ping import Ping

# if __name__ == '__main__':
#     print('start batch ping...')
#
#     fin = open('ip.txt')
#
#     for ip in fin:
#         Ping(ip.strip()).test_ping()
#
#     fin.close()
#     pass


import sys

from PyQt5.QtWidgets import QApplication
from ui.forms.MainForm import MainForm

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainForm()
    widget.show()
    sys.exit(app.exec_())
    pass
