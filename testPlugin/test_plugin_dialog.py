# -*- coding: utf-8 -*-
"""
/***************************************************************************
 testPluginDialog
                                 A QGIS plugin
 testing plugin
                             -------------------
        begin                : 2014-07-05
        git sha              : $Format:%H$
        copyright            : (C) 2014 by private
        email                : testing@adasd.cosaf
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import testPlugin_gui




class testPluginDialog(QDialog,testPlugin_gui.Ui_Dialog):
    def __init__(self, parent=None):
        """Constructor."""
        super(testPluginDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect


        self.setupUi(self)

        # connect comboBox
        #QObject.connect(self.dlg.ui.KeterdampakanComboBox,SIGNAL('currentIndexChanged(int)'), self.bacaKeterdampakan)

        # connect browse button
        self.connect(self.browseButton, SIGNAL("clicked()"),self.browseOutfile)


    def browseOutfile(self):
        outName = QFileDialog.getSaveFileName(self, "Output Shapefile",self.lineInput.displayText(), "Shapefile (*.shp)")
        if outName != None:
           self.lineInput.setText(outName)



