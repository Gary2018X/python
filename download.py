#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Gary
import tkinter as tk
from tkinter import filedialog, messagebox
import requests
import time
import os


class App():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('批量下载小工具')  # 标题
        self.window.geometry('1000x600')  # 这里的乘是小x
        self.window.resizable(0, 0)  # 防止用户改窗口大小
        self.version = '1.7.2'
        tip = tk.Label(self.window,
                           text='欢迎使用python版批量下载小工具，如果有任何bug，请及时联系发布者，谢谢！\n导入url下载仅支持txt文本文件。\n使用前请仔细阅读说明文档！\n版本号：{}'.format(
                               self.version), font=('Arial', 12), width=66, height=4)
        tip.pack()
        try:  # 添加图片
            img_gif = tk.PhotoImage(file='bg.gif')
            label_img = tk.Label(self.window, image=img_gif)
            label_img.pack()
        except:  # 没加载成功会自动下载背景图片
            tk.messagebox.showwarning(title='提示消息', message='背景图片加载失败，请重启应用！')
            image_path = os.getcwd()
            bg = requests.get('http://download.gary666.com/bg.gif')
            try:
                if bg.content:
                    file = open(image_path + '/' + 'bg.gif', "wb")  # 采用二进制的形式存储文件
                    file.write(bg.content)
                    file.flush()
                    file.close()
            except:
                pass

        tk.Label(self.window, text='目标路径:', font=14).place(x=125, y=275)
        self.path = tk.Text(self.window, font=('Arial', 14), height=3, width=50)
        self.path.place(x=225, y=280)
        btn_select = tk.Button(self.window, text='选择路径', command=self.select_path, width=10, height=1, font=14,
                               bg='#00BFFF')
        btn_select.place(x=785, y=280)

        tk.Label(self.window, text='所有的url:', font=('Arial', 14)).place(x=125, y=310)
        self.var_url = tk.Text(self.window, font=('Arial', 14), height=10, width=50)
        self.var_url.place(x=225, y=310)
        btn_download2 = tk.Button(self.window, text='导入url', command=self.import_data, width=10, height=1, font=14,
                                  bg='#00BFFF')
        btn_download2.place(x=115, y=340)

        btn_delete = tk.Button(self.window, text='清空输入', command=self.delete, width=10, height=1, font=14, bg='#00BFFF')
        btn_delete.place(x=785, y=460)
        btn_download1 = tk.Button(self.window, text='确认下载', command=self.download, width=10, height=1, font=14,
                                  bg='#00BFFF')
        btn_download1.place(x=785, y=500)
        self.window.mainloop()

    def select_path(self):  # 选择路径
        path = filedialog.askdirectory()
        try:
            self.path.delete('1.0', 'end')
        except:
            pass
        self.path.insert('insert', path)

    def download(self):  # 下载
        url = self.var_url.get('0.0', 'end')
        if not url.strip():  # 判断输入是否为空
            tk.messagebox.showwarning(title='提示消息', message='输入为空请重新输入！')
        else:
            path_ = self.path.get('0.0', 'end')  # 这样读取会多换行符
            if not path_.strip():
                tk.messagebox.showwarning(title='提示消息', message='未选择存储路径！')
            else:
                path_ = path_.replace('\n', '')
                URL = url.split(',')
                # print(URL)
                try:
                    # 设置下载进度条
                    tk.Label(self.window, text='下载进度:', font=('Arial', 14)).place(x=125, y=550)
                    canvas = tk.Canvas(self.window, width=465, height=22, bg="red")
                    canvas.place(x=225, y=550)
                    fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
                    x = len(URL) - 2  # 未知变量，可更改
                    n = 465 / x  # 465是矩形填充满的次数
                    error = 0  # 出错次数
                    for i in range(x):
                        n = n + 465 / x
                        canvas.coords(fill_line, (0, 0, n, 60))
                        self.window.update()
                        time.sleep(0.02)  # 控制进度条流动的速度
                        try:
                            # print(URL[i+1])
                            r = requests.get(URL[i + 1])
                            if r.content:
                                # print(path_ + '/' + URL[i + 1].split('/')[-1].split('+')[-1])
                                try:  # 异常处理保存文件失败
                                    file = open(path_ + '/' + URL[i + 1].split('/')[-1].split('+')[-1],
                                                "wb")  # 采用二进制的形式存储文件
                                    file.write(r.content)
                                    file.flush()
                                    file.close()
                                except:
                                    error += 1
                                    tk.messagebox.showerror(title='提示消息', message='第{}个保存文件错误，请重试或联系管理员！'.format(i + 1))
                                    file.close()
                        except:
                            error += 1
                            tk.messagebox.showerror(title='提示消息', message='第{}个的url错误或发生异常，请检查格式或重试！'.format(i + 1))
                    tk.messagebox.showinfo(title='提示消息', message='下载{}个文件成功！'.format(x - error))
                except:
                    tk.messagebox.showerror(title='提示消息', message='异常错误，请重试或联系管理员！')

    def import_data(self):  # 从txt文件导入url下载
        filename = filedialog.askopenfilename(filetypes=[("text file", "*.txt")])
        try:
            f = open(filename, 'r', encoding='utf-8')
            content = f.read()
            self.var_url.insert('insert', content)
            f.close()
        except UnicodeDecodeError:  # 编码错误
            tk.messagebox.showerror(title='提示消息', message='编码错误，可将文件另存为，然后选择编码utf-8或联系管理员！')
        except:
            tk.messagebox.showerror(title='提示消息', message='异常错误，请重试或联系管理员！')

    def delete(self):  # 清空输入框
        self.var_url.delete('0.0', 'end')


app = App()
