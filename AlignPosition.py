import sys
import argparse
from PySide6 import QtWidgets

from Window.loadingWindow import GifAnimationDialog


def main(background):

    # Create the application instance
    app = QtWidgets.QApplication(sys.argv)
    w = GifAnimationDialog()
    w.setScreen(app.primaryScreen())
    w.check_background(background)
    app.exec()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Enhanced Parental Control and Posture Monitoring Application")
    parser.add_argument("--background", action="store_true", help="Run the application in the background")

    args = parser.parse_args()
    main(args.background)
