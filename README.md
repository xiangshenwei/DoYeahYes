# DoYeahYes 🚀

一个基于 PyAutoGUI 的自动化工具

## 功能一：用于快速完成 SSH 登录流程。
背景：公司提供了服务器用户sysmgr、root的密码。其中root只能通过sysmgr切换过去。
现在要使用无密码用户bes。 流程为ssh sysmgr 输密码; su - root 输密码;
su - bes。 不考虑做免密登录的情况下，如此输密码简直折磨。

- 自动打开终端
- 自动 SSH 登录
- 自动切换 root / bes 用户

## 🆕 新人快速上手

### 1️⃣ 克隆项目

```bash
git clone https://github.com/xiangshenwei/DoYeahYes.git
cd DoYeahYes

```


### 2️⃣ 创建虚拟环境
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ 安装依赖
```bash
pip install -r requirements.txt
```

### 4️⃣ mac 必须设置权限（⚠️ 非常重要）

由于项目基于 PyAutoGUI，需要系统权限：

打开：

系统设置 → 隐私与安全

开启以下权限：

✅ 辅助功能（Accessibility）
✅ 屏幕录制（Screen Recording）

👉 勾选你的终端（Terminal / iTerm）或打包后的程序

### 5️⃣ 运行
```bash
python main.py config.yaml
```

### 6️⃣ 可选：录制坐标模式
```bash
python main.py record
```
👉 使用方式：

鼠标移动到目标位置
按 s → 输出坐标
按 q → 退出


## 🧩 内置策略（Strategy）说明
| function 名称              | 说明                 | 参数（params）                     |
| ------------------------ | ------------------ | ------------------------------ |
| open_terminal            | 打开终端（自动切换中文输入法）    | 无                              |
| input_command            | 批量输入命令并逐条执行（自动切英文） | `list[str]`：命令列表               |
| sleep                    | 延迟执行               | `int / float`：秒（默认1秒）          |
| move_to                  | 移动鼠标到指定位置          | `[x, y]`：坐标                    |
| move_to_click            | 移动鼠标并左键点击          | `[x, y]`：坐标                    |
| click                    | 点击当前鼠标位置           | `str`（可选）：`"right"` 表示右键，否则为左键 |
| find_img_x_y             | 查找图片并移动鼠标到目标位置     | `str`：图片名称（如 `"zh.png"`）       |
| find_img_x_y_click       | 查找图片并左键点击          | `str`：图片名称                     |
| find_img_x_y_click_right | 查找图片并右键点击          | `str`：图片名称                     |
| type_text                | 输入文本（不回车）          | `str`：文本内容                     |
| switch_cn                | 切换为中文输入法           | 无                              |
| switch_en                | 切换为英文输入法           | 无                              |
| wait_input               | 等待用户手动按回车继续        | 无                              |

---
## 🧪 参数示例（更新版）

### 1️⃣ 输入命令

```yaml
- step:
    function: input_command
    params:
      - "ssh user@ip"
      - "password"
      - "su - root"
    is_do: true
```

---

### 2️⃣ 延迟

```yaml
- step:
    function: sleep
    params: 2
    is_do: true
```

---

### 3️⃣ 鼠标移动

```yaml
- step:
    function: move_to
    params: [500, 300]
    is_do: true
```

---

### 4️⃣ 左键点击（当前位置）

```yaml
- step:
    function: click
    is_do: true
```

---

### 5️⃣ 右键点击

```yaml
- step:
    function: click
    params: right
    is_do: true
```

---

### 6️⃣ 移动并点击

```yaml
- step:
    function: move_to_click
    params: [500, 300]
    is_do: true
```

---

### 7️⃣ 图像识别（仅移动）

```yaml
- step:
    function: find_img_x_y
    params: "login.png"
    is_do: true
```

---

### 8️⃣ 图像识别 + 左键点击

```yaml
- step:
    function: find_img_x_y_click
    params: "login.png"
    is_do: true
```

---

### 9️⃣ 图像识别 + 右键点击

```yaml
- step:
    function: find_img_x_y_click_right
    params: "login.png"
    is_do: true
```

---

### 🔟 输入文本（不回车）

```yaml
- step:
    function: type_text
    params: "hello world"
    is_do: true
```

---

### 1️⃣1️⃣ 切换输入法

```yaml
- step:
    function: switch_en
    is_do: true

- step:
    function: switch_cn
    is_do: true
```

---

### 1️⃣2️⃣ 手动暂停（等待用户操作）

```yaml
- step:
    function: wait_input
    is_do: true
```

---

## ⚠️ 参数规则（更新版）

* `input_command` → 必须是 **list[str]**
* `move_to / move_to_click` → 必须是 **[x, y]**
* `click` →

  * 不传：左键
  * `"right"`：右键
* `sleep` → `int / float`
* `type_text` → `str`
* `find_img_x_y*` → 图片名称（必须放在 `images/` 目录）
* `switch_en / switch_cn / open_terminal / wait_input` → **无参数**

---

## 💡 小技巧（增强版）

* 所有 `params` 支持变量替换（如 `{ip}`、`{user}`）
* `{input}` 可复用整段命令列表
* `find_img_x_y` 实际会**移动鼠标到目标位置**
* Retina 屏（Mac）已自动做坐标缩放处理
* 图像识别建议：

  * 使用原始截图
  * 避免缩放 / 压缩
  * 保持分辨率一致

---

## 🚀 总结（更新版）

> STRATEGY + YAML
> = 可配置自动化流程引擎

> function 定义能力
> params 决定行为

👉 已支持：

* 鼠标控制
* 键盘输入
* 图像识别
* 输入法切换
* 人工干预（wait）


### last. 依赖锁定（开发者）

```bash
pip3 freeze > requirements.txt
```

### 打包
```bash
rm -rf build dist
pyinstaller main.py --name auto-run --add-data "images:images" --clean
```