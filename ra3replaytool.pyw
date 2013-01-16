# !/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PyQt4.QtGui import *
from PyQt4 import QtCore

from rep import decoder
from rep import filter
import path

import ui_main
import res_rc

class Ra3ReplayToolWindow(QMainWindow):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        
        self.faction1 = None
        self.faction2 = None
        self.allReps = []
        
        self.ui = ui_main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.loadReps()
        print self.ui.lwReplays.currentRow()
        self.show()
        
    def loadReps(self):        
        for file in path.getReplayFiles():
            self.allReps.append(decoder.decodeFile(file))
        self.showReps(self.allReps)

    def showReps(self, reps):
        tmpListItems = []
        self.ui.lwReplays.clear()
        for rep in reps:
            icon = QIcon(':res/images/' + rep['map']['image'])
            qstinglistmodel = QStringListModel([rep['name'],rep['filename']])
            listItem = QListWidgetItem(icon, rep['name'], self.ui.lwReplays)

    @QtCore.pyqtSlot()
    def on_lwReplays_itemDoubleClicked(self, item):
        print 'good'
        self.hide()
        
    @QtCore.pyqtSlot()
    def on_rbSoviet1_clicked(self):
        self.faction1 = 'Soviet';
        self.filterByFactions();
        print 'good'
        
    @QtCore.pyqtSlot()
    def on_rbSoviet2_clicked(self):
        self.faction2 = 'Soviet';
        self.filterByFactions();
    
    @QtCore.pyqtSlot()
    def on_rbAllied1_clicked(self):
        self.faction1 = 'Allied';
        self.filterByFactions();
        
    @QtCore.pyqtSlot()
    def on_rbAllied2_clicked(self):
        self.faction2 = 'Allied';
        self.filterByFactions();
        
    @QtCore.pyqtSlot()
    def on_rbEmpire1_clicked(self):
        self.faction1 = 'Empire';
        self.filterByFactions();
        
    @QtCore.pyqtSlot()
    def on_rbEmpire2_clicked(self):
        self.faction2 = 'Empire';
        self.filterByFactions();
        
    @QtCore.pyqtSlot()    
    def on_rbRandom1_clicked(self):
        self.faction1 = 'Random';
        self.filterByFactions();
        
    @QtCore.pyqtSlot()
    def on_rbRandom2_clicked(self):
        self.faction2 = 'Random';
        self.filterByFactions();
        
    @QtCore.pyqtSlot()
    def on_pbAllReps_clicked(self):
        self.showReps(self.allReps)
        self.faction1 = None
        self.faction2 = None
        self.ui.rbNoFaction1.setChecked(True)
        self.ui.rbNoFaction2.setChecked(True)
        print self.faction1, self.faction2
        
    def filterByFactions(self):
        factions = []
        if self.faction1 is not None:
            factions.append(self.faction1)
        if self.faction2 is not None:
            factions.append(self.faction2)
        filteredReps = filter.byFactions(factions, self.allReps)
        self.showReps(filteredReps)
        print self.faction1, self.faction2
        
app = QApplication(sys.argv)
repToolWindow = Ra3ReplayToolWindow()
sys.exit(app.exec_())
        