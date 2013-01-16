# !/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import subprocess

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
        self.ui = ui_main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        
        self.faction1 = None
        self.faction2 = None
        self.allReps = []
        self.currentReps = []
        self.loadReps()
        
    #读取电脑上的录像文件
    def loadReps(self):        
        for file in path.getReplayFiles():
            self.allReps.append(decoder.decodeFile(file))
        self.currentReps = self.allReps
        self.showCurrentReps()
        
    #列表渲染显示回放
    def showCurrentReps(self):
        tmpListItems = []
        self.ui.lwReplays1.clear()
        for rep in self.currentReps:
            icon = QIcon(':res/images/' + rep['map']['image'])
            listItem = QListWidgetItem(icon, rep['name'], self.ui.lwReplays1)
            listItem.setTextAlignment(0x0004)
            
    #播放按钮点击事件
    @QtCore.pyqtSlot()
    def on_pbPlay_clicked(self):
        ra3EXE = path.getRa3Path() + 'ra3.exe';
        index = self.ui.lwReplays1.currentRow()
        repFile = self.currentReps[index]['filename'];
        cmd = '"' + ra3EXE + '" -replayGame "' + repFile + '"'
        cmd = cmd.encode('gbk')
        print cmd, type(cmd)
        subprocess.Popen(cmd)
    
        
    #下面都是阵营单选框点击事件
    @QtCore.pyqtSlot()
    def on_rbSoviet1_clicked(self):
        self.faction1 = 'Soviet';
        self.filterByFactions();
        
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
    
    #所有回放按钮点击事件
    @QtCore.pyqtSlot()
    def on_pbAllReps_clicked(self):
        self.currentReps = self.allReps
        self.showCurrentReps()
        self.faction1 = None
        self.faction2 = None
        self.ui.rbNoFaction1.setChecked(True)
        self.ui.rbNoFaction2.setChecked(True)
    
    #按阵营筛选
    def filterByFactions(self):
        factions = []
        if self.faction1 is not None:
            factions.append(self.faction1)
        if self.faction2 is not None:
            factions.append(self.faction2)
        self.currentReps = filter.byFactions(factions, self.allReps)
        self.showCurrentReps()
        
app = QApplication(sys.argv)
repToolWindow = Ra3ReplayToolWindow()
sys.exit(app.exec_())
        