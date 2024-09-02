import json
from UI import Ui_Form
from PySide6.QtCore import (QCoreApplication, 
    QMetaObject,  QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (
    QFont)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLCDNumber, QLabel, QListWidget,
    QListWidgetItem, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
app=QApplication()
ui=Ui_Form()
window=QWidget()
ui.setupUi(window)
j=json.load(open("result1.json"))
j=j["Result"]
rawEssay=j["rawEssay"]
# ui.textBrowser.setText()
ui.zongpingjiaLabel.setText(j["essayAdvice"])
ui.lcdNumber.setDigitCount(3)
ui.lcdNumber.display(j["totalScore"])
ui.listWidget.addItem("文章句子数:{}".format(j["sentNum"]))
ui.listWidget.addItem("文章词数:{}".format(j["wordNum"]))
ui.listWidget.addItem("简评:{}".format(j["totalEvaluation"]))
ui.listWidget.addItem("语法:{}".format(j["majorScore"]["grammarScore"]))
ui.listWidget.addItem("评价:{}".format(j["majorScore"]["grammarAdvice"]))
ui.listWidget.addItem("内容:{}".format(j["majorScore"]["topicScore"]))
ui.listWidget.addItem("词汇:{}".format(j["majorScore"]["wordScore"]))
ui.listWidget.addItem("评价:{}".format(j["majorScore"]["wordAdvice"]))
ui.listWidget.addItem("逻辑:{}".format(j["majorScore"]["structureScore"]))
ui.listWidget.addItem("评价:{}".format(j["majorScore"]["structureAdvice"]))
sfb=j["essayFeedback"]['sentsFeedback']
from pprint import pp
# pp(sfb)
body=''
body_zongjie=''
for item in sfb:
    rawSent=item["rawSent"]
    if item["isContainGrammarError"] or item["isContainTypoError"]:
        raw=item["rawSent"]
        editPoints=[]
        for jtem in item["errorPosInfos"]:
            title=jtem["errBaseInfo"]
            red=jtem["orgChunk"]
            green=jtem["correctChunk"]
            sP=jtem["startPos"]
            eP=jtem["endPos"]
            editPoints.append({"s":sP,'e':eP,'t':'<span title="{}" style="color: red;">{}</span><span>/</span><span style="color: green;">{}</span>'.format(title,red,green)})
            if jtem.get("knowledgeExp") is not None:
                body_zongjie+="<span>{}<br/>例句[<br/>".format(jtem.get("knowledgeExp"))
                for ktem in jtem["exampleCases"]:
                    body_zongjie+=("&nbsp;&nbsp;&nbsp;&nbsp;"+ktem["right"]+"<br/>")
                body_zongjie+="]</span><br/><br/>"
        sp=0
        ep=len(raw)
        correct=[]
        for dtem in editPoints:
            ep=dtem['s']
            correct.append(raw[sp:ep])
            sp=dtem['e']
            correct.append(dtem['t'])
        correct.append(raw[sp:len(raw)])
        rawSent=''.join(correct)
    body+=rawSent+"<br/>"
ui.textBrowser
ui.textBrowser.setText("<html>"+rawEssay.replace("\n","<br/>")+"<br/><br/><br/>"+body+"<br/>"+body_zongjie+"</html>")

















window.show()



app.exec()