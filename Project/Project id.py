from pdf2image import convert_from_path
import cv2
from PIL import Image

path_pdf = input("Enter the name of the pdf file: ")
images = convert_from_path(
    path_pdf,
    dpi=500,
    poppler_path=r'C:\\Users\\hp\\Desktop\\poppler-24.08.0\\Library\\bin'
)
images[0].save('page.jpg', 'JPEG')

id_top_left = (2400, 1740)
id_bottom_right = (3175, 1869)

phone_top_left = (490, 1740)
phone_bottom_right = (1475, 1869)

image = cv2.imread('page.jpg')

cv2.rectangle(image, id_top_left, id_bottom_right, (255, 255, 255), thickness=-1)
cv2.rectangle(image, phone_top_left, phone_bottom_right, (255, 255, 255), thickness=-1)

id_value = input("Enter the ID value: ")
phone_value = input("Enter the phone number: ")

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2.5
font_color = (0, 0, 0)  
thickness = 5


cv2.putText(image, id_value, (id_top_left[0] + 20, id_bottom_right[1] - 30), font, font_scale, font_color, thickness)

cv2.putText(image, phone_value, (phone_top_left[0] + 20, phone_bottom_right[1] - 30), font, font_scale, font_color, thickness)

cv2.imwrite('image.jpg', image)


final_image = Image.open("image.jpg").convert("RGB")
final_image.save("final_result.pdf")

