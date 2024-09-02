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
app = QApplication()
ui = Ui_Form()
window = QWidget()
ui.setupUi(window)
j = json.load(open("result.json"))
j = j["Result"]
orgContent = j["orgContent"]
ui.zongpingjiaLabel.setText(j["commentCollection"]["comment"])
ui.lcdNumber.setDigitCount(3)
ui.lcdNumber.display(j["scoreCollection"]["score"])
satisfyRequirements = ["", "对题意的理解不够充分，有偏题的嫌疑。", "能理解题目要求，文章基本符合题意。",
                       "能较好地把握题目要求，文章符合题意。", "能正确理解题目要求，文章符合题意。", "能准确理解题目要求，文章切合题意。"]
themeExplicits = ["中心不够明确，立意不够清晰。", "中心不够明确，立意不够清晰。", "虽有中心主题，但表达不够充分有力，文章略显空洞。",
                  "主题基本明确。", "主题较明确。", "主题明确，立意鲜明。"]
goodSents = ["", "用词过于平淡，缺乏文采。", "偶尔使用好词好句，语言平淡质朴。",
             "能够适当运用好词好句，语言生动活泼。", "遣词造句优美，文章富有文采。", "本文语言极其优美，文章极富文学气息。"]
sentimentSinceritys = ["感受不深刻，缺乏感染力。", "情感缺乏深度。", "语言简朴，感情平淡，情意不够深切。",
                       "感情真实，发自肺腑。", "情感饱满，情真意切，能深深打动读者。", "感情真挚动人，情感丰沛，极富感染力。"]
structureStricts = ["条理不清，结构混乱。", "层次不清，结构较乱。", "层次欠清楚，结构较合理。",
                    "层次较分明，结构完整。", "层次清晰，结构完整。", "层次清晰，结构严谨。"]
essayFluences = ["语句不通顺，表述不清晰，令人费解。", "语句欠通，缺乏连贯性。", "语句基本通顺，偶有不畅。",
                 "语句通顺流畅。", "语句流畅连贯，自然通达。", "语言平滑晓畅，可读性强。"]
ui.listWidget.addItem(
    themeExplicits[j["scoreCollection"]["perspectiveScore"]["themeExplicit"]])
ui.listWidget.addItem(
    satisfyRequirements[j["scoreCollection"]["perspectiveScore"]["satisfyRequirement"]])
ui.listWidget.addItem(
    sentimentSinceritys[j["scoreCollection"]["perspectiveScore"]["sentimentSincerity"]])
ui.listWidget.addItem(
    structureStricts[j["scoreCollection"]["perspectiveScore"]["structureStrict"]])
ui.listWidget.addItem(
    essayFluences[j["scoreCollection"]["perspectiveScore"]["essayFluence"]])
ui.listWidget.addItem(
    goodSents[j["scoreCollection"]["perspectiveScore"]["goodSent"]])


de=j["detailedEvaluation"]
cc=j["correctedContent"]
ui.textBrowser.setText(j["orgContent"])

window.show()

app.exec()
