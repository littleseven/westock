from PySide2 import QtCore, QtWidgets

import os

# from PySide2.QtCore import QFile
# from PySide2.QtUiTools import QUiLoader

from app.gui.LoadDataFilesUI import LoadDataFileUI


class LoadDataFiles(QtCore.QObject):

    def __init__(self, controller, parent=None):

        super(LoadDataFiles, self).__init__()

        self.current_dir_path = os.path.dirname(os.path.realpath(__file__))
        self.controller = controller

        self.parent = parent
        self.view = view = LoadDataFileUI()
        view.setController(controller)
        pass

    '''
    def showEvent(self, ev):
        # Move at the center of the window
        #if self.parent is not None:

        #    x = int(self.parent.sizeHint().width() / 2 - self.sizeHint().width())
        #    y = int(self.parent.sizeHint().height() / 2 - self.sizeHint().height()) 
        
        #    self.move( x, y )

        return QtWidgets.showEvent(self, ev)
    '''
