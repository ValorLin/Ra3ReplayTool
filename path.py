# -*- coding: utf-8 -*-

import os
import _winreg

#获取系统目录
def getSysPath(key):
    #key = Personal我的文档,其他的请自行打开注册列表查看。
    path = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',)
    return _winreg.QueryValueEx(path, key)[0]

#获取目录下的所有录像文件
def getFiles(path):
    path = path.rstrip('/\\')
    path += '\\'
    files = []        
    for fileName in os.listdir(path):
        fullFileName = path + fileName            
        if os.path.isfile(fullFileName):#ToDo 检查扩展名
            files.append(fullFileName)            
    return files

#获取回放目录
def getRa3ReplayPath():
    return getSysPath('Personal') + '\\Red Alert 3\\Replays\\'

#获取所有回放文件名
def getReplayFiles():
    return getFiles(getRa3ReplayPath())
