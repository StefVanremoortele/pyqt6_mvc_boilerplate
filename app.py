from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPalette

import sys
import os
import logging
import logging.config
import yaml

from controllers.controller import Controller
from models.model import Model
from views.view import View
from colors.colors import *

def setup_logging(
    default_path='resources/logger_config.yaml',
    default_level=logging.DEBUG,
    env_key='LOG_CFG'
):
    """
    Setup logging configuration
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


class App(QApplication):
    """
    The application
    """
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = Model()
        self.controller = Controller(self.model)
        self.view = View(self.model, self.controller)

        self.view.show()
        self.view.showFullScreen()
        self.view.setWindowTitle("App")
        print("Done")


def setTheme(app):
    """
    Setup app theme
    """
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.setStyle('Fusion')
    palette = QPalette()
    palette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, COLOR_LIGHT_SHADE)
    palette.setColor(QPalette.ColorRole.WindowText, COLOR_BLACK_TEXT)
    palette.setColor(QPalette.ColorRole.Base, COLOR_BLUE)
    palette.setColor(QPalette.ColorRole.AlternateBase, COLOR_LIGHT_GREY)
    palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Button, COLOR_LIGHT_GREY)
    palette.setColor(QPalette.ColorRole.ButtonText, COLOR_BLACK_TEXT)
    palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
    palette.setColor(QPalette.ColorRole.Highlight, COLOR_GRAY.lighter())
    palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)
    app.setPalette(palette)


if __name__ == '__main__':
    setup_logging()
    logger = logging.getLogger(__name__)
    app = App(sys.argv)
    setTheme(app)
    sys.exit(app.exec())
