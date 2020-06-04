"""
numpy version == 1.18.4
qrcode version == 6.1
pillow version == 7.1.2
pyzbar version == 0.1.8
opencv-python version == 4.1.2.30

dectect 讀取現在 .py檔路徑下 Cipher.png
"""

import numpy
import cv2
import pyzbar.pyzbar as pyzbar
from PIL import Image, ImageDraw, ImageFont
import qrcode
from datetime import datetime as dt


def decodeDisplay(imagex1):

    gray = cv2.cvtColor(imagex1, cv2.COLOR_BGR2GRAY)
    barcodes = pyzbar.decode(gray)

    for barcode in barcodes:
        
        # 條形碼資料為位元組物件，所以如果我們想在輸出影象上
        # 畫出來，就需要先將它轉換成字串
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        return barcodeData

        """ for showing image

        # 提取條形碼的邊界框的位置
        # 畫出影象中條形碼的邊界框
        (x, y, w, h) = barcode.rect
        cv2.rectangle(imagex1, (x, y), (x + w, y + h), (255, 255, 0), 2)

        # 不能顯示中文
        # 繪出影象上條形碼的資料和條形碼型別
        # text = "{} ({})".format(barcodeData, barcodeType)
        # cv2.putText(imagex1, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,5, (0, 0, 125), 2)

        # 更換為：
        img_PIL = Image.fromarray(cv2.cvtColor(imagex1, cv2.COLOR_BGR2RGB))

        # 引數（字型，預設大小）
        font = ImageFont.truetype("arial.ttf", 15)
        # 字型顏色（rgb)
        fillColor = (255, 0, 0)
        # 文字輸出位置
        position = (x, y - 10)
        # 輸出內容
        str = barcodeData

        # 需要先把輸出的中文字元轉換成Unicode編碼形式(  str.decode("utf-8)   )

        draw = ImageDraw.Draw(img_PIL)
        draw.text(position, str, font=font, fill=fillColor)
        # 使用PIL中的save方法儲存圖片到本地
        # img_PIL.save('02.jpg', 'jpeg')
        # 轉換回OpenCV格式
        imagex1 = cv2.cvtColor(numpy.asarray(img_PIL), cv2.COLOR_RGB2BGR)
        # 向終端列印條形碼資料和條形碼型別
        #print("掃描結果==》 類別： {0} 內容：\n{1}".format(barcodeType, barcodeData))
        """

    return ""

    # display, but I don't need it
    #cv2.imshow("camera", imagex1)
    #cv2.waitKey(0)

    #cv2.destroyAllWindows()

# input:    string
# output:   [string, string]
def detect(path):
    # read image and detect.
    # DIR 'Cipher.png'
    #cv2.namedWindow("camera", cv2.WINDOW_NORMAL)
    img = Image.open(path)

    frame = cv2.imread(path)
    return [decodeDisplay(frame), get_hidden_key(img)]


# input:    string, string
# output:   string
def QR_generator(ciphertext, key):
    # generator the QRcode but just display it.
    img = qrcode.make(ciphertext)
    #img.show()
    img_rgb = img.convert("RGB")
    hide_key(img_rgb, key)

    filename = dt.today().strftime("%Y-%m-%d %H.%M.%S") + ' Cipher.png'
    img_rgb.save(filename)
    img_rgb.show()
    return filename


# input:    PIL Image, string
# output:   nothing
def hide_key(image, key):
    key_byt = bytearray(key.encode("utf-8"))

    for x in range(image.size[0]):
        for y in range(image.size[1]):
            r, g, b = image.getpixel((x, y))
            if (len(key_byt) > 0):
                tmp_byt = key_byt[0]
                r = r | 4
                r = (r & 252) + (tmp_byt >> 6)
                g = (g & 248) + ((tmp_byt & 63) >> 3)
                b = (b & 248) + (tmp_byt & 7)
                image.putpixel((x, y), (r, g, b))
                key_byt = key_byt[1:]
            else:
                image.putpixel((x, y), (r & 251, g, b))


# input:    PIL Image
# output:   string
def get_hidden_key(image):
    msg = []
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            r, g, b = image.getpixel((x, y))
            if ((r & 4) > 0):
                tmp_byt = (r & 3)
                tmp_byt = (tmp_byt << 3) + (g & 7)
                tmp_byt = (tmp_byt << 3) + (b & 7)
                msg.append(tmp_byt)
            else:
                break

    return ''.join(chr(e) for e in msg)