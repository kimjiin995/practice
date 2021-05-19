from openpyxl import Workbook
from openpyxl.drawing.image import Image

wb = Workbook()
ws = wb.active
img = Image("C:/Users/kjiin/Pictures/peng5.jpg")

ws.add_image(img, "E5")

wb.save("sample_image.xlsx")