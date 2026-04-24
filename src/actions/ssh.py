from src.config import Config
from src.actions.ui import *
from src.utils.common import *
from src.utils.peaple_do import wait_input


STRATEGY = {
    "open_terminal": open_terminal,
    "input_command": input_command,
    "sleep": sleep,
    "find_img_x_y": find_img_x_y,
    "find_img_x_y_click": find_img_x_y_click,
    "find_img_x_y_click_right": find_img_x_y_click_right,
    "move_to": move_to,
    "move_to_click": move_to_click,
    "click": click,
    "wait_input": wait_input,
    "type_text": type_text,
    "switch_cn": switch_cn,
    "switch_en": switch_en
}


def do_do_do(cfg: Config):
    for i, step in enumerate(cfg.steps):
        if not step['is_do']:
            continue

        func_name = step['function']
        print(f'do_do_do {i + 1} / {len(cfg.steps)}  {func_name}')

        func = STRATEGY.get(func_name)

        if not func:
            print(f"[WARN] 未找到策略: {func_name}")
            continue

        # 执行
        if 'params' in step:
            n = step.get('numbers')
            if isinstance(step['params'], list) and n is not None:
                func(*step['params'])
            else:
                func(step['params'])
        else:
            func()





