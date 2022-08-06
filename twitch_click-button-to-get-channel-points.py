import time

import pyautogui

# Found this awesomeness on Reddit lol
# https://www.reddit.com/r/learnpython/comments/99fer7/comment/e4neq6p/?utm_source=share&utm_medium=web2x&context=3
from PIL import ImageGrab
from functools import partial

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)


def find_button(button_name):
    button = pyautogui.locateOnScreen(button_name, confidence=0.8)
    if button is None:
        return False
    else:
        return button


DELAY = 10 * 60  # Time to wait before clicking
TIMES_CLICKED = 0
BUTTON_FILENAME = "twitch-button.png"  # File to use when looking for button to click
while True:
    x, y = pyautogui.position()  # Get current location of mouse cursor

    claim_button = find_button(BUTTON_FILENAME)
    if claim_button:
        current_time = time.strftime("%H:%M%p", time.localtime())
        print("Claim button found!")

        claim_center = pyautogui.center(claim_button)
        pyautogui.moveTo(claim_center.x, claim_center.y)  # Location of button
        pyautogui.click(button='left')  # Click button to receive channel points
        pyautogui.moveTo(x, y)  # Go back to where ever we started

        TIMES_CLICKED = TIMES_CLICKED + 1
        print("Collected channel points", TIMES_CLICKED, "time(s). Last time collected at", current_time)
        time.sleep(DELAY)
    else:
        print("Claim button not found...waiting 10s before retrying click.")
        time.sleep(10)
        find_button(BUTTON_FILENAME)
