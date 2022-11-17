import cv2 as cv

img = cv.imread('/home/viktor/Изображения/oguzok.jpg')
new_img = img


def click_event(event, x, y, flags, params):
    # checking for left mouse clicks
    if event == cv.EVENT_LBUTTONDOWN:
        global x1, y1, colorR, colorG, colorB
        x1, y1 = x, y
        colorB = img[y, x, 0]
        colorG = img[y, x, 1]
        colorR = img[y, x, 2]
        colors = img[y, x]
        print(f"{colorR}, {colorG}, {colorB}")
        # print("Coordinates of pixel: X: ", x, "Y: ", y)


def coordinates(x, y, red, green, blue):
    img[y, x] = (255 - red, 255 - green, 255 - blue)
    Y1, Y2 = y - 50 if y >= 50 else 0, y + 50 if y <= 450 else 499
    X1, X2 = x - 50 if x >= 50 else 0, x + 50 if x <= 450 else 499
    print(X1, X2)
    print(Y1, Y2)
    cropped = img[y - 50:
                  y + 50,
                  x - 50:
                  x + 50]
    return cropped


click_event(cv.EVENT_LBUTTONDOWN, 100, 100, None, None)
cv.namedWindow("chef i oguzok", cv.WINDOW_NORMAL)
cv.resizeWindow("chef i oguzok", 1000, 700)
cv.namedWindow("Resized_Window", cv.WINDOW_NORMAL)
cv.resizeWindow("Resized_Window", 500, 500)
cv.setMouseCallback('chef i oguzok', click_event)

while 1:
    new_img = coordinates(x1, y1, colorR, colorG, colorB)

    cv.imshow('chef i oguzok', img)
    cv.imshow('Resized_Window', new_img)
    if cv.waitKey(20) % 0xFF == ord('q'):
        break
cv.destroyAllWindows()
