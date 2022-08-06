# import pyautogui, sys
# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr)
# except KeyboardInterrupt:
#     print('\n')
import time

import pyautogui

t = time.strftime("%I:%M %p")
print(t)