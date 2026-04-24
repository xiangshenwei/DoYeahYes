import pyautogui
import time
from src.utils.common import is_chinese, is_english


def open_terminal():
    # 切换成中文
    switch_cn()
    pyautogui.keyDown("command")
    pyautogui.press("space")
    pyautogui.keyUp("command")
    time.sleep(1)
    pyautogui.write('zhongduan', interval=0.1)
    pyautogui.press('1')
    time.sleep(1)
    pyautogui.press('enter')


def switch_cn():
    box = is_english()
    if box:
        x, y = box
        print(f"当前是英文，准备按CapsLock切换成中文，坐标{x}, {y}")
        pyautogui.moveTo(x, y, duration=0.2)
        pyautogui.click(interval=0.2)
        pyautogui.moveTo(x, 82, duration=0.2)
        pyautogui.click(interval=0.2)


def switch_en():
    box = is_chinese()
    if box:
        x, y = box
        print(f"当前是中文，准备按CapsLock切换成英文，坐标{x}, {y}")
        pyautogui.moveTo(x, y, duration=0.2)
        pyautogui.click(interval=0.2)
        pyautogui.moveTo(x, 64, duration=0.2)
        pyautogui.click(interval=0.2)


def move_to(x:float, y:float):
    pyautogui.moveTo(x, y, duration=0.2)


def move_to_click(x:float, y:float):
    move_to(x, y)
    click()


def click(mode:str = None):
    if mode == "right":
        pyautogui.click(button='right', interval=0.2)
    else:
        pyautogui.click(interval=0.2)


def type_text(text):
    pyautogui.write(text, interval=0.1)


def enter():
    pyautogui.press("enter")


def sleep(s=1):
    time.sleep(s)


def input_command(commands=None):
    if commands is None:
        commands = []
    switch_en()


    time.sleep(1)

    for i, cmd in enumerate(commands):
        print(f"执行第{i + 1}/{len(commands)}步: {cmd}")
        type_text(cmd)
        enter()
        sleep()