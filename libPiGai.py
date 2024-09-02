import requests
import time
import base64
from AuthV3Util import addAuthParams
from config import APP_KEY,APP_SECRET


def EN_Image_Correct(image_path: str, limited_words: int = 80):
    data = {
        "q": str(base64.b64encode(open(image_path, 'rb').read()), 'utf-8'),
        'grade': "high",
        "isNeedSynonyms": "true",
        "correctVersion": "advanced",
        "isNeedEssayReport": "true",
        "limitedWords": limited_words
    }
    addAuthParams(APP_KEY, APP_SECRET, data)
    return requests.post("https://openapi.youdao.com/v2/correct_writing_image", data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'}).json()


def CN_Image_Correct(image_path: str, requirement: str,title:str):
    data = {
        "q": str(base64.b64encode(open(image_path, 'rb').read()), 'utf-8'),
        'grade': "g11",
        "requirement": requirement,
        "title":title
    }
    addAuthParams(APP_KEY, APP_SECRET, data)
    return requests.post("https://openapi.youdao.com/correct_writing_cn_image", data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'}).json()
