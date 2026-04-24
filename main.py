import sys
from pathlib import Path

import pyautogui
from pynput import keyboard

from src.actions.ssh import do_do_do
from src.config import Config

pyautogui.PAUSE = 0.2
pyautogui.FAILSAFE = True


def record_mode():
    print("进入录制模式：")
    print("👉 鼠标移动到目标位置")
    print("👉 输入 s  记录坐标")
    print("👉 输入 q  退出\n")

    def on_press(key):
        try:
            if key.char == 's':
                x, y = pyautogui.position()
                print(f"[记录] 坐标: [{x}, {y}]")

            elif key.char == 'q':
                print("退出录制模式")
                return False  # 停止监听

        except AttributeError:
            pass  # 忽略功能键

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def main():
    # ----------------------------
    # record 模式
    # ----------------------------
    if len(sys.argv) >= 2 and sys.argv[1] == "record":
        record_mode()
        return

    print("3秒后开始执行...")
    pyautogui.sleep(3)

    # ----------------------------
    # 正常执行模式
    # ----------------------------
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python main.py <config.yaml>")
        print("  python main.py record")
        sys.exit(1)

    config_file = sys.argv[1]
    path = Path(config_file)

    if not path.exists():
        print(f"[ERROR] config file not found: {config_file}")
        sys.exit(1)

    cfg = Config(path)
    do_do_do(cfg)


if __name__ == "__main__":
    main()