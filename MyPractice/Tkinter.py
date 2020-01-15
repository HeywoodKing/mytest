# -*- coding: UTF-8 -*-

import tkinter

root = tkinter.Tk()


li = ['C', 'python', 'php', 'html', 'SQL', 'java', 'C#']
movie = ['css', 'jquery', 'bootstrap']
listb = tkinter.Listbox(root)
listb2 = tkinter.Listbox(root)

for item in li:
    listb.insert(0, item)

for item in movie:
    listb2.insert(0, item)

listb.pack()
listb2.pack()

button = tkinter.Button()
button.info = '123'

button.pack()


# 进入循环消息体
root.mainloop()



