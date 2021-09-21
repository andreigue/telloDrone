import cv2
import pytesseract

def thresh(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    finalImg = cv2.adaptiveThreshold(imgGray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,31,2) #anything below 100 (darkness) will stay dark, rest becomes 255 (white)
    ret2, finalImg2 = cv2.threshold(imgGray, 200, 255, cv2.THRESH_BINARY) #anything below 100 (darkness) will stay dark, rest becomes 255 (white)
    return finalImg, finalImg2

def canny(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    finalImg = cv2.Canny(imgGray, 100,100)
    return finalImg


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

imgOriginal =  cv2.imread("../Resources/phonefriend.jpg")
img = imgOriginal.copy()
img2 = img.copy()
cv2.imshow("img", img)
cv2.waitKey(1000)
# cv2.imshow("Text",img)
thresh,thresh2 = thresh(img)

# list = []
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# for contour in contours:
#     cv2.drawContours(img,contour,-1, (255,0,0),3)
#     x,y,w,h = cv2.boundingRect(contour)
#     rect = cv2.rectangle(img,(x,y), (x+w, y+h),(0,255,0),2)
#     cropped = thresh[y:y+h, x:x+w]
#     cropped = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)
#     pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#     text = pytesseract.image_to_string(cropped)
#     list.append(text)
# print(list)
#====================================================

# canny = canny(img2)
# contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# for contour in contours:
#     cv2.drawContours(img2,contour,-1, (255,0,0),3)
#     x,y,w,h = cv2.boundingRect(contour)
#     rect = cv2.rectangle(img2,(x,y), (x+w, y+h),(0,255,0),2)
#     cropped = imgOriginal[y:y+h, x:x+w]
#     pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#     text = pytesseract.image_to_string(cropped)
#     print(text)
#
# cv2.imshow("img2canny", img2)
# cv2.imshow("canny", canny)

#================================


print(pytesseract.image_to_string(thresh))

# cv2.imshow("imgthresh", img)
cv2.imshow("thresh", thresh)
cv2.imshow("thresh2", thresh2)

cv2.waitKey(0)





