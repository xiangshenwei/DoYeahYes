import time

import pyautogui
from src.config import ROOT


def at(*paths):
    print(f"Paths: {paths} , {ROOT}")
    return ROOT.joinpath(*paths)


def img(name):
    return at("images", name)


def is_chinese():
    try:
        box = pyautogui.locateOnScreen(str(img("zh.png")), confidence=0.8)
        if not box:
            return None
        return (
            mac_real(box.left + box.width / 2),
            mac_real(box.top + box.height / 2)
        )
    except pyautogui.ImageNotFoundException:
        return False


def is_english():
    try:
        box = pyautogui.locateOnScreen(str(img("en.png")), confidence=0.8)
        if not box:
            return None
        return (
            mac_real(box.left + box.width / 2),
            mac_real(box.top + box.height / 2)
        )
    except pyautogui.ImageNotFoundException:
        return False


def mac_real(i:float):
    scale = 2  # Mac Retina 常见
    return i/scale


def find_img_x_y(img_name: str):
    try:
        box = pyautogui.locateOnScreen(str(img(img_name)), confidence=0.8)
        if not box:
            return None
        xy = (
            mac_real(box.left + box.width / 2),
            mac_real(box.top + box.height / 2)
        )
        x, y = xy
        print(f"xy : {x}, y : {y}")
        pyautogui.moveTo(x, y, duration=0.2)
        return xy
    except pyautogui.ImageNotFoundException:
        print(f"img_name : {img_name} not found")
        return False


def find_img_x_y_click(img_name: str):
    box = find_img_x_y(img_name)
    if box:
        x, y = box
        pyautogui.moveTo(x, y, duration=0.2)
        time.sleep(1)
        pyautogui.click(interval=1)


def find_img_x_y_click_right(img_name: str):
    box = find_img_x_y(img_name)
    if box:
        x, y = box
        pyautogui.moveTo(x, y, duration=0.2)
        time.sleep(1)
        pyautogui.click(button='right')