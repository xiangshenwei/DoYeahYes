import sys
from pathlib import Path

import yaml

if getattr(sys, 'frozen', False):
    ROOT = Path(sys._MEIPASS)
else:
    ROOT = Path(__file__).resolve().parent.parent

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


class Config:
    def __init__(self, path):
        row = load_yaml(path)
        cfg = row["config"]

        self.ip = cfg["ip"]
        self.user = cfg["user"]
        self.password = cfg.get("password", "")
        self.root_pass = cfg.get("root_pass", "")

        self.ctx = {
            "user": self.user,
            "ip": self.ip,
            "password": self.password,
            "root_pass": self.root_pass,
        }

        self.input = self.build_input(cfg)
        self.ctx.setdefault("{input}", self.input)
        self.steps = self.build_steps(cfg["steps"])


    def render(self, text: str):
        try:
            return text.format(**self.ctx)
        except KeyError as e:
            item = self.ctx.get(text)
            return item

    def build_input(self, cfg):
        return [self.render(i) for i in cfg["input"]]

    def build_steps(self, steps):
        result = []

        for item in steps:
            step = item["step"]

            new_step = {
                "function": step["function"],
                "is_do": step.get("is_do", True)
            }

            if "params" in step:
                if isinstance(step["params"], str):
                    new_step["params"] = self.render(step["params"])
                else:
                    new_step["params"] = step["params"]

            if "numbers" in step:
                new_step["numbers"] = step["numbers"]


            result.append(new_step)


        return result