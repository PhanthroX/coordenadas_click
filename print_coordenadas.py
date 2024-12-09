import pyautogui

x, y = 1785, 755
screenshot = pyautogui.screenshot(region=(x, y, 25, 25))
screenshot.show()