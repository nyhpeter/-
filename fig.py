import os
import pytesseract
from PIL import Image


#path
path = 'D:\OneDrive\照片\屏幕快照\带变化的真实阻尼\\'



imgs = [path + i for i in os.listdir(path)]


f = open('text.txt','w+',encoding='utf-8')

for img in imgs:
    f.write(img +'\n')

f.close()

string=pytesseract.image_to_string('text.txt',lang='chi_sim')

print(string)

