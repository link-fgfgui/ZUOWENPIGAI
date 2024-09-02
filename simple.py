import libPiGai
import pprint
import json
# result=libPiGai.EN_Image_Correct("1D.jpg")
result = libPiGai.CN_Image_Correct(
    "2.jpg", "阅读下面的材料,根据要求写作。(60分)“质疑××,理解××,成为××”是在特定的人生阶段,面对特定的认知对象,客观存在的动态心理过程,也是心智成长、成熟的必经阶段。对此,你有怎样的联想和思考？请写一篇文章,谈谈自己的看法。要求：选准角度,确定立意,明确文体,自拟标题;不要套作,不得抄袭;不得泄露个人信息;不少于800字。","能力与选择")
pprint.pp(result)
with open("./result.json", 'w')as f:
    json.dump(result, f)
