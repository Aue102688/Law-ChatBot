from tkinter import W
import nltk
import pythainlp
import pprint
import deepcut
import random


def clean_words(words):
    stopwords = pythainlp.corpus.common.thai_stopwords()
    data = []
    list_word = [
        "อยาก",
        "ไป",
        "ต่อ",
        "กัน",
        "ขอบคุณ",
        "ใคร",
        "คือ",
        "สงสัย",
        "เห็น",
        "ให้",
        "หน่อย",
        "คืออะไร",
        "อะไร",
        "บ้าง",
        "ได้",
        "เพียง",
        "เเค่ไหน",
        "ไหน",
        "ทำไม",
        "เป็น",
        "ที่",
        "ใน",
        "อย่าง",
        "ไร",
        "ต้อง",
        "ยัง",
        "ไง",
        "เป็น",
        "หรือ",
        "ไม่",
        "พร้อม",
        "กับ",
        "เเค่",
        "ข้อ",
        "ความหมาย",
        "มี",
        "น้อย",
        "รับรอง",
        "ถูก",
        "คำ",
        # ข้อ1
        "การการุณยฆาต",
        "ทำยังไง",
        # ข้อ2
        "เป็นคนทำ",
        "ใครมีหน้าที่",
        # ข้อ3
        "กฏหมาย",
        "ประเทศไทย",
        "ในไทย",
        # ข้อ4
        "การ",
        "อื่น",
        "นอก",
    ]
    for word in words:
        word = word.strip()
        if word in list_word:
            data.append(word)

        if word not in stopwords:
            data.append(word)

    return data


# def get_features(data):
#     words = deepcut.tokenize(data)
#     words = clean_words(words)
#     data = {"words": " ".join(words), "count": len(words)}
#     return data


def get_features(data):

    words = deepcut.tokenize(data)
    words = clean_words(words)
    frequency = dict()
    for word in words:
        if word not in frequency:
            frequency[word] = 1
        else:
            frequency[word] += 1

    features = dict()

    # def get_features(data):
    #     words = deepcut.tokenize(data)
    #     words = clean_words(words)
    #     features = {}

    # ทักทาย
    features["สวัสดี"] = (
        "สวัสดี" in words
        or "โย่ว" in words
        or "Hi" in words
        or "สบายดี" in words
        or "ดี" in words
        or "hi" in words
        or "หวัดดี" in words
        or "โย่ว" in words
    )
    features["นายชื่อไร"] = (
        "ชื่อ" in words or "ชื่ออะไร" in words or "ชื่อไร" in words or "ชื่อไรคับ"
    )
    features["quest_one"] = (
        "หนึ่ง" in words or "1" in words or "อยากทราบข้อ 1" in words or "ข้อ 1" in words
    )
    features["quest_two"] = (
        "สอง" in words or "2" in words or "อยากทราบข้อ 2" in words or "ข้อ 2" in words
    )
    features["quest_three"] = (
        "สาม" in words or "3" in words or "อยากทราบข้อ 3" in words or "ข้อ 3" in words
    )
    features["quest_four"] = (
        "สี่" in words or "4" in words or "อยากทราบข้อ 4" in words or "ข้อ 4" in words
    )
    features["quest_five"] = (
        "ห้า" in words or "5" in words or "อยากทราบข้อ 5" in words or "ข้อ 5" in words
    )
    features["quest_six"] = (
        "หก" in words or "6" in words or "อยากทราบข้อ 6" in words or "ข้อ 6" in words
    )
    features["quest_seven"] = (
        "เจ็ด" in words or "7" in words or "อยากทราบข้อ 7" in words or "ข้อ 7" in words
    )
    features["quest_eight"] = (
        "เเปด" in words or "8" in words or "อยากทราบข้อ 8" in words or "ข้อ 8" in words
    )
    features["quest_nine"] = (
        "เก้า" in words or "9" in words or "อยากทราบข้อ 9" in words or "ข้อ 9" in words
    )
    features["quest_ten"] = (
        "สิบ" in words
        or "10" in words
        or "อยากทราบข้อ 10" in words
        or "ข้อ 10" in words
    )

    # เเก้
    features["ข้อ 9"] = "ข้อ 9'" in words
    features["ข้อ 10"] = "ข้อ 10'" in words
    features["ข้อ 2"] = "ข้อ 2'" in words

    # คำถาม
    features["เมนู"] = "เมนู" in words
    features["คำ"] = "คำ" in words
    features["สั่ง"] = "สั่ง'" in words

    # question
    features["question"] = (
        "บอท" in words
        or "น้อย" in words
        or "ทำ" in words
        or "ทำ" in words
        or "อะไร" in words
        or "บอทน้อยทำอะไรได้มั้ง" in words
    )
    # ตัวเลือกในการถามตอบ
    features["ชื่อ"] = "ชื่อ" in words
    features["ต่อ"] = "ต่อ" in words
    features["ต่อไป"] = "ต่อไป" in words
    features["หัวข้อ"] = "หัวข้อ" in words
    features["สงสัย"] = "สงสัย" in words or "สง" in words or "สัย" in words
    features["ข้อมูล"] = "ข้อมูล" in words
    features["อยาก"] = "อยาก" in words
    features["ทราบ"] = "ทราบ" in words
    features["หัวข้อ"] = "หัวข้อ" in words
    features["ข้อ"] = "ข้อ" in words
    features["ถัด"] = "ถัด" in words
    features["ไป"] = "ไป" in words
    features["ถัดไป"] = "ถัดไป" in words
    features["อะไร"] = "อะไร" in words
    features["ทำ"] = "ทำ" in words
    features["ได้"] = "ได้" in words
    features["เพียง"] = "เพียง" in words
    features["ใด"] = "ใด" in words
    features["ไหน"] = "ไหน" in words
    features["ไหม"] = "ไหม" in words
    features["ทำไม"] = "ทำไม" in words
    features["เเค่"] = "เเค่" in words
    features["ใคร"] = "ใคร" in words
    features["เป็น"] = "เป็น" in words
    features["ที่"] = "ที่" in words
    features["ทำ"] = "ทำ" in words
    features["ไม"] = "ไม" in words
    features["ถกเถียง"] = "ถกเถียง" in words
    features["กัน"] = "กัน" in words
    features["ใน"] = "ใน" in words
    features["การ"] = "การ" in words
    features["ความหมาย"] = "ความหมาย" in words
    features["ความหมายของ"] = "ความหมายของ" in words or "ความหมายของการ" in words
    features["มี"] = "มี" in words
    features["ของ"] = "ของ" in words
    features["สังคม"] = "สังคม" in words
    features["ต้องการ"] = "ต้องการ" in words
    features["อย่างไร"] = "อย่างไร" in words
    features["เเค่ไหน"] = "เเค่ไหน" in words
    features["ต้อง"] = "ต้อง" in words
    features["ขัด"] = "ขัด" in words
    features["รัฐธรรมนูญ"] = "รัฐธรรมนูญ" in words
    features["รู้"] = "รู้" in words
    features["ถูก"] = "ถูก" in words
    features["พร้อม"] = "พร้อม" in words
    features["หน้าที่"] = "หน้าที่" in words
    features["ไทย"] = "ไทย" in words
    features["ไอ้บอทโง่"] = "ไอ้บอทโง่" in words
    # features["ถามนอกเรื่อง"] = "ถามนอกเรื่อง" in words or "ถามเรื่องอื่น" in words or "ถามไม่เกี่ยวกับกฎหมาย" in words
    features["another"] = (
        "ถาม" in words
        or "นอก" in words
        or "เรื่อง" in words
        or "อื่น" in words
        or "ถามนอกเรื่อง" in words
        or "ถามเรื่องอื่น" in words
        or "ถามไม่เกี่ยวกับกฎหมาย" in words
    )

    # Event
    features["เกม"] = "เกม" in words
    features["รูป"] = "รูป" in words
    features["เห็น"] = "เห็น" in words
    features["Game"] = "Game" in words or "game" in words or "GAME" in words
    features["image"] = "image" in words

    # การจากลา
    features["ขอบคุณ"] = (
        "ขอบคุณ" in words
        or "thank" in words
        or "ใจ" in words
        or "ใจจ้า" in words
        or "ขอบใจ" in words
    )

    # ข้อ1
    features["คืออะไร"] = "คือ" in words or "คืออะไร" in words or "หมายถึงอะไร" in words
    features["การการุณยฆาต"] = (
        "การุณยฆาต" in words or "การการุณยฆาต" in words or "การุณ" in words
    )
    features["เป็นการทำอะไร"] = (
        "เป็นการทำ" in words or "ทำอะไร" in words or "ทำยังไง" in words
    )

    # ข้อ2
    features["ใครมีหน้าที่"] = (
        "ใคร" in words or "มีหน้าที่" in words or "หน้าที" in words
    )
    features["คนทำ"] = "คนทำ" in words or "ทำ" in words or "ทำการ" in words

    # ข้อ3
    features["กฏหมาย"] = (
        "กฏหมาย" in words or "ผิดกฏหมาย" in words or "ถูกกฏหมาย" in words
    )
    features["ประเทศไทย"] = "ไทย" in words or "ในไทย" in words or "ในไทยถูกไหม" in words
    features["ผิด"] = "ผิด" in words or "ผิดไหม" in words
    features["ได้"] = "ได้" in words or "ได้ไหม" in words

    # ข้อ4
    features["วิธีการทำการุณยฆาต"] = "วิธีการทำการุณยฆาต" in words
    features["วิธีการ"] = "วิธีการ" in words
    features["วิธี"] = "วิธี" in words
    features["การ"] = "การ" in words
    features["ทำ"] = "ทำ" in words

    # ข้อ5
    features["รับรอง"] = (
        "รับรอง" in words or "ยอมรับ" in words or "สามารถทำได้" in words
    )

    data = {"words": " ".join(words), "count": len(words)}
    data.update(features)
    return data
