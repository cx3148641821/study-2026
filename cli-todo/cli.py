# import storage
# # print(storage.load_todos())
# storage.save_todos([{'id':1,'title':'买菜','done':False}])
# print(storage.load_todos())

import storage
import argparse
import sys

def cmd_add(args):
    todos = storage.load_todos()
    todo ={
        "id":storage.next_id(todos),
        'title':args.title, #argprase解析出来的位置参数
        'done':False,
    }
    todos.append(todo)
    storage.save_todos(todos)
    print(f"已添加[{todo['id']}]{todo['title']}")

def cmd_list(args):
    todos=storage.load_todos()
    if not todos:
        print("(无暂办)")
        return
    for item in todos:
        mark = "x" if item["done"] else " "
        print(f"[{mark}] {item['id']}  {item['title']}")

def cmd_done(args):
    
    todos =storage.load_todos()
    for item in todos:
        if item["id"] == args.id:
            item["done"] = True
            storage.save_todos(todos)
            print(f"已完成[{item['id']} {item['title']}]")
            return
    print(f"错误：不存在id={args.id}",file=sys.stderr)
    sys.exit(1)


def build_parser():
    parser=argparse.ArgumentParser(description="极简待办清单：add/list/done")
    sub = parser.add_subparsers(dest="command",required=True)

    p_add = sub.add_parser("add",help="添加一条待办事项")
    p_add.add_argument("title",help="代办内容，例如：买菜")
    p_add.set_defaults(func=cmd_add)

    p_list = sub.add_parser("list",help="列出全部待办事项")
    p_list.set_defaults(func=cmd_list) 

    p_done = sub.add_parser("done",help="标记完成")
    p_done.add_argument("id",type=int,help="待办数字 id")
    p_done.set_defaults(func=cmd_done)
    return parser



def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()