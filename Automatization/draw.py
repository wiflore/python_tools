import pyautogui

print(pyautogui.position())
pyautogui.click(802, 89)
pyautogui.click()
pyautogui.click(822, 272)

distance = 200
while distance > 0:
    print(distance, 0)
    pyautogui.dragRel(distance, 0, duration=0.0) # move right
    distance = distance - 4
    print(0, distance)
    pyautogui.dragRel(0, distance, duration=0.0) # move down
    print(-distance, 0)
    pyautogui.dragRel(-distance, 0, duration=0.0) # move left
    distance = distance - 10
    print(0, -distance)
    pyautogui.dragRel(0, -distance, duration=0.0) # move up