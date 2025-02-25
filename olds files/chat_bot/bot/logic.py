# bot.logic.py
LOGIC_RESPONSES = { 
    'test': [
        "You can find your account information on https://www.codingforentrepreneurs.com/account/"
    ], 

    "สวัสดี" : [
        'สวัสดีสุดหล่อของข่อย สูเจ้างงหม่องใดแค่พิมพ์ว่า(สังสัย)ก็จะพบกับหัวข้อต่างๆ',
    ],

    "สงสัย" : [
        'สูเจ้าอยากทราบเกี่ยวกับอะไรบอทน้อยจะตอบให้เด้อ(พิมพ์แค่ตัวเลข) \n1.การการุณยฆาตคืออะไร \n2.ใครมีหน้าที่ทำการการุณยฆาต \n3. การุณยฆาตถูกกฎหมายไหมในประเทศไทย \n4. วิธีการทำการุณยฆาต   \n5. ประเทศที่รับรองการการุณยฆาตแบบถูกกฎหมาย \n6. การการุณยฆาตทำได้เพียงใดในประเทศไทย \n7. ทำไมการการุณยฆาตถึงเป็นที่ถกเถียงกันในสังคม \n8. หากต้องการทำการุณยฆาตต้องทำอย่างไร \n9. การที่การการุณยฆาตไม่ถูกรับรองในไทยถือเป็นการขัดรัฐธรรมนูญหรือไม่ \n10. การุณยฆาตพร้อมแค่ไหนในสังคมไทย'
    ],

    "1" : [
        'การทำให้เสียชีวิตอย่างสงบโดยมีมนุษยธรรม ซึ่ง การุณยฆาต คือ การยุติชีวิตของผู้ป่วยระยะสุดท้ายตามเจตนารมณ์ของผู้ป่วยหรือตามคำร้องขอของผู้แทนโดยชอบธรรม โดยมีโดยมีแพทย์เป็นผู้ดำเนินการยุติความเจ็บป่วย หรือเป็นผู้ทำให้ผู้ป่วยเสียชีวิตด้วยดี เป็นการยุติชีวิตโดยเจตนาเพื่อให้พ้นจากความเจ็บปวดทรมาน '
    ],

    "2" : [
        'ผู้ที่มีหน้าที่การุณยฆาต คือ แพทย์ เป็นผู้ดำเนินการยุติความเจ็บป่วย หรือเป็นผู้ทำให้ผู้ป่วยเสียชีวิต โดยในแต่ละประเทศที่กฎหมายอนุญาตให้การุณยฆาตได้นั้น จะมีข้อกำหนดและเงื่อนไขต่างกันออกไป ยกตัวอย่างเช่น เนเธอร์แลนด์ อนุญาตเฉพาะผู้ป่วยที่มีอายุ 12 ปี ขึ้นไป ผู้ป่วยระยะสุดท้ายที่ต้องทนทุกข์ทรมานจากอาการป่วยเท่านั้น และ ผู้ป่วยต้องมีสติสัมปชัญญะในการขอร้องแพทย์ให้มีการทำการุณยฆาต สหรัฐอเมริกา อนุญาตให้ผู้ป่วยระยะสุดท้าย ที่คาดว่าจะมีชีวิตไม่เกิน 6 เดือน ได้จบชีวิตด้วยตนเอง ภายได้การช่วยเหลือจากทีมแพทย์ในการเตรียมยาและอุปกรณ์ให้  ญี่ปุ่น อนุญาตเฉพาะผู้ป่วยระยะสุดท้าย พร้อมทั้งได้รับการยืนยันจากแพทย์ว่าไม่มีวิธีรักษา และได้รับการอนุญาตจากครอบครัวแล้ว เป็นต้น '
    ],

    "3" : [
        'ในประเทศไทย การการรุณยฆาตยังไม่ถูกกฎหมายและยังไม่มีกฎหมายรองรับ เพราะถือว่าเข้าข่ายการกระทำความผิด ตามประมวลกฎหมายอาญาฐานฆ่าผู้อื่นโดยเจตนา ยกเว้น เป็นการดูแลของแพทย์ผู้เชี่ยวชาญ'
    ],

    "4" : [
        'การขอการุณยฆาต มี 2 แบบ 1.การุณยฆาตเชิงรุก คือ การตั้งใจให้เสียชีวิต  2.การุณยฆาตเชิงรับ คือ การไม่ใช้เครื่องมือทางการแพทย์หรือปฎิเสธการรักษา'
    ],

    "5" : [
        'ปัจจุบันทั่วโลกมีเพียง 13 ประเทศที่มีกฎหมายรองรับการทำการุณยฆาต ได้แก่ เนเธอร์แลนด์, เบลเยียม, ลักเซมเบิร์ก, สวิตเซอร์แลนด์, ออสเตรเลีย, แคนาดา,โคลัมเบีย, สหรัฐอเมริกา, เยอรมนี, ญี่ปุ่น อินเดีย,และสเปน'
    ], 
    "6" : [
        'ประเทศไทยยังไม่มีกฎหมายที่อนุญาตให้ทำการุณยฆาต มีเพียงมาตรา 12 ใน พ.ร.บ.สุขภาพแห่งชาติ พ.ศ.2550 ซึ่งอนุญาตให้ผู้ป่วยระยะท้ายปฏิเสธการรักษาที่ไม่ได้ประโยชน์เท่านั้น'
    ],
    "7" : [
        'เพราะยังไม่มีกฎหมายรองรับ และถือว่าการการุณยฆาต ยังเป็นการกระทำที่ผิดกฎหมายอาญาเพราะมีผู้คนจำนวนมากไม่เห็นด้วย ถ้ามองในด้านศีลธรรมถือว่าเป็นการกระทำที่เป็นบาป ขัดต่อศีลธรรม'
    ],
    "8" : [
        'หากต้องการทำการุณยฆาต สามารถแบ่งได้เป็น 2 ประเภท ได้แก่ 1.การยินยอมให้แพทย์หรือผู้อื่นที่ได้รับอนุญาตกระทำการฉีดสารหรือใช้วัตถุยุติชีวิตตามเจตจำนงผู้ป่วย\n 2.การยุติชีวิตด้วยตัวผู้ป่วยเอง ไม่ว่าจะเป็นการให้ยา การฉีดหรือกดปุ่ม โดยมีแพทย์เตรียมอุปกรณ์และเครื่องมือให้ เรียกวิธีนี้ว่า Physician Assisted Suicide (PAS) ซึ่งเป็นวิธีที่สอดคล้องกับศีลธรรมและกฎหมายที่ทำให้ผู้ป่วยได้จบชีวิตด้วยตัวเองอย่างสงบ'
    ],
    "9" : [
        'การไม่มีการการุณยฆาตในประเทศไทยนั้นขัดตามรัฐธรรมนูญแห่งราชอาณาจักรไทย  การุณยฆาต ถือเป็นสิทธิมนุษยชนแบบหนึ่ง ที่มนุษย์ทุกคนพึงจะได้รับ และไม่ให้ผู้อื่นเข้ามาละเมิดได้ โดยสามารถอธิบายได้จากมนุษย์ย่อมมีสิทธิในร่างกายของตนเอง แต่เนื่องจากผู้อื่นหรือ แม้กระทั่งแพทย์ผู้รักษา ไม่สามารถกระทำการใดๆ ต่อบุคคลได้ หากผู้นั้นไม่ได้ยินยอมม ซึ่งสอดคล้องกับพระราชบัญญัติสุขภาพแห่งชาติ ปีพุทธศักราช 2550 ที่ระบุไว้ในหมวด 1 สิทธิและหน้าที่ด้านสุขภาพ ดังนี้\n“มาตรา 8 ในการบริการสาธารณสุข บุคลากรด้านสาธารณสุขต้องแจ้งข้อมูลด้านสุขภาพที่เกี่ยวข้องกับการให้บริการให้ผู้รับบริการ ทราบอย่างเพียงพอที่ผู้รับบริการจะใช้ประกอบการตัดสินใจในการรับ หรือไม่รับบริการใด และในกรณีที่ผู้รับบริการปฏิเสธไม่รับบริการใด จะให้บริการนั้นมิได้”\n“มาตรา 12 บุคคลมีสิทธิทําหนังสือแสดงเจตนาไม่ประสงค์จะรับบริการสาธารณสุขที่เป็นไปเพียงเพื่อยืดการตายในวาระสุดท้ายของชีวิตตน หรือเพื่อยุติการทรมานจากการเจ็บป่วยได้ การดําเนินการตามหนังสือแสดงเจตนาตามวรรคหนึ่ง ให้เป็นไป ตามหลักเกณฑ์และวิธีการที่กําหนดในกฎกระทรวง เมื่อผู้ประกอบวิชาชีพด้านสาธารณสุขได้ปฏิบัติตามเจตนาของ บุคคลตามวรรคหนึ่งแล้วมิให้ถือว่าการกระทํานั้นเป็นความผิดและให้ พ้นจากความรับผิดทั้งปวง”'
    ],
    "10" : [
        'ประเทศไทยจะพัฒนากฎหมายให้มีการการุณยฆาตได้นั้นจะต้องใช้เวลาในการทำความเข้าใจร่วมกันอีกมาก เพราะเกี่ยวข้องกับมิติทางการแพทย์ กฎหมาย และความเชื่อทางศาสนา แม้แต่การบัญญัติมาตรา 12 แห่งพระราชบัญญัติสุขภาพแห่งชาติ พ.ศ. 2550 ก็ยังปรากฏว่ายังมีผู้โต้แย้งไม่เห็นด้วยอีกมาก'
    ],              
    
    "ขอบคุณนะ" : [
        'ไม่เป็นไรจ้า ถ้ายังสงสัยอยู่ก็พิมพ์(สงสัย) แล้วลองเลือกหัวข้อที่ไม่เข้าใจดูน้า',
        'ขอบคุณที่สนใจเช่นกันจ้า ถ้ายังสงสัยอยู่ก็พิมพ์(สงสัย) มาได้เลยน้า'
    ],              
    
}
