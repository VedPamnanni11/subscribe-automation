import pyautogui
import time

channel = pyautogui.prompt(text="Enter a youtube channel name", title="Automation")

time.sleep(2)

pyautogui.keyDown("command")
pyautogui.press("space")
pyautogui.keyUp("command")
pyautogui.write("safari")
pyautogui.press("return")

time.sleep(1)

pyautogui.keyDown("command")
pyautogui.press("t")
pyautogui.keyUp("command")

time.sleep(2)

pyautogui.write("youtube.com")
pyautogui.press("return")

time.sleep(7)

search = pyautogui.locateCenterOnScreen("search.png", confidence=0.9)
pyautogui.click(search.x // 2, search.y // 2)
pyautogui.write(channel)
pyautogui.press("return")

time.sleep(5)

subscribe = pyautogui.locateCenterOnScreen("subscribe.png", confidence=0.9)
pyautogui.click(subscribe.x // 2, subscribe.y // 2)