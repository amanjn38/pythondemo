# import pyautogui
# from PIL import Image, ImageGrab
# import time
#
#
# # from numpy import asarray
#
# def hit(key):
#     pyautogui.keyDown(key)
#
#
# def draw():
#     pass
#
#
# def takess():
#     pass
#
#
# def isCollide(data):
#     for i in range(250, 300):
#         for j in range(562, 650):
#             if data[i, j] < 100:
#                 hit('down')
#                 return
#
#     for i in range(250, 300):
#         for j in range(410, 562):
#             if data[i, j] < 100:
#                 hit('up')
#                 return
#
#     return
#
#
# if __name__ == '__main__':
#     print("Hey, Dino game to start in 3 seconds")
#     time.sleep(2)
#     hit('up')
#     while 1:
#         image = ImageGrab.grab().convert('L')
#         data = image.load()
#         isCollide(data)
#         # if isCollide(data):
#         #     hit('up')
#         # print(asarray(image))
#         for i in range(300, 415):
#             for j in range(610, 650):
#                 data[i, j] = 0
#
#         for i in range(300, 415):
#             for j in range(410, 610):
#                 data[i, j] = 71
#
# #     image.show()

import pyautogui  # pip install pyautogui
from PIL import Image, ImageGrab  # pip install pillow
# from numpy import asarray
import time


def hit(key):
    pyautogui.keyDown(key)
    return


def isCollide(data):
    # Draw the rectangle for birds
    for i in range(300, 415):
        for j in range(410, 563):
            if data[i, j] < 100:
                hit("down")
                return

    for i in range(300, 415):
        for j in range(563, 650):
            if data[i, j] < 100:
                hit("up")
                return
    return


if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

        # print(asarray(image))

        # Draw the rectangle for cactus
        for i in range(675, 705):
            for j in range(370, 410):
                data[i, j] = 0

        # Draw the rectangle for birds
        for i in range(665, 695):
            for j in range(300, 370):
                data[i, j] = 171

        image.show()
        break

