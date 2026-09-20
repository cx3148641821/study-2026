import json
from pathlib import Path

# 数据文件固定叫todos.json，与本文件在同一目录

DATA_FILE = Path(__file__).parent / "todos.json"

def load_todos():
    # 读全部待办。没有文件就当空列表，不报错
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE,encoding="utf-8") as f:
        return json.load(f)

def save_todos(todos):
    with open(DATA_FILE,"w",encoding="utf-8") as f:
        json.dump(todos,f,ensure_ascii=False,indent=2)

def next_id(todos):
    if not todos:
        return 1
    return max(item["id"] for item in todos)+1