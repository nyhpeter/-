import pytesseract
from PIL import Image

im = Image.open('D:\OneDrive\照片\屏幕快照\\屏幕截图 2021-12-31 110052.png')

string = pytesseract.image_to_string(im)

print(string)


#, lang='chi_sim'

