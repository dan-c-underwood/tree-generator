import sys
import argparse

from PyQt4.QtGui import QApplication, QMainWindow

from ui_mainwindow import Ui_MainWindow
from tree_gen import generate


def _start_gui():
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    window.show()

    sys.exit(app.exec_())

def _start_cli(settings_file, random):
    generate(settings_file, random)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generator for 3D Tree models')
    parser.add_argument('-c','--cli', dest='cli', action='store_true', help='Runs program through the command line')
    parser.add_argument('-s','--settings', type=str, dest='settings_file', default='default.ini', action='store', nargs=1, help="Specify a preferences file for the CLI")
    parser.add_argument('-r','--random', dest='random', action='store_true')

    args = parser.parse_args()

    if args.cli:
        _start_cli(open(args.settings_file, 'r'), args.random)
    else:
        _start_gui()
