import json
import os
import tkinter as tk
from importlib.metadata import entry_points
from tkinter import  scrolledtext,messagebox,filedialog



def browse_file():
    filepath = filedialog.askopenfilename(
        title= "选择一个文本文件",
        filetypes = [
        ("JSON 文件","*.json")
        ]
    )
    if filepath:
        entry.delete(0,tk.END)
        entry.insert(0,filepath)

#获取输入的路径
def get_user_file():
    #获取输入框的路径，如何前后去空字符
    file_path = entry.get().strip()

    try:
        with open(file_path,'r',encoding='utf-8') as f:
            data = json.load(f)
            formatted_json = json.dumps(data,ensure_ascii=False,indent=4)

        text_area.config(state='normal')  # 确保可写（虽然默认是 normal，但安全起见）
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, formatted_json)
        text_area.config(state='disabled')  # 设为只读，需要修改则删除掉这行

    except Exception as e:
        messagebox.showerror(f"无法读取文件:{str(e)}")

#创建一个主窗口
root = tk.Tk()
root.title("json排版脚本")
root.geometry("600x400") #这里乘号使用字母X代替

label  = tk.Label(root,text = "请输入文件路径")
label.pack(pady= 5)

#重新创建一个容器，将输入框和文件浏览按钮放入这个容器内，这样才能实现同行排列
input_frame = tk.Frame(root)
input_frame .pack(pady=5)


entry = tk.Entry(input_frame,width= 70)
entry.pack(side = tk.LEFT,padx=(0,5))

browse_btn = tk.Button(input_frame, text="浏览...", command=browse_file)
browse_btn.pack(side=tk.LEFT)  # 紧跟在输入框右侧


#command 后是要执行的是函数
button = tk.Button(root,text="加载文件",command=get_user_file)
button.pack(pady=5)

# 滚动文本区域（用于显示文件内容）
text_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    width=70,
    height=20,
    font=("Microsoft YaHei", 12)  # ← 关键：设置字体和大小
)
text_area.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

def on_enter(event):
    get_user_file()
entry.bind('<Return>',on_enter)

#启动GUI，并保持启动状态
root.mainloop()

