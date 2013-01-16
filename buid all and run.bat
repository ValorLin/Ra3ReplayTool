@SET pythonPath=C:/Python/Python27
@SET pyqtPath=%pythonPath%/Lib/site-packages/PyQt4
@SET workPath=C:/Users/weilao/GitHub/Ra3ReplayTool
@echo 生成ui_.py文件
@"%pythonPath%/python" "%pyqtPath%/uic/pyuic.py" -o "%workPath%/ui_main.py" "%workPath%/main.ui" %1 %2 %3 %4 %5 %6 %7 %8 %9
@echo 生成_rc.py文件
@"%pyqtPath%/pyrcc4" -o "%workPath%/res_rc.py" "%workPath%/res.qrc" %1 %2 %3 %4 %5 %6 %7 %8 %9
@echo 启动程序
@"%pythonPath%/python" "%workPath%/ra3replaytool.pyw" -run -i
pause