"""
Tree Generator

This script produces simple 3D models of trees based on a set of parameters declared in a .ini file. The algorithm used
is recursive and based on the one put forward by Peter E. Oppenheimer in his 1986 paper: "Real Time Design and Animation
of Fractal Plants and Trees".

A simple recursive algorithm was used as opposed to an L-System. This was because the tool is used for outreach by the
University of Manchester (School of Computer Science) to demonstrate the concept of recursion. The script was also
designed to be easily explainable and modifiable by school children so simplicity was the design goal.

Dependencies:
numpy
PyQt4
"""
import sys
import argparse
import doctest

from PyQt4.QtGui import QApplication, QMainWindow

from ui_mainwindow import Ui_MainWindow
from tree_gen import generate



# Initialise the GUI version
def _start_gui():
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    window.show()

    sys.exit(app.exec_())


# Initialise the Command Line version
def _start_cli(design_file, random):
    generate(design_file, random)

# Main definition
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generator for 3D Tree models')
    parser.add_argument('-c', '--cli', dest='cli', action='store_true', help='Runs program through the command line')
    parser.add_argument('-d', '--design', type=str, dest='design_file', default='designs/default.ini', action='store',
                        nargs=1, help="Specify a preferences design file for the CLI (.ini)")
    parser.add_argument('-r', '--random', dest='random', action='store_true')
    parser.add_argument('-t', '--test', dest='test', action = 'store_true', help='Runs doctests in USAGE.md.')

    args = parser.parse_args()
    if args.test:
        doctest.testfile('USAGE.md')

    if args.cli:
        _start_cli(open(args.design_file, 'r'), args.random)
    else:
        _start_gui()
