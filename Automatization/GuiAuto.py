import pyautogui


width, height = pyautogui.size()
print(width, height)
print(pyautogui.position())
pyautogui.moveTo(500,500)
#pyautogui.moveTo(100,100, duration=2)
#pyautogui.moveRel(200, 0)
#pyautogui.moveRel(200, 0)
pyautogui.moveRel(-200, 200, duration=1)
pyautogui.click(517, 17)
pyautogui.click(373, 201)

