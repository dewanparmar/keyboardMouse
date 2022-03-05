from pynput.keyboard import Key, Controller as key_control
from pynput.mouse import Button, Controller
import time 
import random
keyboard = key_control()
mouse = Controller()
while True:
    key_num=random.randint(50, 200)
    mouse_num=random.randint(10, 50)
    count_num=random.randint(1, 5)
    for i in range(key_num):
        keyboard.press(Key.ctrl)
        keyboard.release(Key.ctrl)
    for j in range(mouse_num):
        mouse.press(Button.left)
        mouse.release(Button.left)
    keyboard.press(Key.ctrl)
    for i in range(count_num):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
    keyboard.release(Key.ctrl)
    time.sleep(60 - time.time() % 60)   
